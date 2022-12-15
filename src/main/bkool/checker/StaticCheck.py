"""
 * @author nhphung
 * Student's name: Le Tran Phuc Loc
 * Student's ID: 2013684
"""
from array import ArrayType
from re import error
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from typing import List


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("readInt", MType([], IntType())),
        Symbol("writeInt", MType([IntType()], VoidType())),
        Symbol("writeIntLn", MType([IntType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("writeFloatLn", MType([FloatType()], VoidType())),
        Symbol("readBool", MType([], BoolType())),
        Symbol("writeBool", MType([BoolType()], VoidType())),
        Symbol("writeBoolLn", MType([BoolType()], VoidType())),
        Symbol("readStr", MType([], StringType())),
        Symbol("writeStr", MType([StringType()], VoidType())),
        Symbol("writeStrLn", MType([StringType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast

    ### `getASTName` function used to get name of AST object
    ## @param targetObj can be type of AttributeDecl, MethodDecl, VarDecl, ConstDecl, ClassDecl, FieldAccess, ArrayCell, CallExpr, ClassType
    def getASTName(self, targetObj) -> str:
        if isinstance(targetObj, Id):
            return targetObj.name
        elif isinstance(targetObj, AttributeDecl):
            return self.getASTName(targetObj.decl)
        elif isinstance(targetObj, MethodDecl):
            return targetObj.name.name
        elif isinstance(targetObj, VarDecl):
            return targetObj.variable.name
        elif isinstance(targetObj, ConstDecl):
            return targetObj.constant.name
        elif isinstance(targetObj, ClassDecl):
            return targetObj.classname.name
        elif isinstance(targetObj, FieldAccess):
            return self.getASTName(targetObj.obj)
        elif isinstance(targetObj, ArrayCell):
            return self.getASTName(targetObj.arr)
        elif isinstance(targetObj, CallExpr):
            return self.getASTName(targetObj.obj)
        elif isinstance(targetObj, CallStmt):
            return self.getASTName(targetObj.obj)
        elif isinstance(targetObj, ClassType):
            return self.getASTName(targetObj.classname)
        else:
            return ""

    ### `getMemDeclType` function used to get Type of AST member of class
    def getMemDeclType(self, memDecl: MemDecl) -> Type:
        if isinstance(memDecl, MethodDecl):
            return memDecl.returnType
        else:
            storeDecl = memDecl.decl
            if isinstance(storeDecl, VarDecl):
                return storeDecl.varType
            else:
                return storeDecl.constType

    ### `searchClass` function used to find existed class
    def searchClassByName(self, name: str) -> ClassDecl:
        for decl in self.globalScopeDecls:
            if self.getASTName(decl) == name:
                return decl
        return None

    ### `searchMemberOfClassByName` search a member of other class in global scope
    def searchMemberOfClassByName(
        self, classDecl: ClassDecl, targetMemberName: str
    ) -> MemDecl:
        for mem in classDecl.memlist:
            memName = self.getASTName(mem)
            if memName == targetMemberName:
                return mem
        return None

    ### `searchMemberByName` search a member of current checking class
    def searchMemberByName(self, targetMemberName: str) -> MemDecl:
        for mem in self.classScopeMembers:
            memName = self.getASTName(mem)
            if memName == targetMemberName:
                return mem
        return None

    ### `searchVarDecl` function used to search a Decl through name
    def searchDeclByName(
        self, targetname: str, visibleScopeDecls: List[Decl]
    ) -> StoreDecl:
        for decl in visibleScopeDecls:
            if self.getASTName(decl) == targetname:
                return decl
        return None

    ### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
    def checkIsKidOf(self, targetChildName: str, targetParentName: str) -> bool:
        searchedChildClass = self.searchClassByName(targetChildName)
        if searchedChildClass == None:
            raise Undeclared(Class(), targetChildName)
        else:
            if searchedChildClass.parentname == None:
                return False
            parentOfTargetChild = searchedChildClass.parentname.name
            if parentOfTargetChild == targetParentName:
                return True
            else:
                return self.checkIsKidOf(parentOfTargetChild, targetParentName)

    ### `checkTypeMatch` function used to check if rhs has the same type to lhs or can be con be coerce to lhs
    def checkTypeMatch(self, lhsType: Type, rhsType: Type) -> bool:
        if type(lhsType) != type(rhsType):
            if isinstance(lhsType, FloatType) and isinstance(rhsType, IntType):
                return True
            else:
                return False
        else:
            if isinstance(lhsType, ClassType) and isinstance(rhsType, ClassType):
                lhsTypeClassName = lhsType.classname.name
                rhsTypeClassName = rhsType.classname.name
                return self.checkIsKidOf(rhsTypeClassName, lhsTypeClassName)
            if isinstance(lhsType, ArrayType) and isinstance(rhsType, ArrayType):
                if lhsType.size != rhsType.size:
                    return False
                return self.checkTypeMatch(lhsType.eleType, rhsType.eleType)
            return True

    def checkIsConstant(self, decl: Decl) -> bool:
        if isinstance(decl, ConstDecl):
            return True
        if isinstance(decl, AttributeDecl):
            return self.checkIsConstant(decl.decl)

    def visitAccess(self, ast, visibleScopeDecls: List[Decl], memDeclType):
        objName = self.getASTName(ast)
        classDecl = self.searchClassByName(objName)
        fieldname = self.getASTName(ast.fieldname if memDeclType == AttributeDecl else ast.method)
        searchedMember = None
        if isinstance(ast.obj, SelfLiteral):
            searchedMember = self.searchMemberByName(fieldname)
            if searchedMember == None or type(searchedMember) != memDeclType:
                errorKind = Attribute() if memDeclType == AttributeDecl else Method()
                raise Undeclared(errorKind, fieldname)
        elif classDecl == None:  # case obj is a variable type class
            objType = ast.obj.accept(self, visibleScopeDecls)
            if not isinstance(objType, ClassType):
                raise IllegalMemberAccess(ast)
            classDeclName = self.getASTName(objType)
            classDecl = self.searchClassByName(classDeclName)
            searchedMember = self.searchMemberOfClassByName(
                classDecl, fieldname
            )
            if searchedMember == None or not isinstance(
                searchedMember, memDeclType
            ):
                errorKind = Attribute() if isinstance(memDeclType, AttributeDecl) else Method()
                raise Undeclared(errorKind, fieldname)
        else:  # case obj is a class try to access static member
            searchedMember = self.searchMemberOfClassByName(classDecl, fieldname)
            if searchedMember == None or not isinstance(
                searchedMember, memDeclType
            ):
                errorKind = Attribute() if isinstance(memDeclType, AttributeDecl) else Method()
                raise Undeclared(errorKind, fieldname)
            if not isinstance(searchedMember.kind, Static):
                raise IllegalMemberAccess(ast)
        return searchedMember

    def visitId(self, ast: Id, visibleScopeDecls: List[Decl]) -> Type:
        searchedDecl = self.searchDeclByName(ast.name, visibleScopeDecls)
        if isinstance(searchedDecl, VarDecl):
            return searchedDecl.varType
        elif isinstance(searchedDecl, ConstDecl):
            return searchedDecl.constType
        elif isinstance(searchedDecl, AttributeDecl):
            storeDecl = searchedDecl.decl
            if isinstance(storeDecl, VarDecl):
                return storeDecl.varType
            elif isinstance(storeDecl, ConstDecl):
                return storeDecl.constType
        elif isinstance(searchedDecl, MethodDecl):
            return searchedDecl.returnType
        elif isinstance(searchedDecl, ClassDecl):
            return ClassType(ast.name)
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self, ast: BinaryOp, visibleScopeDecls: List[Decl]) -> Type:
        leftOperandType = ast.left.accept(self, visibleScopeDecls)
        rightOperandType = ast.right.accept(self, visibleScopeDecls)

        if ast.op in ["+", "-", "*", "/", "\\", "%"]:
            if not (
                (type(leftOperandType) in [IntType, FloatType])
                and (type(rightOperandType) in [IntType, FloatType])
            ):
                raise TypeMismatchInExpression(ast)
            if ast.op == "/":
                return FloatType()
            elif ast.op in ["\\", "%"]:
                if not (
                    isinstance(leftOperandType, IntType)
                    and isinstance(rightOperandType, IntType)
                ):
                    raise TypeMismatchInExpression(ast)
                return IntType()
            else:
                if isinstance(leftOperandType, IntType) and isinstance(
                    rightOperandType, IntType
                ):
                    return IntType()
                else:
                    return FloatType()
        elif ast.op in ["==", "!="]:
            if not (
                (
                    isinstance(leftOperandType, IntType)
                    and isinstance(rightOperandType, IntType)
                )
                or (
                    isinstance(leftOperandType, BoolType)
                    and isinstance(rightOperandType, BoolType)
                )
            ):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op in [">", "<", ">=", "<="]:
            if not (
                (type(leftOperandType) in [IntType, FloatType])
                and (type(rightOperandType) in [IntType, FloatType])
            ):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op == "^":
            if not (
                isinstance(leftOperandType, StringType)
                and isinstance(rightOperandType, StringType)
            ):
                raise TypeMismatchInExpression(ast)
            return StringType()

    def visitUnaryOp(self, ast: UnaryOp, visibleScopeDecls: List[Decl]) -> Type:
        return ast.body.accept(self, visibleScopeDecls)

    def visitCallExpr(self, ast: CallExpr, visibleScopeDecls: List[Decl]) -> Type:
        searchedMethodMember = self.visitAccess(ast, visibleScopeDecls, MethodDecl)
        paramDecls = []
        for p in searchedMethodMember.param:
            paramDecls.append(p.accept(self, []))
        paramPassed = []
        for p in ast.param:
            paramPassed.append(p.accept(self, visibleScopeDecls))
        if len(paramDecls) != len(paramPassed):
            raise TypeMismatchInExpression(ast)
        for i in range(0, len(paramDecls)):
            if not self.checkTypeMatch(paramDecls[i], paramPassed[i]):
                raise TypeMismatchInExpression(ast)

        return self.getMemDeclType(searchedMethodMember)

    def visitNewExpr(self, ast: NewExpr, visibleScopeDecls: List[Decl]):
        pass

    def visitArrayCell(self, ast: ArrayCell, visibleScopeDecls: List[Decl]):
        pass

    def visitFieldAccess(self, ast: FieldAccess, visibleScopeDecls: List[Decl]) -> Type:
        searchedAttributeMember = self.visitAccess(ast, visibleScopeDecls, AttributeDecl)
        return self.getMemDeclType(searchedAttributeMember)

    def visitIntLiteral(
        self, ast: IntLiteral, visibleScopeDecls: List[Decl]
    ) -> IntType:
        return IntType()

    def visitFloatLiteral(
        self, ast: FloatLiteral, visibleScopeDecls: List[Decl]
    ) -> FloatType:
        return FloatType()

    def visitStringLiteral(
        self, ast: StringLiteral, visibleScopeDecls: List[Decl]
    ) -> StringType:
        return StringType()

    def visitBooleanLiteral(
        self, ast: BooleanLiteral, visibleScopeDecls: List[Decl]
    ) -> BoolType:
        return BoolType()

    def visitArrayLiteral(self, ast: ArrayLiteral, temp) -> ArrayType:
        eleType = ast.value[0].accept(self, temp)
        for v in ast.value:
            vType = v.accept(self, temp)
            if not (
                self.checkTypeMatch(vType, eleType)
                and self.checkTypeMatch(eleType, vType)
            ):
                raise IllegalArrayLiteral(ast)
        return ArrayType(len(ast.value), eleType)

    def visitAssign(self, ast: Assign, visibleScopeDecls: List[StoreDecl]) -> None:
        lhsType = ast.lhs.accept(self, visibleScopeDecls)
        expType = ast.exp.accept(self, visibleScopeDecls)
        if isinstance(ast.lhs, Id):
            lhsName = self.getASTName(ast.lhs)
            decl = self.searchDeclByName(lhsName, visibleScopeDecls)
            if decl == None:
                raise Undeclared(Identifier(), lhsName)
            if self.checkIsConstant(decl):
                raise CannotAssignToConstant(ast)
        elif isinstance(ast.lhs, FieldAccess):
            searchedMember = self.visitAccess(ast.lhs)
            if isinstance(searchedMember.decl, ConstDecl):
                raise CannotAssignToConstant(ast)
        elif isinstance(ast.lhs, ArrayCell):
            pass
        else:
            # handle error (unknown)
            pass

        if not self.checkTypeMatch(lhsType, expType):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast: If, visibleScopeDecls: List[StoreDecl]):
        exprType = ast.expr.accept(self, visibleScopeDecls)
        if not isinstance(exprType, BoolType):
            raise TypeMismatchInStatement(ast)
        ast.thenStmt.accept(self, visibleScopeDecls)
        ast.elseStmt.accept(self, visibleScopeDecls)

    def visitFor(self, ast: For, visibleScopeDecls: List[StoreDecl]) -> None:
        idType = ast.id.accept(self, visibleScopeDecls)
        assignPart = Assign(ast.id, ast.expr1)
        assignPart.accept(self, visibleScopeDecls)
        if not isinstance(idType, IntType):
            raise TypeMismatchInStatement(ast)
        expr1Type = ast.expr1.accept(self, IntType)
        if not isinstance(expr1Type, IntType):
            raise TypeMismatchInStatement(ast)
        expr2Type = ast.expr2.accept(self, IntType)
        if not isinstance(expr2Type, IntType):
            raise TypeMismatchInStatement(ast)
        ast.loop.accept(self, visibleScopeDecls)

    def visitReturn(self, ast: Return, visibleScopeDecls: List[StoreDecl]) -> None:
        exprType = ast.expr.accept(self, visibleScopeDecls)
        if not self.checkTypeMatch(self.returnType, exprType):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast: CallStmt, visibleScopeDecls: List[StoreDecl]) -> None:
        searchedMethodMember = self.visitAccess(ast, visibleScopeDecls, MethodDecl)
        paramDecls = []
        for p in searchedMethodMember.param:
            paramDecls.append(p.accept(self, []))
        paramPassed = []
        for p in ast.param:
            paramPassed.append(p.accept(self, visibleScopeDecls))
        if len(paramDecls) != len(paramPassed):
            raise TypeMismatchInStatement(ast)
        for i in range(0, len(paramDecls)):
            if not self.checkTypeMatch(paramDecls[i], paramPassed[i]):
                raise TypeMismatchInStatement(ast)

    def visitVarDecl(self, ast: VarDecl, visibleScopeDecls: list[StoreDecl]) -> Type:
        varType = ast.varType
        varInit = ast.varInit.accept(self, visibleScopeDecls) if ast.varInit else None

        if varInit:
            if not self.checkTypeMatch(varType, varInit):
                raise TypeMismatchInStatement(Assign(ast.variable, ast.varInit))
        return varType

    def visitBlock(self, ast: Block, visibleScopeDecls: List[Decl]) -> None:
        extraVisibleScopeDecls = [*visibleScopeDecls]
        # check Redeclared between decls in Block
        blockScopeDeclNames = []
        blockDecls = ast.decl
        for decl in blockDecls:
            declName = self.getASTName(decl)
            if declName in blockScopeDeclNames:
                errorKind = Constant() if isinstance(decl, ConstDecl) else Variable()
                raise Redeclared(errorKind, declName)
            decl.accept(self, extraVisibleScopeDecls)
            blockScopeDeclNames.append(declName)
            extraVisibleScopeDecls.insert(0, decl)

        # check Error in statements
        blockStmts = ast.stmt
        for stmt in blockStmts:
            stmt.accept(self, extraVisibleScopeDecls)

    def visitConstDecl(self, ast: ConstDecl, visibleScopeDecls: List[Decl]) -> Type:
        constType = ast.constType
        value = ast.value.accept(self, visibleScopeDecls)

        if not self.checkTypeMatch(constType, value):
            raise TypeMismatchInConstant(ast)

        return constType

    def visitClassDecl(self, ast: ClassDecl, globalScopeDecls: List[Decl]) -> ClassDecl:
        # store all class'name of ClassDecl in globalScopeDecls
        classDeclNames = []
        for decl in globalScopeDecls:
            classDeclNames.append(self.getASTName(decl))

        # check Redeclared new class
        classname = self.getASTName(ast)
        if classname in classDeclNames:
            raise Redeclared(Class(), classname)

        # check Undeclared parent Class
        parentname = self.getASTName(ast.parentname)
        if parentname != "":
            if not parentname in classDeclNames:
                raise Undeclared(Class(), parentname)

        # init classScopeDecls
        classScopeDecls = []
        self.classScopeMembers = []

        # check Error in class's members
        classMembers = ast.memlist
        for mem in classMembers:
            checkedMember = mem.accept(self, classScopeDecls)
            self.classScopeMembers.append(checkedMember)
            classScopeDecls.append(checkedMember)

        print("ok in visitClassDecl")
        return ast

    def visitMethodDecl(
        self, ast: MethodDecl, classScopeDecls: List[Decl]
    ) -> MethodDecl:
        # store all member's name of MemDecl in classScopeDecls
        memDeclNames = []
        for decl in classScopeDecls:
            memDeclNames.append(self.getASTName(decl))

        # check Redeclared method in Class scope
        methodName = self.getASTName(ast)
        if methodName in memDeclNames:
            raise Redeclared(Method(), methodName)

        self.returnType = ast.returnType

        # init methodScopeDecls
        methodScopeDecls = []
        # check Redeclared in parameter
        paramNames = []
        paramDecls = ast.param
        for decl in paramDecls:
            paramName = self.getASTName(decl)
            if paramName in paramNames:
                raise Redeclared(Parameter(), paramName)
            paramNames.append(paramName)
            methodScopeDecls.append(decl)

        # check Redeclared if any decl of body redeclared in methodScopeDecls
        bodyDecls = ast.body.decl
        for decl in bodyDecls:
            declName = self.getASTName(decl)
            if declName in paramNames:
                errorKind = Constant() if isinstance(decl, ConstDecl) else Variable()
                raise Redeclared(errorKind, declName)

        # combine decl to pass to statements
        combineDecls = paramDecls + classScopeDecls

        # check Error in Block
        ast.body.accept(self, combineDecls)
        return ast

    def visitAttributeDecl(
        self, ast: AttributeDecl, classScopeDecls: List[MemDecl]
    ) -> AttributeDecl:
        # store all member's name of MemDecl in classScopeDecls
        memDeclNames = []
        for decl in classScopeDecls:
            memDeclNames.append(self.getASTName(decl))

        # check Redeclared attribute in Class scope
        attributeName = self.getASTName(ast)
        if attributeName in memDeclNames:
            raise Redeclared(Attribute(), attributeName)

        # check Error in StoreDecl
        ast.decl.accept(self, classScopeDecls)

        print("ok in visitAttributeDecl")
        return ast

    def visitProgram(self, ast: Program, c) -> None:
        # Store io class
        ioMembers = []
        for s in c:
            ioMembers.append(
                MethodDecl(
                    Static(),
                    Id(s.name),
                    [VarDecl(Id("anArg"), s.mtype.partype[0])]
                    if len(s.mtype.partype) != 0
                    else [],
                    s.mtype.rettype,
                    Block([], []),
                )
            )
        ioClassDecl = ClassDecl(Id("io"), ioMembers)

        # init globalScopeDecls
        self.globalScopeDecls = [ioClassDecl]
        # check Error in every classDecl
        classDecls = ast.decl
        for decl in classDecls:
            checkedClassDecl = decl.accept(self, self.globalScopeDecls)
            if checkedClassDecl != None:
                self.globalScopeDecls.append(checkedClassDecl)
        print("ok in visitProgram")

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)
