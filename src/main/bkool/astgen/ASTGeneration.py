from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program(ctx.class_decls().accept(self))

    # --- 2.1 ---
    # class declaration
    def visitClass_decls(self, ctx: BKOOLParser.Class_declsContext):
        if ctx.getChildCount() == 1:
            return [ctx.class_decl().accept(self)]
        else:
            return [ctx.class_decl().accept(self), *ctx.class_decls().accept(self)]

    def visitClass_decl(self, ctx: BKOOLParser.Class_declContext):
        if ctx.extend_class() == None:
            return ClassDecl(
                Id(ctx.ID().getText()),
                ctx.members().accept(self),
            )
        else:
            return ClassDecl(
                Id(ctx.ID().getText()),
                ctx.members().accept(self),
                ctx.extend_class().accept(self),
            )

    def visitExtend_class(self, ctx: BKOOLParser.Extend_classContext):
        return Id(ctx.ID().getText())

    # class members
    def visitMembers(self, ctx: BKOOLParser.MembersContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            return [*ctx.member().accept(self), *ctx.members().accept(self)]

    def visitMember(self, ctx: BKOOLParser.MemberContext):
        if ctx.mutable_attribute_decl():
            return ctx.mutable_attribute_decl().accept(self)
        if ctx.immutable_attribute_decl():
            return ctx.immutable_attribute_decl().accept(self)
        if ctx.method_decl():
            return [ctx.method_decl().accept(self)]

    # --- 2.2 ---
    # attribute declaration
    def visitMutable_attribute_decl(
        self, ctx: BKOOLParser.Mutable_attribute_declContext
    ):
        attributeNames = ctx.attribute_names().accept(self)
        type = ctx.attribute_type().accept(self)
        isStatic = ctx.STATIC() != None
        attributeDecls = []
        # aN[0]: Id
        # aN[1]: Expr assign to Id
        for aN in attributeNames:
            attributeDecls.append(
                AttributeDecl(
                    Static() if isStatic else Instance(),
                    VarDecl(aN[0], type, aN[1])
                    if len(aN) == 2
                    else VarDecl(aN[0], type),
                )
            )
        return attributeDecls

    def visitImmutable_attribute_decl(
        self, ctx: BKOOLParser.Immutable_attribute_declContext
    ):
        attributeNames = ctx.attribute_names().accept(self)
        type = ctx.attribute_type().accept(self)
        isStatic = ctx.STATIC() != None

        attributeDecls = []
        for aN in attributeNames:
            attributeDecls.append(
                AttributeDecl(
                    Static() if isStatic else Instance(),
                    ConstDecl(aN[0], type, aN[1])
                    if len(aN) == 2
                    else ConstDecl(aN[0], type),
                )
            )
        return attributeDecls

    def visitAttribute_type(self, ctx: BKOOLParser.Attribute_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.array_type():
            return ctx.array_type().accept(self)
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))

    def visitAttribute_names(self, ctx: BKOOLParser.Attribute_namesContext):
        if ctx.getChildCount() == 1:
            return [ctx.attribute_name().accept(self)]
        else:
            return [
                ctx.attribute_name().accept(self),
                *ctx.attribute_names().accept(self),
            ]

    def visitAttribute_name(self, ctx: BKOOLParser.Attribute_nameContext):
        if ctx.getChildCount() == 1:
            return (Id(ctx.ID().getText()),)
        else:
            return (Id(ctx.ID().getText()), ctx.expr().accept(self))

    # --- 2.3 ---
    # method declaration
    def visitMethod_decl(self, ctx: BKOOLParser.Method_declContext):
        if ctx.main_method():
            return ctx.main_method().accept(self)
        if ctx.normal_method():
            return ctx.normal_method().accept(self)
        if ctx.constructor():
            return ctx.constructor().accept(self)

    def visitNormal_method(self, ctx: BKOOLParser.Normal_methodContext):
        isStatic = ctx.STATIC() != None
        isParamsExist = ctx.params() != None
        return MethodDecl(
            Static() if isStatic else Instance(),
            Id(ctx.ID().getText()),
            ctx.params().accept(self) if isParamsExist else [],
            ctx.return_type().accept(self),
            ctx.block_stmt().accept(self),
        )

    def visitMain_method(self, ctx: BKOOLParser.Main_methodContext):
        return MethodDecl(
            Static(), Id("main"), [], VoidType(), ctx.block_stmt().accept(self)
        )

    def visitConstructor(self, ctx: BKOOLParser.ConstructorContext):
        isParamsExist = ctx.params() != None
        return MethodDecl(
            Instance(),
            Id("<init>"),
            ctx.params().accept(self) if isParamsExist else [],
            None,
            ctx.block_stmt().accept(self),
        )

    def visitReturn_type(self, ctx: BKOOLParser.Return_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.VOID():
            return VoidType()
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        if ctx.array_type():
            return ctx.array_type().accept(self)

    def visitParams(self, ctx: BKOOLParser.ParamsContext):
        if ctx.getChildCount() == 1:
            return ctx.param().accept(self)
        else:
            return [*ctx.param().accept(self), *ctx.params().accept(self)]

    def visitParam(self, ctx: BKOOLParser.ParamContext):
        paramIds = ctx.comma_sep_ids().accept(self)
        paramType = ctx.param_type().accept(self)
        paramDecls = []
        for pId in paramIds:
            paramDecls.append(VarDecl(pId, paramType))
        return paramDecls

    def visitParam_type(self, ctx: BKOOLParser.Param_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))

    def visitComma_sep_ids(self, ctx: BKOOLParser.Comma_sep_idsContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        else:
            return [Id(ctx.ID().getText()), *ctx.comma_sep_ids().accept(self)]

    # --- 3.7 ---
    # Literal
    def visitBool_lit(self, ctx: BKOOLParser.Bool_litContext):
        if ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)

    def visitArray_lit(self, ctx: BKOOLParser.Array_litContext):
        return (
            ArrayLiteral(ctx.comma_sep_array_elmts().accept(self))
            if ctx.comma_sep_array_elmts()
            else ArrayLiteral([])
        )

    def visitComma_sep_array_elmts(self, ctx: BKOOLParser.Comma_sep_array_elmtsContext):
        if ctx.getChildCount() == 1:
            return [ctx.elmt().accept(self)]
        else:
            return [ctx.elmt().accept(self), *ctx.comma_sep_array_elmts().accept(self)]

    def visitElmt(self, ctx: BKOOLParser.ElmtContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        if ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())
        if ctx.bool_lit():
            return ctx.bool_lit().accept(self)
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])

    # --- 4.2 ---
    # Array Type
    def visitArray_type(self, ctx: BKOOLParser.Array_typeContext):
        if ctx.INT():
            return ArrayType(int(ctx.INT_LIT().getText()), IntType())
        if ctx.FLOAT():
            return ArrayType(int(ctx.INT_LIT().getText()), FloatType())
        if ctx.BOOLEAN():
            return ArrayType(int(ctx.INT_LIT().getText()), BoolType())
        if ctx.STRING():
            return ArrayType(int(ctx.INT_LIT().getText()), StringType())
        if ctx.ID():
            return ArrayType(
                int(ctx.INT_LIT().getText()), ClassType(Id(ctx.ID().getText()))
            )

    # -- 5 --
    # Expression
    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        if ctx.getChildCount() == 1:
            return ctx.equality_expr()[0].accept(self)
        if ctx.getChildCount() == 3:
            op = ""
            if ctx.LESS():
                op = ctx.LESS().getText()
            elif ctx.GREATER():
                op = ctx.GREATER().getText()
            elif ctx.LESS_OR_EQUAL():
                op = ctx.LESS_OR_EQUAL().getText()
            elif ctx.GREATER_OR_EQUAL():
                op = ctx.GREATER_OR_EQUAL().getText()
            return BinaryOp(
                op,
                ctx.equality_expr()[0].accept(self),
                ctx.equality_expr()[1].accept(self),
            )

    def visitEquality_expr(self, ctx: BKOOLParser.Equality_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.boolean_expr()[0].accept(self)
        if ctx.getChildCount() == 3:
            op = ""
            if ctx.EQUAL():
                op = ctx.EQUAL().getText()
            elif ctx.NOT_EQUAL():
                op = ctx.NOT_EQUAL().getText()
            return BinaryOp(
                op,
                ctx.boolean_expr()[0].accept(self),
                ctx.boolean_expr()[1].accept(self),
            )

    def visitBoolean_expr(self, ctx: BKOOLParser.Boolean_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.bin_additive_expr().accept(self)
        if ctx.getChildCount() == 3:
            op = ""
            if ctx.AND():
                op = ctx.AND().getText()
            elif ctx.OR():
                op = ctx.OR().getText()
            return BinaryOp(
                op,
                ctx.boolean_expr().accept(self),
                ctx.bin_additive_expr().accept(self),
            )

    def visitBin_additive_expr(self, ctx: BKOOLParser.Bin_additive_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.multiplicative_expr().accept(self)
        if ctx.getChildCount() == 3:
            op = ""
            if ctx.ADDOP():
                op = ctx.ADDOP().getText()
            elif ctx.SUBOP():
                op = ctx.SUBOP().getText()
            return BinaryOp(
                op,
                ctx.bin_additive_expr().accept(self),
                ctx.multiplicative_expr().accept(self),
            )

    def visitMultiplicative_expr(self, ctx: BKOOLParser.Multiplicative_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.concatenation_expr().accept(self)
        if ctx.getChildCount() == 3:
            op = ""
            if ctx.MULOP():
                op = ctx.MULOP().getText()
            elif ctx.I_DIV():
                op = ctx.I_DIV().getText()
            elif ctx.F_DIV():
                op = ctx.F_DIV().getText()
            elif ctx.MOD():
                op = ctx.MOD().getText()
            return BinaryOp(
                op,
                ctx.multiplicative_expr().accept(self),
                ctx.concatenation_expr().accept(self),
            )

    def visitConcatenation_expr(self, ctx: BKOOLParser.Concatenation_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.not_expr().accept(self)
        if ctx.getChildCount() == 3:
            op = ctx.CONCATENATION().getText()
            return BinaryOp(
                op, ctx.concatenation_expr().accept(self), ctx.not_expr().accept(self)
            )

    def visitNot_expr(self, ctx: BKOOLParser.Not_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.u_additive_expr().accept(self)
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOT().getText(), ctx.not_expr().accept(self))

    def visitU_additive_expr(self, ctx: BKOOLParser.U_additive_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.idx_expr().accept(self)
        if ctx.getChildCount() == 2:
            op = ""
            if ctx.ADDOP():
                op = ctx.ADDOP().getText()
            elif ctx.SUBOP():
                op = ctx.SUBOP().getText()
            return UnaryOp(op, ctx.u_additive_expr().accept(self))

    def visitIdx_expr(self, ctx: BKOOLParser.Idx_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.access_expr().accept(self)
        if ctx.getChildCount() == 4:
            return ArrayCell(ctx.access_expr().accept(self), ctx.expr().accept(self))

    def visitAccess_expr(self, ctx: BKOOLParser.Access_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.new_expr().accept(self)
        else:
            if ctx.LB():
                return CallExpr(
                    ctx.access_expr().accept(self),
                    Id(ctx.ID().getText()),
                    ctx.comma_sep_exprs().accept(self) if ctx.comma_sep_exprs() else [],
                )
            else:
                return FieldAccess(
                    ctx.access_expr().accept(self), Id(ctx.ID().getText())
                )

    def visitNew_expr(self, ctx: BKOOLParser.New_exprContext):
        if ctx.getChildCount() == 1:
            return ctx.simple_expr().accept(self)
        else:
            areParamsExist = ctx.comma_sep_exprs() != None
            return NewExpr(
                ctx.new_expr().accept(self),
                ctx.comma_sep_exprs().accept(self) if areParamsExist else [],
            )

    def visitSimple_expr(self, ctx: BKOOLParser.Simple_exprContext):
        return ctx.atom().accept(self)

    def visitAtom(self, ctx: BKOOLParser.AtomContext):
        if ctx.getChildCount() == 3:
            return ctx.expr().accept(self)
        if ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(ctx.INT_LIT().getText())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.bool_lit():
            return ctx.bool_lit().accept(self)
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText()[1:-1])
        elif ctx.array_lit():
            return ctx.array_lit().accept(self)

    def visitComma_sep_exprs(self, ctx: BKOOLParser.Comma_sep_exprsContext):
        if ctx.getChildCount() == 1:
            return [ctx.expr().accept(self)]
        else:
            return [ctx.expr().accept(self), *ctx.comma_sep_exprs().accept(self)]

    # -- 6 --
    # Statement
    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        if ctx.assign_stmt():
            return ctx.assign_stmt().accept(self)
        if ctx.if_stmt():
            return ctx.if_stmt().accept(self)
        if ctx.for_stmt():
            return ctx.for_stmt().accept(self)
        if ctx.break_stmt():
            return ctx.break_stmt().accept(self)
        if ctx.continue_stmt():
            return ctx.continue_stmt().accept(self)
        if ctx.return_stmt():
            return ctx.return_stmt().accept(self)
        if ctx.method_invoc_stmt():
            return ctx.method_invoc_stmt().accept(self)
        if ctx.block_stmt():
            return ctx.block_stmt().accept(self)

    # --- 6.1 ---
    # Block statement
    def visitBlock_stmt(self, ctx: BKOOLParser.Block_stmtContext):
        decls = []
        for declContext in ctx.var_decl():
            subDecls = declContext.accept(self)
            decls = [*decls, *subDecls]

        stmts = []
        for stmtContext in ctx.stmt():
            stmts.append(stmtContext.accept(self))
        return Block(decls, stmts)

    def visitVar_decl(self, ctx: BKOOLParser.Var_declContext):
        attributeNames = ctx.attribute_names().accept(self)
        type = ctx.attribute_type().accept(self)
        subDecls = []
        if ctx.FINAL():
            # aN[0]: Id
            # aN[1]: Expr assign to Id
            for aN in attributeNames:
                subDecls.append(ConstDecl(aN[0], type, aN[1]))
        else:
            # aN[0]: Id
            # aN[1]: Expr assign to Id
            for aN in attributeNames:
                subDecls.append(
                    VarDecl(aN[0], type, aN[1])
                    if len(aN) == 2
                    else VarDecl(aN[0], type),
                )

        return subDecls

    # --- 6.2 ---
    # Assignment statement
    def visitAssign_stmt(self, ctx: BKOOLParser.Assign_stmtContext):
        return Assign(
            ctx.lhs().accept(self),
            ctx.expr().accept(self),
        )

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.mutable_expr():
            return ctx.mutable_expr().accept(self)
        if ctx.array_ele():
            return ctx.array_ele().accept(self)

    def visitMutable_expr(self, ctx: BKOOLParser.Mutable_exprContext):
        if len(ctx.ID()) == 1:
            if ctx.expr():
                return ArrayCell(
                    FieldAccess(SelfLiteral(), Id(ctx.ID()[0].getText())),
                    ctx.expr().accept(self),
                )
            else:
                return FieldAccess(SelfLiteral(), Id(ctx.ID()[0].getText()))
        else:
            if ctx.expr():
                return ArrayCell(
                    FieldAccess(Id(ctx.ID()[0].getText()), Id(ctx.ID()[1].getText())),
                    ctx.expr().accept(self),
                )
            else:
                return FieldAccess(Id(ctx.ID()[0].getText()), Id(ctx.ID()[1].getText()))

    def visitArray_ele(self, ctx: BKOOLParser.Array_eleContext):
        return ArrayCell(Id(ctx.ID().getText()), ctx.expr().accept(self))

    # --- 6.3 ---
    # If statement
    def visitIf_stmt(self, ctx: BKOOLParser.If_stmtContext):
        if ctx.ELSE():
            return If(
                ctx.expr().accept(self),
                ctx.stmt()[0].accept(self),
                ctx.stmt()[1].accept(self),
            )
        else:
            return If(ctx.expr().accept(self), ctx.stmt()[0].accept(self))

    # --- 6.4 ---
    # For statement
    def visitFor_stmt(self, ctx: BKOOLParser.For_stmtContext):
        for_range = ctx.for_range().accept(self)
        return For(
            Id(ctx.ID().getText()),
            for_range[0],
            for_range[1],
            for_range[2],
            ctx.stmt().accept(self),
        )

    def visitFor_range(self, ctx: BKOOLParser.For_rangeContext):
        return [
            ctx.init_val().accept(self),
            ctx.final_val().accept(self),
            ctx.TO() != None,
        ]

    def visitInit_val(self, ctx: BKOOLParser.Init_valContext):
        return ctx.expr().accept(self)

    def visitFinal_val(self, ctx: BKOOLParser.Final_valContext):
        return ctx.expr().accept(self)

    # --- 6.5 ---
    # Break statement
    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        return Break()

    # --- 6.6 ---
    # Continue statement
    def visitContinue_stmt(self, ctx: BKOOLParser.Continue_stmtContext):
        return Continue()

    # --- 6.7 ---
    # Return statement
    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        return Return(ctx.expr().accept(self))

    # --- 6.8 ---
    # Method Invocation statement
    def visitMethod_invoc_stmt(self, ctx: BKOOLParser.Method_invoc_stmtContext):
        return CallStmt(
            ctx.expr().accept(self),
            Id(ctx.ID().getText()),
            ctx.comma_sep_exprs().accept(self) if ctx.comma_sep_exprs() else [],
        )
