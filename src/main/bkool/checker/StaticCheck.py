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
    ## @param targetObj can be type of AttributeDecl, MethodDecl, VarDecl, ConstDecl
    ## @return name type str
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
        elif isinstance(targetObj, ClassType):
            return self.getASTName(targetObj.classname)
        else:
            return ""

    def getMemDeclType(self, memDecl: MemDecl):
        if isinstance(memDecl, MethodDecl):
            return memDecl.returnType
        else:
            storeDecl = memDecl.decl
            if isinstance(storeDecl, VarDecl):
                return storeDecl.varType
            else:
                return storeDecl.constType

    # @return MemDecl
    def searchMemberOfClassByName(self, classDecl: ClassDecl, targetMemberName: str):
        for mem in classDecl.memlist:
            memName = self.getASTName(mem)
            if memName == targetMemberName:
                return mem
        return None

    # @return MemDecl
    def searchMemberByName(self, targetMemberName: str):
        for mem in self.classScopeMembers:
            memName = self.getASTName(mem)
            if memName == targetMemberName:
                return mem
        return None

    ### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
    ## @param targetChildName is the child's name need to check (type: str)
    ## @param targetParentName is the parent's name need to check (type: str)
    ## @return True/False
    def checkIsKidOf(self, targetChildName: str, targetParentName: str):
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

    ### `checkStoreExist` function used to check if variable is declared within a block scope
    ## @param variable is the name to check
    ## @param varDecls is list of decl type StoreDecl that may contain variable
    ## @return True/False
    def checkStoreExist(self, variable: str, decls: List[StoreDecl]):
        for d in decls:
            if self.getASTName(d) == variable:
                return True
        return False

    ### `searchClass` function used to find existed class
    ## @param classname type str
    ## @param ClassDecl
    def searchClassByName(self, name: str):
        for decl in self.globalScopeDecls:
            if self.getASTName(decl) == name:
                return decl
        return None

    ### `searchVarDecl` function used to search a varDecl through name
    ## @param targetname name to search
    ## @param varDecls is list of varDecl that may contain varDecl with targetname
    ## @return VarDecl
    def searchDeclByName(self, targetname: str, decls: List[Decl]):
        for decl in decls:
            if self.getASTName(decl) == targetname:
                return decl
        return None

    ### `checkTypeMatch` function used to check if rhs has the same type to lhs or can be con be coerce to lhs
    ## @param lhsType type Type (left hand side Type)
    ## @param rhsType type Type (right hand side Type)
    ## @return True/False
    def checkTypeMatch(self, lhsType: Type, rhsType: Type):
        if type(lhsType) != type(rhsType):
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

    def visitId(self, ast: Id, visibleScopeDecls: List[Decl]):
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

    def visitBinaryOp(self, ast: BinaryOp, visibleScopeDecls: List[Decl]):
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

    def visitUnaryOp(self, ast: UnaryOp, visibleScopeDecls: List[Decl]):
        return ast.body.accept(self, visibleScopeDecls)

    def visitCallExpr(self, ast: CallExpr, visibleScopeDecls: List[Decl]):
        objName = self.getASTName(ast)
        classDecl = self.searchClassByName(objName)
        methodName = self.getASTName(ast.method)
        searchedMem = None
        if isinstance(ast.obj, SelfLiteral):
            searchedMem = self.searchMemberByName(methodName)
            if searchedMem == None or not isinstance(searchedMem, MethodDecl):
                raise Undeclared(Method(), methodName)
        for p in ast.param:
            p.accept(self, visibleScopeDecls)
        return self.getMemDeclType(searchedMem)

    def visitNewExpr(self, ast: NewExpr, visibleScopeDecls: List[Decl]):
        pass

    def visitArrayCell(self, ast: ArrayCell, visibleScopeDecls: List[Decl]):
        pass

    def visitFieldAccess(self, ast: FieldAccess, visibleScopeDecls: List[Decl]):
        objName = self.getASTName(ast)
        classDecl = self.searchClassByName(objName)
        fieldname = self.getASTName(ast.fieldname)
        searchedMem = None
        if isinstance(ast.obj, SelfLiteral):
            searchedMem = self.searchMemberByName(fieldname)
            if searchedMem == None or not isinstance(searchedMem, AttributeDecl):
                raise Undeclared(Attribute(), fieldname)
        elif classDecl == None:
            objType = ast.obj.accept(self, visibleScopeDecls)
            if not isinstance(objType, ClassType):
                raise IllegalMemberAccess(ast)
            classDeclName = self.getASTName(objType)
            classDecl = self.searchClassByName(classDeclName)
            searchedMem = self.searchMemberOfClassByName(classDecl, fieldname)
            if searchedMem == None:
                raise IllegalMemberAccess(ast)
        else:
            searchedMem = self.searchMemberOfClassByName(classDecl, fieldname)
            if searchedMem == None:
                raise IllegalMemberAccess(ast)
            if not isinstance(searchedMem.kind, Static):
                raise IllegalMemberAccess(ast)
        return self.getMemDeclType(searchedMem)

    def visitIntLiteral(self, ast: IntLiteral, visibleScopeDecls: List[Decl]):
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, visibleScopeDecls: List[Decl]):
        return FloatType()

    def visitStringLiteral(self, ast: StringLiteral, visibleScopeDecls: List[Decl]):
        return StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, visibleScopeDecls: List[Decl]):
        return BoolType()

    def visitArrayLiteral(self, ast: ArrayLiteral, temp):
        eleType = ast.value[0].accept(self, temp)
        for v in ast.value:
            vType = v.accept(self, temp)
            if not (
                self.checkTypeMatch(vType, eleType)
                and self.checkTypeMatch(eleType, vType)
            ):
                raise IllegalArrayLiteral(ast)
        return ArrayType(len(ast.value), eleType)

    def visitAssign(self, ast: Assign, decls: List[StoreDecl]):
        lhsType = ast.accept(self, decls)
        rhsType = ast.accept(self, decls)
        if self.checkTypeMatch(lhsType, rhsType):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast: CallStmt, decls: List[StoreDecl]):
        print("loc")

    def visitVarDecl(self, ast: VarDecl, visibleScopeDecls: list[StoreDecl]):
        varType = ast.varType
        varInit = ast.varInit.accept(self, visibleScopeDecls) if ast.varInit else None

        if varInit:
            if not self.checkTypeMatch(varType, varInit):
                raise TypeMismatchInStatement(Assign(ast.variable, ast.varInit))
        return ast

    # @param visibleScopeDecls can be methodScopeDecls or blockScopeDecls
    def visitBlock(self, ast: Block, visibleScopeDecls: List[Decl]):
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

    def visitConstDecl(self, ast: ConstDecl, visibleScopeDecls: List[Decl]):
        constType = ast.constType
        value = ast.value.accept(self, visibleScopeDecls)

        if not self.checkTypeMatch(constType, value):
            raise TypeMismatchInConstant(ast)

        return ast

    def visitClassDecl(self, ast: ClassDecl, globalScopeDecls: List[Decl]):
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

    def visitMethodDecl(self, ast: MethodDecl, classScopeDecls: List[Decl]):
        # store all member's name of MemDecl in classScopeDecls
        memDeclNames = []
        for decl in classScopeDecls:
            memDeclNames.append(self.getASTName(decl))

        # check Redeclared method in Class scope
        methodName = self.getASTName(ast)
        if methodName in memDeclNames:
            raise Redeclared(Method(), methodName)

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

    def visitAttributeDecl(self, ast: AttributeDecl, classScopeDecls: List[MemDecl]):
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

    def visitProgram(self, ast: Program, c):
        # Store io class
        ioMembers = []
        for s in c:
            ioMembers.append(
                MethodDecl(
                    Static(),
                    s.name,
                    [VarDecl(Id("anArg"), s.mtype.partype)],
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
            self.globalScopeDecls.append(checkedClassDecl)
        print("ok in visitProgram")

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)
