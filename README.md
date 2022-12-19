## 🚀 Usage
Go to `src` directory and run the following commands
```python
python run.py gen
python run.py test CheckerSuite
```

## This assignment include two main parts:
- ### [Support Methods](#support-methods-2)
- ### [Static Checker](#static-checker-2)

# Support Methods

### getASTName()
```python
    ### `getASTName` function used to get name of AST object
    ## @param targetObj can be type of AttributeDecl, MethodDecl, VarDecl, ConstDecl, ClassDecl, FieldAccess, ArrayCell, CallExpr, ClassType
    def getASTName(self, targetObj) -> str:
```

### searchClassByName()
```python
    ### `searchClass` function used to find existed class
    def searchClassByName(self, name: str) -> ClassDecl:
```

### getMemDeclType()
```python
    ### `getMemDeclType` function used to get Type of AST member of class
    def getMemDeclType(self, memDecl: MemDecl) -> Type:
```

### searchMemberOfClassByName()
```python
    ### `searchMemberOfClassByName` search a member of other class in global scope
    def searchMemberOfClassByName(self, classDecl: ClassDecl, targetMemberName: str) -> MemDecl:
```

### searchMemberByName()
```python
    ### `searchMemberByName` search a member of current checking class
    def searchMemberByName(self, targetMemberName: str) -> MemDecl:
```

### searchDeclByName()
```python
    ### `searchVarDecl` function used to search a Decl through name
    def searchDeclByName(self, targetname: str, visibleScopeDecls: List[Decl]) -> StoreDecl:
```

### checkIsKidOf()
```python
    ### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
    def checkIsKidOf(self, targetChildName: str, targetParentName: str) -> bool:
```

### checkTypeMatch()
```python
    ### `checkTypeMatch` function used to check if rhs has the same type to lhs or can be con be coerce to lhs
    def checkTypeMatch(self, lhsType: Type, rhsType: Type) -> bool:
```

# Static Checker

### visitAccess
```python
    ## @param memDeclType MethodDecl | AttributeDecl
    def visitAccess(self, ast, visibleScopeDecls: List[Decl], memDeclType) -> StoreDecl:
```
> this function is used by visitFieldAccess, visitCallExpr, visitCallStmt, visitAssign

> this function return the member searched
- check error `Undeclared(errorKind, fieldname)`, `IllegalMemberAccess(ast)`

### visitId
```python
    def visitId(self, ast: Id, visibleScopeDecls: List[Decl]) -> Type:
```

- check error `Undeclared(Identifier(), ast.name)` (this function only check this type of error because the `id` checked here is the `id` used in `expr`; `id` like `classname` or `methodname` have to be checked in its own function for example: `visitClassDecl`, `visitMethodDecl`, ... )

### visitBinaryOp
```python
    def visitBinaryOp(self, ast: BinaryOp, visibleScopeDecls: List[Decl]) -> Type:
```
- check error `TypeMisMatch(ast)`

### visitUnaryOp
```python
    def visitUnaryOp(self, ast: UnaryOp, visibleScopeDecls: List[Decl]) -> Type:
```

### visitCallExpr
```python
    def visitCallExpr(self, ast: CallExpr, visibleScopeDecls: List[Decl]) -> Type:
```
- check error in visitAccess(), `TypeMismatchInExpression(ast)`

### visitNewExpr
```python
    def visitNewExpr(self, ast: NewExpr, visibleScopeDecls: List[Decl]) -> ExprRet:
```
- check error `Undeclared(Class(), name)`, `Undeclared(Method(), "<init>")`, `TypeMismatchInExpression(ast)` 

### visitArrayCell
```python
    def visitArrayCell(self, ast: ArrayCell, visibleScopeDecls: List[Decl]) -> ExprRet:
```
- check error `TypeMismatchInExpression(ast)`

### visitFieldAccess
```python
    def visitFieldAccess(self, ast: FieldAccess, visibleScopeDecls: List[Decl]) -> ExprRet:
```
- check error in `visitAccess()`

### visitIntLiteral()
```python
    def visitIntLiteral(
        self, ast: IntLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
```

### visitFloatLiteral()
```python
    def visitFloatLiteral(
        self, ast: FloatLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
```

### visitStringLiteral()
```python
    def visitStringLiteral(
        self, ast: StringLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
```

### visitBoolLiteral()
```python
    def visitBooleanLiteral(
        self, ast: BooleanLiteral, visibleScopeDecls: List[Decl]
    ) -> ExprRet:
```

### visitArrayLiteral
```python
    def visitArrayLiteral(self, ast: ArrayLiteral, temp) -> ExprRet:
```
- check error `IllegalArrayLiteral(ast)`

### visitAssign
```python
    def visitAssign(self, ast: Assign, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `Undeclared(Identifier(), lhsName)`
- check error `TypeMismatchInStatement(assignStmt)`
- check error `CannotAssignToConstant(assignStmt)` (check if lhs is connstant)

### visitIf
```python
    def visitIf(self, ast: If, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `TypeMismatchInStatement(ast)`

### visitFor
```python
    def visitFor(self, ast: For, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `TypeMismatchInStatement(ast)`

### visitBreak
```python
    def visitBreak(self, ast: Break, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `MustInLoop(ast)`

### visitContinue
```python
    def visitContinue(self, ast: Continue, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `MustInLoop(ast)`

### visitReturn()
```python
    def visitReturn(self, ast :Return, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `TypeMismatchInStatement(ast)`

### visitCallStmt()
```python
    def visitCallStmt(self, ast: CallStmt, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error in `visitAccess` and `TypeMismatchInStatement(ast)`

### visitVarDecl
```python
    def visitVarDecl(self, ast: VarDecl, visibleScopeDecls: list[StoreDecl]) -> ExprRet:
```
- check error `TypeMismatchInStatement(Assign(ast.variable, ast.varInit))`

### visitBlock
```python
    def visitBlock(self, ast: Block, visibleScopeDecls: List[Decl]) -> None:
```
- check error `Redeclared(errorKind, declName)` (only check between declares in block)

### visitConstDecl
```python
    def visitConstDecl(self, ast: ConstDecl, visibleScopeDecls: List[Decl]) -> ExprRet:
```
- check error `TypeMismatchInConstant(ast)`, `IllegalConstantExpression(ast.value)`

### visitClassDecl
```python
    def visitClassDecl(self, ast: ClassDecl, globalScopeDecls: List[Decl]) -> ClassDecl:
```
- check error `Redeclared(Class(), classname)` the new class
- check error `Undeclared(Class(), parentname)` the parent of new class

### visitMethodDecl
```python
    def visitMethodDecl(self, ast: MethodDecl, classScopeDecls: List[Decl]) -> MethodDecl:
```
- check error `Redeclared(Method(), methodName)` of the new method
- check error `Redeclared(Parameter(),paramName)` in list of params
- check error `Redeclared(StoreDecl, name)` in list of decls of `Block` (only if `StoreDecl` exist in list of `parameters`)

### visitAttributeDecl
```python
    def visitAttributeDecl(self, ast: AttributeDecl, classScopeDecls: List[MemDecl]) -> AttributeDecl:
```
- check error `Redeclared(Attribute(), attributeName)`

### visitProgram
```python
    def visitProgram(self, ast: Program, c) -> None:
```
- add one existed class `io` to the completely new program
- create `globalScopeDecls` store in global
