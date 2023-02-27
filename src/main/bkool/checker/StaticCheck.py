"""
 * @author nhphung
 * Student's name: Le Tran Phuc Loc
 * Student's ID: 2013684
"""
from re import error
from AST import *
from Visitor import *
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


class ExprRet:
    def __init__(self, type, isInitialized=None):
        self.astType = type
        self.isInitialized = isInitialized


class StaticChecker(BaseVisitor):

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
            return self.getASTName(targetObj.fieldname)
        elif isinstance(targetObj, ArrayCell):
            return self.getASTName(targetObj.arr)
        elif isinstance(targetObj, CallExpr):
            return self.getASTName(targetObj.obj)
        elif isinstance(targetObj, CallStmt):
            return self.getASTName(targetObj.obj)
        elif isinstance(targetObj, ClassType):
            return self.getASTName(targetObj.classname)
        elif isinstance(targetObj, NewExpr):
            return self.getASTName(targetObj.classname)
        else:
            return ""

    ### `getMemDeclType` function used to get Type of AST member of class(may be AttributeDecl, MethodDecl, VarDecl, ConstDecl)
    def getDeclType(self, memDecl: MemDecl) -> Type:
        if isinstance(memDecl, MethodDecl):
            return memDecl.returnType
        elif isinstance(memDecl, AttributeDecl):
            return self.getDeclType(memDecl.decl)
        elif isinstance(memDecl, VarDecl):
            return memDecl.varType
        elif isinstance(memDecl, ConstDecl):
            return memDecl.constType

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
    def searchDeclByName(self, targetname: str, visibleScopeDecls: List[Decl]):
        for decl in visibleScopeDecls:
            if self.getASTName(decl) == targetname:
                return decl
        return None

    ### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
    def checkIsKidOf(self, targetChildName: str, targetParentName: str) -> bool:
        searchedChildClass = self.searchClassByName(targetChildName)
        if searchedChildClass is None:
            raise Undeclared(Class(), targetChildName)
        else:
            if searchedChildClass.parentname is None:
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

    def assignVal(self, decl, val) -> None:
        if isinstance(decl, VarDecl):
            decl.varInit = val
        elif isinstance(decl, AttributeDecl):
            self.assignVal(decl.decl, val)

    ## @param memDeclType MethodDecl | AttributeDecl
    def visitAccess(self, ast, visibleScopeDecls: List[Decl], memDeclType):
        objName = self.getASTName(ast.obj)
        classDecl = self.searchClassByName(objName)
        fieldname = self.getASTName(
            ast.fieldname if memDeclType == AttributeDecl else ast.method
        )
        searchedMember = None
        ## case obj is `this`
        if isinstance(ast.obj, SelfLiteral):
            searchedMember = self.searchMemberByName(fieldname)
            if searchedMember is None or not isinstance(searchedMember, memDeclType):
                errorKind = Attribute() if memDeclType == AttributeDecl else Method()
                raise Undeclared(errorKind, fieldname)
        ## case obj is a variable type class
        elif classDecl is None:
            objType = ast.obj.accept(self, visibleScopeDecls).astType
            if not isinstance(objType, ClassType):
                raise IllegalMemberAccess(ast)
            classDeclName = self.getASTName(objType)
            classDecl = self.searchClassByName(classDeclName)
            searchedMember = self.searchMemberOfClassByName(classDecl, fieldname)
            if searchedMember is None or not isinstance(searchedMember, memDeclType):
                errorKind = Attribute() if memDeclType == AttributeDecl else Method()
                raise Undeclared(errorKind, fieldname)
        ## case obj is a class try to access static member
        else:
            searchedMember = self.searchMemberOfClassByName(classDecl, fieldname)
            if searchedMember is None or not isinstance(searchedMember, memDeclType):
                errorKind = Attribute() if memDeclType == AttributeDecl else Method()
                raise Undeclared(errorKind, fieldname)
            if not isinstance(searchedMember.kind, Static):
                raise IllegalMemberAccess(ast)
        return searchedMember

    def visitId(self, ast: Id, visibleScopeDecls: List[Decl]) -> Type:
        searchedDecl = self.searchDeclByName(ast.name, visibleScopeDecls)
        if isinstance(searchedDecl, VarDecl):
            isInitialized = searchedDecl.varInit != None
            return ExprRet(searchedDecl.varType, isInitialized)
        elif isinstance(searchedDecl, ConstDecl):
            return ExprRet(searchedDecl.constType, True)
        elif isinstance(searchedDecl, AttributeDecl):
            storeDecl = searchedDecl.decl
            if isinstance(storeDecl, VarDecl):
                isInitialized = storeDecl.varInit != None
                return ExprRet(storeDecl.varType, isInitialized)
            elif isinstance(storeDecl, ConstDecl):
                return ExprRet(storeDecl.constType, True)
        elif isinstance(searchedDecl, MethodDecl):
            return ExprRet(searchedDecl.returnType)
        elif isinstance(searchedDecl, ClassDecl):
            return ExprRet(ClassType(ast.name))
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self, ast: BinaryOp, visibleScopeDecls: List[Decl]) -> Type:
        leftOperand = ast.left.accept(self, visibleScopeDecls)
        rightOperand = ast.right.accept(self, visibleScopeDecls)
        leftOperandType = leftOperand.astType
        rightOperandType = rightOperand.astType
        isInitialized = leftOperand.isInitialized and rightOperand.isInitialized

        if ast.op in ["+", "-", "*", "/", "\\", "%"]:
            if not (
                (type(leftOperandType) in [IntType, FloatType])
                and (type(rightOperandType) in [IntType, FloatType])
            ):
                raise TypeMismatchInExpression(ast)
            if ast.op == "/":
                return ExprRet(FloatType(), isInitialized)
            elif ast.op in ["\\", "%"]:
                if not (
                    isinstance(leftOperandType, IntType)
                    and isinstance(rightOperandType, IntType)
                ):
                    raise TypeMismatchInExpression(ast)
                return ExprRet(IntType(), isInitialized)
            else:
                if isinstance(leftOperandType, IntType) and isinstance(
                    rightOperandType, IntType
                ):
                    return ExprRet(IntType(), isInitialized)
                else:
                    return ExprRet(FloatType(), isInitialized)
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
            return ExprRet(BoolType(), isInitialized)
        elif ast.op in [">", "<", ">=", "<="]:
            if not (
                (type(leftOperandType) in [IntType, FloatType])
                and (type(rightOperandType) in [IntType, FloatType])
            ):
                raise TypeMismatchInExpression(ast)
            return ExprRet(BoolType(), isInitialized)
        elif ast.op == "^":
            if not (
                isinstance(leftOperandType, StringType)
                and isinstance(rightOperandType, StringType)
            ):
                raise TypeMismatchInExpression(ast)
            return ExprRet(StringType(), isInitialized)

    def visitUnaryOp(self, ast: UnaryOp, visibleScopeDecls: List[Decl]) -> Type:
        return ast.body.accept(self, visibleScopeDecls)

    def visitCallExpr(self, ast: CallExpr, visibleScopeDecls: List[Decl]) -> Type:
        searchedMethodMember = self.visitAccess(ast, visibleScopeDecls, MethodDecl)
        # store all ExprRet of paramdecl in MethodDecl
        paramDecls = []
        isInitialized = True
        for p in searchedMethodMember.param:
            paramExprRet = p.accept(self, paramDecls)
            paramDecls.append(paramExprRet)
        # store all ExprRet of param passed in MethodCall
        paramPassed = []
        for p in ast.param:
            paramExprRet = p.accept(self, visibleScopeDecls)
            paramPassed.append(paramExprRet)
            isInitialized = paramExprRet.isInitialized and isInitialized
        if len(paramDecls) != len(paramPassed):
            raise TypeMismatchInExpression(ast)
        for i in range(0, len(paramDecls)):
            if not self.checkTypeMatch(paramDecls[i].astType, paramPassed[i].astType):
                raise TypeMismatchInExpression(ast)

        astType = self.getDeclType(searchedMethodMember)
        return ExprRet(astType, isInitialized)

    def visitNewExpr(self, ast: NewExpr, visibleScopeDecls: List[Decl]) -> ExprRet:
        name = self.getASTName(ast)
        classDecl = self.searchClassByName(name)
        if classDecl is None:
            raise Undeclared(Class(), name)
        constructor = None
        for decl in self.classScopeMembers:
            if self.getASTName(decl) == "<init>":
                constructor = decl
                break
        if constructor is None:
            raise Undeclared(Method(), "<init>")
        # store all ExprRet of paramdecl in MethodDecl
        paramDecls = []
        for p in constructor.param:
            paramExprRet = p.accept(self, paramDecls)
            paramDecls.append(paramExprRet)
        # store all ExprRet of param passed in MethodCall
        paramPassed = []
        for p in ast.param:
            paramExprRet = p.accept(self, visibleScopeDecls)
            paramPassed.append(paramExprRet)
        if len(paramDecls) != len(paramPassed):
            raise TypeMismatchInExpression(ast)
        for i in range(0, len(paramDecls)):
            if not self.checkTypeMatch(paramDecls[i].astType, paramPassed[i].astType):
                raise TypeMismatchInExpression(ast)
        astType = ClassType(Id(name))
        return ExprRet(astType, True)

    def visitArrayCell(self, ast: ArrayCell, visibleScopeDecls: List[Decl]) -> ExprRet:
        arr = ast.arr.accept(self, visibleScopeDecls)
        idx = ast.idx.accept(self, visibleScopeDecls)
        isInitialized = True
        arrType = arr.astType
        idxType = idx.astType
        isInitialized = isInitialized and arr.isInitialized and idx.isInitialized
        if not isinstance(arrType, ArrayType):
            raise TypeMismatchInExpression(ast)
        if not isinstance(idxType, IntType):
            raise TypeMismatchInExpression(ast)
        return ExprRet(arrType.eleType, isInitialized)

    def visitFieldAccess(
        self, ast: FieldAccess, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
        searchedAttributeMember = self.visitAccess(
            ast, visibleScopeDecls, AttributeDecl
        )
        isInitialized = (
            isinstance(searchedAttributeMember.decl, ConstDecl)
            or searchedAttributeMember.decl.varInit != None
        )
        return ExprRet(self.getDeclType(searchedAttributeMember), isInitialized)

    def visitIntLiteral(
        self, ast: IntLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
        return ExprRet(IntType(), True)

    def visitFloatLiteral(
        self, ast: FloatLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
        return ExprRet(FloatType(), True)

    def visitStringLiteral(
        self, ast: StringLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
        return ExprRet(StringType(), True)

    def visitBooleanLiteral(
        self, ast: BooleanLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
        return ExprRet(BoolType(), True)

    def visitArrayLiteral(self, ast: ArrayLiteral, temp) -> ExprRet:
        eleType = ast.value[0].accept(self, temp).astType
        for v in ast.value:
            vType = v.accept(self, temp).astType
            if not (
                self.checkTypeMatch(vType, eleType)
                and self.checkTypeMatch(eleType, vType)
            ):
                raise IllegalArrayLiteral(ast)
        astType = ArrayType(len(ast.value), eleType)
        return ExprRet(astType, True)

    def visitAssign(self, ast: Assign, visibleScopeDecls) -> None:
        lhs = ast.lhs.accept(self, visibleScopeDecls)
        exp = ast.exp.accept(self, visibleScopeDecls)
        lhsType = lhs.astType
        expType = exp.astType
        if isinstance(ast.lhs, Id):
            lhsName = self.getASTName(ast.lhs)
            decl = self.searchDeclByName(lhsName, visibleScopeDecls)
            if decl is None:
                raise Undeclared(Identifier(), lhsName)
            if self.checkIsConstant(decl):
                raise CannotAssignToConstant(ast)
            self.assignVal(decl, ast.exp)
        elif isinstance(ast.lhs, FieldAccess):
            searchedMember = self.visitAccess(ast.lhs, visibleScopeDecls, AttributeDecl)
            if self.checkIsConstant(searchedMember):
                raise CannotAssignToConstant(ast)
            self.assignVal(searchedMember, ast.exp)
        elif isinstance(ast.lhs, ArrayCell):
            arrName = self.getASTName(ast.lhs)
            memDecl = self.searchDeclByName(arrName, visibleScopeDecls)
            if self.checkIsConstant(memDecl):
                raise CannotAssignToConstant(ast)
            self.assignVal(memDecl, [ast.exp])
        else:
            raise Undeclared(Identifier(), lhsName)

        if not self.checkTypeMatch(lhsType, expType):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast: If, visibleScopeDecls) -> None:
        exprType = ast.expr.accept(self, visibleScopeDecls).astType
        if not isinstance(exprType, BoolType):
            raise TypeMismatchInStatement(ast)
        self.stack_scopeType.append(If)
        ast.thenStmt.accept(self, visibleScopeDecls)
        if ast.elseStmt != None:
            ast.elseStmt.accept(self, visibleScopeDecls)
        self.stack_scopeType.pop()

    def visitFor(self, ast: For, visibleScopeDecls) -> None:
        idType = ast.id.accept(self, visibleScopeDecls).astType
        assignPart = Assign(ast.id, ast.expr1)
        assignPart.accept(self, visibleScopeDecls)
        if not isinstance(idType, IntType):
            raise TypeMismatchInStatement(ast)
        expr1Type = ast.expr1.accept(self, IntType).astType
        if not isinstance(expr1Type, IntType):
            raise TypeMismatchInStatement(ast)
        expr2Type = ast.expr2.accept(self, IntType).astType
        if not isinstance(expr2Type, IntType):
            raise TypeMismatchInStatement(ast)
        self.stack_scopeType.append(For)
        ast.loop.accept(self, visibleScopeDecls)
        self.stack_scopeType.pop()

    def visitBreak(self, ast: Break, visibleScopeDecls) -> None:
        if not self.stack_scopeType[-1] == For:
            raise MustInLoop(ast)

    def visitContinue(self, ast: Continue, visibleScopeDecls) -> None:
        if not self.stack_scopeType[-1] == For:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, visibleScopeDecls) -> None:
        exprType = ast.expr.accept(self, visibleScopeDecls).astType
        curMethodReturnType = self.classScopeMembers[-1].returnType
        if not self.checkTypeMatch(curMethodReturnType, exprType):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast: CallStmt, visibleScopeDecls) -> None:
        searchedMethodMember = self.visitAccess(ast, visibleScopeDecls, MethodDecl)
        if not isinstance(searchedMethodMember.returnType, VoidType):
            raise TypeMismatchInStatement(ast)
        # store all ExprRet of paramdecl in MethodDecl
        paramDecls = []
        for p in searchedMethodMember.param:
            paramExprRet = p.accept(self, paramDecls)
            paramDecls.append(paramExprRet)
        # store all ExprRet of param passed in MethodCall
        paramPassed = []
        for p in ast.param:
            paramExprRet = p.accept(self, visibleScopeDecls)
            paramPassed.append(paramExprRet)
        if len(paramDecls) != len(paramPassed):
            raise TypeMismatchInStatement(ast)
        for i in range(0, len(paramDecls)):
            if not self.checkTypeMatch(paramDecls[i].astType, paramPassed[i].astType):
                raise TypeMismatchInStatement(ast)

    def visitVarDecl(self, ast: VarDecl, visibleScopeDecls) -> ExprRet:
        varType = ast.varType
        varInitExprRet = (
            ast.varInit.accept(self, visibleScopeDecls) if ast.varInit else None
        )
        isInitialized = False
        if varInitExprRet:
            isInitialized = True
            varInitType = varInitExprRet.astType
            if not self.checkTypeMatch(varType, varInitType):
                raise TypeMismatchInStatement(Assign(ast.variable, ast.varInit))
        return ExprRet(varType, isInitialized)

    def visitBlock(self, ast: Block, visibleScopeDecls: List[Decl]) -> None:
        extraVisibleScopeDecls = [*visibleScopeDecls]
        # check Redeclared between decls in Block
        blockScopeDeclNames = []
        for decl in ast.decl:
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

    def visitConstDecl(self, ast: ConstDecl, visibleScopeDecls: List[Decl]) -> ExprRet:
        constType = ast.constType
        valueExprRet = ast.value.accept(self, visibleScopeDecls)
        valueType = valueExprRet.astType

        if not self.checkTypeMatch(constType, valueType):
            raise TypeMismatchInConstant(ast)

        if not valueExprRet.isInitialized:
            raise IllegalConstantExpression(ast.value)

        return ExprRet(constType, True)

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

        self.globalScopeDecls.append(ast)

        # init classScopeDecls
        classScopeDecls = []
        self.classScopeMembers = []
        # check Error in class's members
        classMembers = ast.memlist
        for mem in classMembers:
            if isinstance(mem, MethodDecl):
                self.stack_scopeType.append(MethodDecl)
            self.classScopeMembers.append(mem)
            checkedMember = mem.accept(self, classScopeDecls)
            classScopeDecls.append(checkedMember)
            if isinstance(mem, MethodDecl):
                self.stack_scopeType.pop()
        # if parentname != "":
        #     parentClass = self.searchClassByName(parentname)
        #     classMembers = parentClass.memlist
        #     for mem in classMembers:
        #         memName = self.getASTName(mem)
        #         if self.searchDeclByName(memName):
        #             Continue
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
        print(self.getASTName(ast.decl))
        if attributeName in memDeclNames:
            raise Redeclared(Attribute(), attributeName)

        # check Error in StoreDecl
        ast.decl.accept(self, classScopeDecls)

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

        # init stack to store BlockDeclType
        self.stack_scopeType = []

        # check Error in every classDecl
        classDecls = ast.decl
        for decl in classDecls:
            self.stack_scopeType.append(ClassDecl)
            decl.accept(self, self.globalScopeDecls)
            self.stack_scopeType.pop()
        print("ok in visitProgram")

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)
