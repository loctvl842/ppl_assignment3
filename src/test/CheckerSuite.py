import unittest
from TestUtils import TestChecker
from AST import *
from StaticError import *

from main.bkool.utils.AST import *


class CheckerSuite(unittest.TestCase):
    # def test_1(self):
    #     input = "class io extends TestParent {}"
    #     expect = "Redeclared Class: io"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    # def test_2(self):
    #     input = "class Test extends TestParent {}"
    #     expect = "Undeclared Class: TestParent"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_3(self):
    #     input = """
    #     class Ex
    #     {
    #         int my1Var = 2 + 3;
    #         static float my1Var;
    #         int a() {}
    #     }"""
    #     expect = "Redeclared Attribute: my1Var"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_4(self):
    #     """If Expr: return `ClassType(C)`"""
    #     input = """
    #     class A {}
    #     class B extends A {}
    #     class C {
    #         A v;
    #         B x = v + v;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(v),Id(v))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_5(self):
    #     """If Expr: return `FloatType()`"""
    #     input = """
    #     class C {
    #         int a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_6(self):
    #     """If Expr: return `FloatType()` (check if not the same type)"""
    #     input = """
    #     class C {
    #         string a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_7(self):
    #     """If Expr: return `FloatType()` (check if not the same type)"""
    #     input = """
    #     class C {
    #         final string a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),StringType,BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_8(self):
    #     """If Expr: return `FloatType()` (check if not the same type) [conerce error only int assign to float]"""
    #     input = """
    #     class C {
    #         final int a = 2.0 + 3;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,BinaryOp(+,FloatLit(2.0),IntLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_9(self):
    #     input = """
    #     class C {
    #         final float a = 2.0 \\ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(\\,FloatLit(2.0),StringLit(loc))"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_10(self):
    #     input = """
    #     class C {
    #         final float a = 2.0 ^ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(^,FloatLit(2.0),StringLit(loc))"
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_11(self):
    #     input = """
    #     class C {
    #         final float a = 2.0 ^ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(^,FloatLit(2.0),StringLit(loc))"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_12(self):
    #     input = """
    #     class C {
    #         final float a = "van" ^ "loc";
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),FloatType,BinaryOp(^,StringLit(van),StringLit(loc)))"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test_13(self):
    #     input = """
    #     class C {
    #         string x;
    #         float x;
    #     }
    #     """
    #     expect = "Redeclared Attribute: x"
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    # def test_14(self):
    #     input = """
    #     class C {
    #         string x;
    #         float x;
    #     }
    #     """
    #     expect = "Redeclared Attribute: x"
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test_15(self):
    #     input = """
    #     class C {
    #         string a;
    #         float x = a + 2;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 414))

    # def test_16(self):
    #     input = """
    #     class C {
    #         int a;
    #         float b;
    #         string c;
    #         final float x = c;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),FloatType,Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 415))

    # def test_17(self):
    #     input = """
    #     class C {
    #         string d;
    #         final float x = c;
    #     }
    #     """
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input, expect, 416))

    # def test_18(self):
    #     input = """
    #     class C {
    #         float c;
    #         int c() {}
    #     }
    #     """
    #     expect = "Redeclared Method: c"
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test_19(self):
    #     input = """
    #     class C {
    #         int a(int a; int b; float d; string e; bool f; string a) {}
    #     }
    #     """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # def test_20(self):
    #     input = """
    #     class C {
    #         int a(int a; int b; float d) {
    #             int a;
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    # def test_21(self):
    #     input = """
    #     class C {
    #         int a(int a; int b; float d) {
    #             final int b = 2;
    #         }
    #     }
    #     """
    #     expect = "Redeclared Constant: b"
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test_22(self):
    #     input = """
    #     class C {
    #         int a(int a; int b; float d) {
    #             final int c = 2;
    #             string c;
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: c"
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test_23(self):
    #     input = """
    #     class C {
    #         final int a = {1, 2, 3};
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,[IntLit(1),IntLit(2),IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 422))

    # def test_24(self):
    #     input = """
    #     class C {
    #         final float[2] a = {1, 2, 3};
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(2,FloatType),[IntLit(1),IntLit(2),IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    # def test_25(self):
    #     input = """
    #     class C {
    #         float[2] a = {1, 2, 3};
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test_26(self):
    #     input = """
    #     class C {
    #         final float[3] a = {2.3, 4, 102e3};
    #     }
    #     """
    #     expect = "Illegal Array Literal: [FloatLit(2.3),IntLit(4),FloatLit(102e3)]"
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test_27(self):
    #     input = """
    #     class C {
    #         final float[3] a = {2.3, 102e3};
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(3,FloatType),[FloatLit(2.3),FloatLit(102e3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 426))
