# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decls.
    def visitClass_decls(self, ctx:BKOOLParser.Class_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#extend_class.
    def visitExtend_class(self, ctx:BKOOLParser.Extend_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#members.
    def visitMembers(self, ctx:BKOOLParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutable_attribute_decl.
    def visitMutable_attribute_decl(self, ctx:BKOOLParser.Mutable_attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutable_attribute_decl.
    def visitImmutable_attribute_decl(self, ctx:BKOOLParser.Immutable_attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_type.
    def visitAttribute_type(self, ctx:BKOOLParser.Attribute_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_names.
    def visitAttribute_names(self, ctx:BKOOLParser.Attribute_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_name.
    def visitAttribute_name(self, ctx:BKOOLParser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#normal_method.
    def visitNormal_method(self, ctx:BKOOLParser.Normal_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#main_method.
    def visitMain_method(self, ctx:BKOOLParser.Main_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_type.
    def visitReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_type.
    def visitParam_type(self, ctx:BKOOLParser.Param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#comma_sep_ids.
    def visitComma_sep_ids(self, ctx:BKOOLParser.Comma_sep_idsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_lit.
    def visitBool_lit(self, ctx:BKOOLParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lit.
    def visitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#comma_sep_array_elmts.
    def visitComma_sep_array_elmts(self, ctx:BKOOLParser.Comma_sep_array_elmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elmt.
    def visitElmt(self, ctx:BKOOLParser.ElmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#int_type.
    def visitInt_type(self, ctx:BKOOLParser.Int_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#float_type.
    def visitFloat_type(self, ctx:BKOOLParser.Float_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_type.
    def visitBool_type(self, ctx:BKOOLParser.Bool_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#string_type.
    def visitString_type(self, ctx:BKOOLParser.String_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#void_type.
    def visitVoid_type(self, ctx:BKOOLParser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#equality_expr.
    def visitEquality_expr(self, ctx:BKOOLParser.Equality_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#boolean_expr.
    def visitBoolean_expr(self, ctx:BKOOLParser.Boolean_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bin_additive_expr.
    def visitBin_additive_expr(self, ctx:BKOOLParser.Bin_additive_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#multiplicative_expr.
    def visitMultiplicative_expr(self, ctx:BKOOLParser.Multiplicative_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#concatenation_expr.
    def visitConcatenation_expr(self, ctx:BKOOLParser.Concatenation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#not_expr.
    def visitNot_expr(self, ctx:BKOOLParser.Not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#u_additive_expr.
    def visitU_additive_expr(self, ctx:BKOOLParser.U_additive_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idx_expr.
    def visitIdx_expr(self, ctx:BKOOLParser.Idx_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#access_expr.
    def visitAccess_expr(self, ctx:BKOOLParser.Access_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#new_expr.
    def visitNew_expr(self, ctx:BKOOLParser.New_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#simple_expr.
    def visitSimple_expr(self, ctx:BKOOLParser.Simple_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atom.
    def visitAtom(self, ctx:BKOOLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#comma_sep_exprs.
    def visitComma_sep_exprs(self, ctx:BKOOLParser.Comma_sep_exprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutable_expr.
    def visitMutable_expr(self, ctx:BKOOLParser.Mutable_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_ele.
    def visitArray_ele(self, ctx:BKOOLParser.Array_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_range.
    def visitFor_range(self, ctx:BKOOLParser.For_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#init_val.
    def visitInit_val(self, ctx:BKOOLParser.Init_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#final_val.
    def visitFinal_val(self, ctx:BKOOLParser.Final_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invoc_stmt.
    def visitMethod_invoc_stmt(self, ctx:BKOOLParser.Method_invoc_stmtContext):
        return self.visitChildren(ctx)



del BKOOLParser