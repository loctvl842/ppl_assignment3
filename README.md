- Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
- Change current directory to initial/src where there is file run.py
- Type: python run.py gen
- Then type: python run.py test LexerSuite
- Then type: python run.py test ParserSuite
- Then type: python run.py test ASTGenSuite

# SUPPORT METHODS

## getASTName()
```python
    ### `getASTName` function used to get name of AST object
    ## @param targetObj can be type of AttributeDecl, MethodDecl, VarDecl, ConstDecl, ClassDecl, FieldAccess, ArrayCell, CallExpr, ClassType
    def getASTName(self, targetObj) -> str:
```

## searchClassByName()
```python
    ### `searchClass` function used to find existed class
    def searchClassByName(self, name: str) -> ClassDecl:
```

## getMemDeclType()
```python
    ### `getMemDeclType` function used to get Type of AST member of class
    def getMemDeclType(self, memDecl: MemDecl) -> Type:
```

## searchMemberOfClassByName()
```python
    ### `searchMemberOfClassByName` search a member of other class in global scope
    def searchMemberOfClassByName(self, classDecl: ClassDecl, targetMemberName: str) -> MemDecl:
```

## searchMemberByName()
```python
    ### `searchMemberByName` search a member of current checking class
    def searchMemberByName(self, targetMemberName: str) -> MemDecl:
```

## searchDeclByName()
```python
    ### `searchVarDecl` function used to search a Decl through name
    def searchDeclByName(self, targetname: str, visibleScopeDecls: List[Decl]) -> StoreDecl:
```

## checkIsKidOf()
```python
    ### `checkIsKidOf` function used to check if an object is a child of another by query bottom down
    def checkIsKidOf(self, targetChildName: str, targetParentName: str) -> bool:
```

## checkTypeMatch()
```python
    ### `checkTypeMatch` function used to check if rhs has the same type to lhs or can be con be coerce to lhs
    def checkTypeMatch(self, lhsType: Type, rhsType: Type) -> bool:
```

# CHECK ASSIGNMENT

```python
    def visitId(self, ast: Id, visibleScopeDecls: List[Decl]) -> Type:
```

- check error `Undeclared(Identifier(), ast.name)` (this function only check this type of error because the `id` checked here is the `id` used in `expr`; `id` like `classname` or `methodname` have to be checked in its own function for example: `visitClassDecl`, `visitMethodDecl`, ... )

## visitBinaryOp
```python
    def visitBinaryOp(self, ast: BinaryOp, visibleScopeDecls: List[Decl]) -> Type:
```
- check error `TypeMisMatch(ast)`

## visitUnaryOp
```python
    def visitUnaryOp(self, ast: UnaryOp, visibleScopeDecls: List[Decl]) -> Type:
```

## visitCallExpr
```python
    def visitCallExpr(self, ast: CallExpr, visibleScopeDecls: List[Decl]) -> Type:
```
- check error `Undeclared(Method(), methodName)`, `TypeMismatchInExpression(ast)`, `IllegalMemberAccess(ast)`

## visitNewExpr

## visitArrayCell

## visitFieldAccess
```python
    def visitFieldAccess(self, ast: FieldAccess, visibleScopeDecls: List[Decl]) -> Type:
```
- check error `Undeclared(Attribute(), fieldname)`, `IllegalMemberAccess(ast)`

## visitIntLiteral()
```python
    def visitIntLiteral(self, ast: IntLiteral, visibleScopeDecls: List[Decl]) -> IntType:
```

## visitFloatLiteral()
```python
    def visitFloatLiteral(self, ast: FloatLiteral, visibleScopeDecls: List[Decl]):
```

## visitStringLiteral()
```python
    def visitStringLiteral(self, ast: StringLiteral, visibleScopeDecls: List[Decl]) -> StringType:
```

## visitBoolLiteral()
```python
    def visitBooleanLiteral(self, ast: BooleanLiteral, visibleScopeDecls: List[Decl]) -> BoolType:
```

## visitArrayLiteral
```python
    def visitArrayLiteral(self, ast: ArrayLiteral, temp) -> ArrayType:
```
- check error `IllegalArrayLiteral(ast)`

## visitAssign
```python
    def visitAssign(self, ast: Assign, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `TypeMismatchInStatement(assignStmt)`
- check error `CannotAssignToConstant(assignStmt)` (check if lhs is connstant)

## visitReturn()
```python
    def visitReturn(self, ast :Return, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `TypeMismatchInStatement(ast)`

## visitCallStmt()
```python
    def visitCallStmt(self, ast: CallStmt, visibleScopeDecls: List[StoreDecl]) -> None:
```
- check error `Undeclared(Method(), methodName)`, `TypeMismatchInStatement(ast)`, `IllegalMemberAccess(ast)`

## visitVarDecl
```python
    def visitVarDecl(self, ast: VarDecl, visibleScopeDecls: list[StoreDecl]) -> Type:
```
- check error `TypeMismatchInStatement(Assign(ast.variable, ast.varInit))`

## visitBlock
```python
    def visitBlock(self, ast: Block, visibleScopeDecls: List[Decl]) -> None:
```
- check error `Redeclared(errorKind, declName)` (only check between declares in block)

## visitConstDecl
```python
    def visitConstDecl(self, ast: ConstDecl, visibleScopeDecls: List[Decl]) -> Type:
```
- check error `TypeMismatchInConstant(ast)`

## visitClassDecl
```python
    def visitClassDecl(self, ast: ClassDecl, globalScopeDecls: List[Decl]) -> ClassDecl:
```
- check error `Redeclared(Class(), classname)` the new class
- check error `Undeclared(Class(), parentname)` the parent of new class

## visitMethodDecl
```python
    def visitMethodDecl(self, ast: MethodDecl, classScopeDecls: List[Decl]) -> MethodDecl:
```
- check error `Redeclared(Method(), methodName)` of the new method
- check error `Redeclared(Parameter(),paramName)` in list of params
- check error `Redeclared(StoreDecl, name)` in list of decls of `Block` (only if `StoreDecl` exist in list of `parameters`)

## visitAttributeDecl
```python
    def visitAttributeDecl(self, ast: AttributeDecl, classScopeDecls: List[MemDecl]) -> AttributeDecl:
```
- check error `Redeclared(Attribute(), attributeName)`

## visitProgram
```python
    def visitProgram(self, ast: Program, c) -> None:
```
- add one existed class `io` to the completely new program
- create `globalScopeDecls`
