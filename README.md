- Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
- Change current directory to initial/src where there is file run.py
- Type: python run.py gen 
- Then type: python run.py test LexerSuite
- Then type: python run.py test ParserSuite
- Then type: python run.py test ASTGenSuite

# CHECK ASSIGNMENT

## visitClassDecl
- check error `Redeclared` the new class
- check error `Undeclared` the parent of new class 

## visitMethodDecl

## visitAttributeDecl

## visitProgram
- add one existed class `io` to the completely new program
