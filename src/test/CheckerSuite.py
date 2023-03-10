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

    # def test_28(self):
    #     input = """
    #     class C {
    #         int a;
    #     }
    #     class B {
    #         C x;
    #         int y;
    #         int z = x.a + y.a;
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(y),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 427))

    # def test_29(self):
    #     input = """
    #     class C {
    #         int a;
    #     }
    #     class B {
    #         int z = C.a;
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(C),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    # def test_30(self):
    #     input = """
    #     class C {
    #         static float a;
    #     }
    #     class B {
    #         final int z = C.a;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(z),IntType,FieldAccess(Id(C),Id(a)))"
    #     self.assertTrue(TestChecker.test(input, expect, 429))

    # def test_31(self):
    #     input = """
    #     class C {
    #         static float a;
    #     }
    #     class B {
    #         C x;
    #         int y;
    #         final int z = y.a;
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(y),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test_32(self):
    #     input = """
    #     class C {
    #         static float a;
    #     }
    #     class B {
    #         C x;
    #         final int z = x.a;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(z),IntType,FieldAccess(Id(x),Id(a)))"
    #     self.assertTrue(TestChecker.test(input, expect, 431))

    # def test_33(self):
    #     input = """
    #     class B {
    #         float d;
    #         final int z = this.d;
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(z),IntType,FieldAccess(Self(),Id(d)))"
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test_34(self):
    #     input = """
    #     class B {
    #         float d() {}
    #         final int z = this.d;
    #     }
    #     """
    #     expect = "Undeclared Attribute: d"
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test_35(self):
    #     input = """
    #     class B {
    #         float d() {}
    #         final int z = this.z();
    #     }
    #     """
    #     expect = "Undeclared Method: z"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test_36(self):
    #     input = """
    #     class B {
    #         float d() {}
    #         final int z = this.d();
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(z),IntType,CallExpr(Self(),Id(d),[]))"
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # def test_37(self):
    #     input = """
    #     class B {
    #         void d() {}
    #         final int z = this.d(a, b);
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test_38(self):
    #     input = """
    #     class B {
    #         float d(int x; int y) {}
    #         int x;
    #         final int z = this.d(x);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Self(),Id(d),[Id(x)])"
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test_39(self):
    #     input = """
    #     class B {
    #         float d(int x; int y) {}
    #         int x;
    #         final int z = this.d(x, x);
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(z),IntType,CallExpr(Self(),Id(d),[Id(x),Id(x)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    # def test_40(self):
    #     input = """
    #     class B {
    #         float d(int x; int y) {}
    #         float x;
    #         final int z = this.d(x, x);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Self(),Id(d),[Id(x),Id(x)])"
    #     self.assertTrue(TestChecker.test(input, expect, 439))

    # def test_41(self):
    #     input = """
    #     class A {
    #         float d(int x; int y) {}
    #     }
    #     class B {
    #         A x;
    #         final int z = x.d();
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(x),Id(d),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test_42(self):
    #     input = """
    #     class A {
    #         float d(int x; int y) {}
    #     }
    #     class B {
    #         A x;
    #         final int z = A.d();
    #     }
    #     """
    #     expect = "Illegal Member Access: CallExpr(Id(A),Id(d),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test_43(self):
    #     input = """
    #     class A {
    #         static float d(int x; int y) {}
    #     }
    #     class B {
    #         A x;
    #         final int z = A.d();
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(A),Id(d),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 442))

    # def test_44(self):
    #     input = """
    #     class A {
    #         static float d(int x; int y) {}
    #     }
    #     class B {
    #         int x;
    #         final int z = A.d(x, x);
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(z),IntType,CallExpr(Id(A),Id(d),[Id(x),Id(x)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 443))

    # def test_45(self):
    #     input = """
    #     class A {
    #         static float d(int x; int y) {}
    #     }
    #     class B {
    #         int x;
    #         final int z = A.d(x);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(A),Id(d),[Id(x)])"
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # def test_46(self):
    #     input = """
    #     class A {
    #         static float d(int x; int y) {}
    #     }
    #     class B {
    #         float x;
    #         final int z = A.d(x);
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(A),Id(d),[Id(x)])"
    #     self.assertTrue(TestChecker.test(input, expect, 445))

    # def test_47(self):
    #     input = """
    #     class A {
    #         static float d(float x) {}
    #     }
    #     class B {
    #         float x;
    #         final int z = A.d(x);
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(z),IntType,CallExpr(Id(A),Id(d),[Id(x)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 446))

    # def test_48(self):
    #     input = """
    #     class B {
    #         int sum(int a; int b) {}
    #         int foo() {
    #             A.sum();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: A"
    #     self.assertTrue(TestChecker.test(input, expect, 447))

    # def test_49(self):
    #     input = """
    #     class A {
    #         static int sum(int a; int b) {}
    #     }
    #     class B {
    #         int sum(int a; int b) {}
    #         int foo() {
    #             A.sum();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(A),Id(sum),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 448))

    # def test_50(self):
    #     input = """
    #     class A {
    #         static int sum(int a; int b) {}
    #     }
    #     class B {
    #         int sum(int a; int b) {}
    #         int foo() {
    #             this.sum();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(sum),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 449))

    # def test_51(self):
    #     input = """
    #     class A {
    #         static int sum(int a; int b) {}
    #     }
    #     class B {
    #         int sum(int a; int b) {}
    #         int foo() {
    #             this.sum(2, 2.3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(sum),[IntLit(2),FloatLit(2.3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 450))

    # def test_52(self):
    #     input = """
    #     class A {
    #         static int sum(int a; int b) {}
    #     }
    #     class B {
    #         int sum(int a; int b) {}
    #         int foo() {
    #             return 2.3;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Return(FloatLit(2.3))"
    #     self.assertTrue(TestChecker.test(input, expect, 451))

    # def test_53(self):
    #     input = """
    #     class A {
    #         static int sum(int a; int b) {}
    #     }
    #     class B {
    #         int sum(int a; int b) {}
    #         int foo() {
    #             float i;
    #             for i := 1 to 100 do {
    #                 io.writeIntLn(i);
    #                 Intarray[i] := i + 1;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(100),True,Block([],[Call(Id(io),Id(writeIntLn),[Id(i)]),AssignStmt(ArrayCell(Id(Intarray),Id(i)),BinaryOp(+,Id(i),IntLit(1)))])])"
    #     self.assertTrue(TestChecker.test(input, expect, 452))

    # def test_54(self):
    #     input = """
    #     class B {
    #         int foo() {
    #             io.writntLn(i);
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: writntLn"
    #     self.assertTrue(TestChecker.test(input, expect, 453))

    # def test_55(self):
    #     input = """
    #     class B {
    #         int foo() {
    #             int i;
    #             for i := 1 to 100 do {
    #                 io.writeStrLn(i);
    #             }
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(io),Id(writeStrLn),[Id(i)])"
    #     self.assertTrue(TestChecker.test(input, expect, 454))

    # def test_56(self):
    #     input = """
    #     class B {
    #         int foo() {
    #             int i;
    #             for i := 1 to 100 do {
    #                 int a = 2;
    #                 int b = 2;
    #             }
    #             int c = a + b;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 455))

    # def test_57(self):
    #     input = """
    #     class B {
    #         int foo() {
    #             int i;
    #             for i := 1 to 100 do {
    #                 int a = 2;
    #                 int b = 2;
    #             }
    #             c := a + b;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input, expect, 456))

    # def test_58(self):
    #     input = """
    #     class B {
    #         int foo() {
    #             int c = 2;
    #             c := 2.3;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(c),FloatLit(2.3))"
    #     self.assertTrue(TestChecker.test(input, expect, 457))

    # def test_59(self):
    #     input = """
    #     class B {
    #         int foo() {
    #             int i;
    #             for i := 1.2 to 100 do {
    #                 int a = 2;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(i),FloatLit(1.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 458))

    # def test_59(self):
    #     input = """
    #     class B {
    #         final int x = 5;
    #         int foo() {
    #             int i;
    #             for i := 1 to 100 do {
    #                 x := 2;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(x),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 458))

    # def test_60(self):
    #     input = """
    #     class B {
    #         int[3] x = {1, 2, 3};
    #         int foo() {
    #             string i = x[1];
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(i),ArrayCell(Id(x),IntLit(1)))"
    #     self.assertTrue(TestChecker.test(input, expect, 459))

    # def test_61(self):
    #     input = """
    #     class B {
    #         final int[3] x = {1, 2, 3};
    #         int foo() {
    #             this.x[1] := 5;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Self(),Id(x)),IntLit(1)),IntLit(5))"
    #     self.assertTrue(TestChecker.test(input, expect, 460))

    # def test_62(self):
    #     input = """
    #     class B {
    #         int foo() {}
    #         B() {
    #             this.foo();
    #             return 3;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Self(),Id(foo),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 461))

    # def test_63(self):
    #     input = """
    #     class B {
    #         void foo() {}
    #         int x() {
    #             this.foo();
    #             break;
    #         }
    #     }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 462))

    # def test_64(self):
    #     input = """
    #     class B {
    #         void foo() {}
    #         int x() {
    #             this.foo();
    #             continue;
    #         }
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 463))

    # def test_65(self):
    #     input = """
    #     class B {
    #         void foo() {}
    #         int x() {
    #             int i;
    #             for i := 1 to 100 do {
    #                 break;
    #                 continue;
    #                 continue;
    #             }
    #             continue;
    #         }
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 464))

    # def test_66(self):
    #     input = """
    #     class B {
    #         void foo() {}
    #         int x() {
    #             int i;
    #             for i := 1 to 100 do {
    #                 break;
    #                 continue;
    #                 continue;
    #                 if 2+2 then {
    #                     int x = 2;
    #                 }
    #             }
    #             continue;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(+,IntLit(2),IntLit(2)),Block([VarDecl(Id(x),IntType,IntLit(2))],[]))"
    #     self.assertTrue(TestChecker.test(input, expect, 465))

    # def test_67(self):
    #     input = """
    #     class B {
    #         void foo() {}
    #         int x() {
    #             int i;
    #             for i := 1 to 100 do {
    #                 break;
    #                 continue;
    #                 continue;
    #                 if 2+2 == 4 then {
    #                     int x = 2;
    #                     continue;
    #                 }
    #             }
    #             continue;
    #         }
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 466))

    # def test_68(self):
    #     input = """
    #     class B {
    #         void x(int x) {
    #             this.x(x);
    #             continue;
    #         }
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 467))

    # def test_69(self):
    #     input = """
    #     class B {
    #         void x(int x) {
    #             int[2] a;
    #             a[0] := 2.3;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLit(0)),FloatLit(2.3))"
    #     self.assertTrue(TestChecker.test(input, expect, 468))

    # def test_70(self):
    #     input = """
    #     class A {
    #         void x(int x) {
    #             A a = new B();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: B"
    #     self.assertTrue(TestChecker.test(input, expect, 469))

    # def test_71(self):
    #     input = """
    #     class A {
    #         void x(int x) {
    #             A a = new A();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: <init>"
    #     self.assertTrue(TestChecker.test(input, expect, 470))

    # def test_72(self):
    #     input = """
    #     class A {
    #         A(int a) {}
    #         void x(int x) {
    #             A a = new A();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 471))

    # def test_73(self):
    #     input = """
    #     class A {
    #         A(int a) {}
    #         void x(int x) {
    #             A a = new A(2.3);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[FloatLit(2.3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 472))

    # def test_74(self):
    #     input = """
    #     class A {
    #         A(int a) {}
    #         void x(int x) {
    #             final int a = new A(2);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,NewExpr(Id(A),[IntLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 473))

    # def test_75(self):
    #     input = """
    #     class A {
    #         int[3] x;
    #         final int a = x[2];
    #     }
    #     """
    #     expect = "Illegal Constant Expression: ArrayCell(Id(x),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 474))

    # def test_76(self):
    #     input = """
    #     class Ex {
    #         final int x = Ex.a;
    #         static int a;
    #     }
    #     """
    #     expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 475))

    # def test_77(self):
    #     input = """
    #     class Ex {
    #         final int x = Ex.a;
    #         static int b;
    #     }
    #     """
    #     expect = "Undeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input, expect, 476))
    #     
    # def test_78(self):
    #     input = "class a extends b {}"
    #     expect = "Undeclared Class: b"
    #     self.assertTrue(TestChecker.test(input, expect, 477))

    # def test_79(self):
    #     input = """
    #     class A 
    #     {
    #         int[5] a;
    #         float x = a[0] + 6;
    #         int y = a[0.5] + 7;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLit(0.5))"
    #     self.assertTrue(TestChecker.test(input, expect, 478))

    # def test_80(self):
    #     input = """
    #     class ABC {
    #         int test() {
    #             int i, j;
    #             for i := 0 to 5 do {
    #                 for j := 0 to 5 do {
    #                     break;
    #                 }
    #                 break;
    #             }
    #             break;
    #         }
    #     }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 479))

    # def test_81(self):
    #     input = """
    #     class A {
    #         int math(int a; int b; float c) {
    #             int a;
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 480))

    def test_82(self):
        input = """
        class A
        {
            int x = 6;
        }
        class B extends A
        {
            final int y = -(2 + x + 7 + -9);
        }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 481))
