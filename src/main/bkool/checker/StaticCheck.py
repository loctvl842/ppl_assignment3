"""
 * @author nhphung
 * Student's name: Le Tran Phuc Loc
 * Student's ID: 2013684
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from typing import List, Tuple


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

### `checkClassExist` function used to check if class exist or not
## @param classname name of the class to check (type: str)
## @param prog the prog contain the class to check
## @return True/False
    def checkClassExist(self, classname: str, prog):
        if classname == "":
            return False
        for index, classDecl in enumerate(prog.decl):
            if classDecl.classname.accept(self, "id") == classname:
                return True
        return False

### `checkMemberExist` function used to check if member (can be attribute or method) exist within a class
## @param targetMem name of member need to check (type: MemDecl)
## @param memlist list of members need to check (type: List[MemDecl])
## @return True/False
    def checkMemberExist(self, targetMem: MemDecl, memlist: List[MemDecl]):
        def getMemberName(member):
            if isinstance(member, AttributeDecl):
                return member.decl.variable.accept(self, "id")
            elif isinstance(member, MethodDecl):
                return member.name

        for member in memlist:
            if getMemberName(targetMem) == getMemberName(member):
                return True
        return False

### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
## @param targetChildName is the child's name need to check (type: str)
## @param targetParentName is the parent's name need to check (type: str)
## @return True/False
    def checkIsKidOf(self, targetChildName: str, targetParentName: str):
        def searchClass(classname):
            for index, classDecl in enumerate(self.program.decl):
                if classDecl.classname.accept(self, "id") == classname:
                    return classDecl
            return None

        searchedChildClass = searchClass(targetChildName)
        if searchedChildClass == None:
            raise Undeclared(Class(), targetChildName)
        else:
            if searchedChildClass.parentname == None:
                return False
            parentOfTargetChild = searchedChildClass.parentname.accept(self, "id")
            if parentOfTargetChild == targetParentName:
                return True
            else:
                return self.checkIsKidOf(parentOfTargetChild, targetParentName)

    def visitId(self, ast: Id, temp):
        return ast.name

    def visitBinaryOp(self, ast: BinaryOp, temp):
        leftOperandType = ast.left.accept(self, "Expr")
        rightOperandType = ast.right.accept(self, "Expr")
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

    def visitUnaryOp(self, ast: UnaryOp, temp):
        return ast.body.accept(self, "Expr")

    def visitIntLiteral(self, ast: IntLiteral, temp):
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, temp):
        return FloatType()

    def visitStringLiteral(self, ast: StringLiteral, temp):
        return StringType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, temp):
        return BoolType()

    def visitVarDecl(self, ast: VarDecl, members: List[MemDecl]):
        variable = ast.variable.accept(self, "id")
        varType = ast.varType
        varInit = ast.varInit.accept(self, "expr") if ast.varInit else None

        # if checkMemberExist()

        varDecl = VarDecl(Id(variable), varType)

        if varInit:
            if type(varType) != type(varInit):
                if not (
                    isinstance(varType, FloatType) and isinstance(varInit, IntType)
                ):
                    raise TypeMismatchInStatement(Assign(Id(variable), ast.varInit))
            else:
                if isinstance(varType, ClassType) and isinstance(varInit, ClassType):
                    varTypeClassName = varType.classname.accept(self, "id")
                    varInitClassName = varInit.classname.accept(self, "id")
                    if not self.checkIsKidOf(varInitClassName, varTypeClassName):
                        raise TypeMismatchInStatement(Assign(Id(variable), ast.varInit))

            varDecl.varInit = varInit

        return varDecl

    def visitConstDecl(self, ast: ConstDecl, members: List[MemDecl]):
        constant = ast.constant.accept(self, "id")
        constType = ast.constType
        value = ast.value.accept(self, "expr")

        if type(constType) != type(value):
            if not (isinstance(constType, FloatType) and isinstance(value, IntType)):
                raise TypeMismatchInConstant(ast)
        else:
            if isinstance(constType, ClassType) and isinstance(value, ClassType):
                constTypeClassName = constType.classname.accept(self, "id")
                valueClassName = value.classname.accept(self, "id")
                if not self.checkIsKidOf(valueClassName, constTypeClassName):
                    raise TypeMismatchInConstant(ast)

        print("ok")
        return ast

    def visitClassDecl(self, ast: ClassDecl, prog: Program):
        classname = ast.classname.accept(self, "id")
        parentname = ast.parentname.accept(self, "id") if ast.parentname else None

        classDecl = ClassDecl(Id(classname), [])

        if self.checkClassExist(classname, prog):
            raise Redeclared(Class(), classname)
        if parentname != None:
            if not self.checkClassExist(parentname, prog):
                raise Undeclared(Class(), parentname)
            else:
                classDecl.parentname = Id(parentname)

        for mem in ast.memlist:
            classDecl.memlist.append(mem.accept(self, classDecl))

        return classDecl

    def visitMethodDecl(self, ast: MethodDecl, classDecl: ClassDecl):
        pass

    def visitAttributeDecl(self, ast: AttributeDecl, classDecl: ClassDecl):
        kind = ast.kind
        decl: StoreDecl = ast.decl.accept(self, classDecl.memlist)
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
            self.program.decl.append(classDecl.accept(self, self.program))

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)
