"""
 * @author nhphung
 * Student's name: Le Tran Phuc Loc
 * Student's ID: 2013684
"""
from array import ArrayType
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


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
    def getASTName(self, targetObj):
        if isinstance(targetObj, AttributeDecl):
            return self.getASTName(targetObj.decl)
        elif isinstance(targetObj, MethodDecl):
            return targetObj.name.name
        elif isinstance(targetObj, VarDecl):
            return targetObj.variable.name
        elif isinstance(targetObj, ConstDecl):
            return targetObj.constant.name

    ### `checkClassExist` function used to check if class exist or not
    ## @param classname name of the class to check (type: str)
    ## @param classDecls list of class existed
    ## @return True/False
    def checkClassExist(self, classname: str, classDecls: List[ClassDecl]):
        if classname == "":
            return False
        for classDecl in classDecls:
            if classDecl.classname.name == classname:
                return True
        return False

    ### `checkMemberExist` function used to check if member (can be attribute or method) exist within a class
    ## @param targetMem name of member need to check (type: MemDecl)
    ## @param memlist list of members need to check (type: List[MemDecl])
    ## @return True/False
    def checkMemberExist(self, targetMem: MemDecl, members: List[MemDecl]):
        targetMemName = self.getASTName(targetMem)
        for m in members:
            if targetMemName == self.getASTName(m):
                return True
        return False

    ### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
    ## @param targetChildName is the child's name need to check (type: str)
    ## @param targetParentName is the parent's name need to check (type: str)
    ## @return True/False
    def checkIsKidOf(self, targetChildName: str, targetParentName: str):
        searchedChildClass = self.searchClass(targetChildName)
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
    def searchClass(self, classname: str):
        for classDecl in self.program.decl:
            if classDecl.classname.name == classname:
                return classDecl
        return None

    ### `searchVarDecl` function used to search a varDecl through name
    ## @param targetname name to search
    ## @param varDecls is list of varDecl that may contain varDecl with targetname
    ## @return VarDecl
    def searchVarDecl(self, targetname: str, varDecls: List[VarDecl]):
        for varDecl in varDecls:
            if self.getASTName(varDecl) == targetname:
                return varDecl

        return None

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

    def visitId(self, ast: Id, varDecls: List[VarDecl]):
        searchedDecl = self.searchVarDecl(ast.name, varDecls)
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
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitBinaryOp(self, ast: BinaryOp, varDecls: List[VarDecl]):
        leftOperandType = ast.left.accept(self, varDecls)
        rightOperandType = ast.right.accept(self, varDecls)

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

    def visitUnaryOp(self, ast: UnaryOp, varDecls: List[VarDecl]):
        return ast.body.accept(self, varDecls)

    def visitIntLiteral(self, ast: IntLiteral, temp):
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, temp):
        return FloatType()

    def visitStringLiteral(self, ast: StringLiteral, temp):
        return StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, temp):
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
        pass

    def visitVarDecl(self, ast: VarDecl, decls: List):
        variable = ast.variable.name
        varType = ast.varType
        varInit = ast.varInit.accept(self, decls) if ast.varInit else None

        if len(decls) > 0 and isinstance(decls[0], StoreDecl):
            if self.checkStoreExist(variable, decls):
                raise Redeclared(Variable(), variable)

        varDecl = VarDecl(Id(variable), varType)

        if varInit:
            if not self.checkTypeMatch(varType, varInit):
                raise TypeMismatchInStatement(Assign(Id(variable), ast.varInit))
            varDecl.varInit = varInit

        return varDecl

    def visitBlock(self, ast: Block, decls: List[StoreDecl]):
        # check Redeclared between decls in Block
        blockDeclNames = []
        blockDecls = ast.decl
        for decl in blockDecls:
            declName = self.getASTName(decl)
            if declName in blockDeclNames:
                if isinstance(decl, ConstDecl):
                    raise Redeclared(Constant(), declName)
                else:
                    raise Redeclared(Variable(), declName)
            blockDeclNames.append(declName)
            decls.append(decl)

        # check statements
        blockStmts = ast.stmt
        for stmt in blockStmts:
            stmt.accept(self, decls)

        return ast

    def visitConstDecl(self, ast: ConstDecl, decls: List):
        constant = ast.constant.name
        constType = ast.constType
        value = ast.value.accept(self, decls)

        if len(decls) > 0 and isinstance(decls[0], StoreDecl):
            if self.checkStoreExist(constant, decls):
                raise Redeclared(Constant(), constant)
        if not self.checkTypeMatch(constType, value):
            raise TypeMismatchInConstant(ast)

        return ast

    def visitClassDecl(self, ast: ClassDecl, classDecls: List[ClassDecl]):
        classname = ast.classname.name
        parentname = ast.parentname.name if ast.parentname else None

        classDecl = ClassDecl(Id(classname), [])

        if self.checkClassExist(classname, classDecls):
            raise Redeclared(Class(), classname)
        if parentname != None:
            if not self.checkClassExist(parentname, classDecls):
                raise Undeclared(Class(), parentname)
            else:
                classDecl.parentname = Id(parentname)

        for mem in ast.memlist:
            checkedMember = mem.accept(self, classDecl.memlist)
            classDecl.memlist.append(checkedMember)

        print("ok in visitClassDecl")
        return classDecl

    def visitMethodDecl(self, ast: MethodDecl, memlist: List[MemDecl]):
        if self.checkMemberExist(ast, memlist):
            raise Redeclared(Method(), self.getASTName(ast))

        paramNames = []
        decls = []
        for p in ast.param:
            pName = self.getASTName(p)
            if pName in paramNames:
                raise Redeclared(Parameter(), pName)
            paramNames.append(pName)
            decls.append(p)

        blockDecls = ast.body.decl
        for decl in blockDecls:
            declName = self.getASTName(decl)
            if declName in paramNames:
                if isinstance(decl, VarDecl):
                    raise Redeclared(Variable(), declName)
                else:
                    raise Redeclared(Constant(), declName)

        ast.body.accept(self, decls)
        return ast

    def visitAttributeDecl(self, ast: AttributeDecl, memlist: List[MemDecl]):
        if self.checkMemberExist(ast, memlist):
            raise Redeclared(Attribute(), self.getASTName(ast))

        kind = ast.kind
        decl: StoreDecl = ast.decl.accept(self, memlist)
        attributeDecl = AttributeDecl(kind, decl)
        return attributeDecl

    def visitProgram(self, ast: Program, c):
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
        self.program = Program([ClassDecl(Id("io"), ioMembers)])
        for classDecl in ast.decl:
            checkedClassDecl = classDecl.accept(self, self.program.decl)
            self.program.decl.append(checkedClassDecl)

        print("ok in visitProgram")

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)
