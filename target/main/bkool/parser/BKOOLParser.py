# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0205\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0084")
        buf.write("\n\3\3\4\3\4\3\4\5\4\u0089\n\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\5\6\u0096\n\6\3\7\3\7\3\7\5\7\u009b")
        buf.write("\n\7\3\b\5\b\u009e\n\b\3\b\3\b\3\b\3\b\3\t\5\t\u00a5\n")
        buf.write("\t\3\t\3\t\3\t\5\t\u00aa\n\t\5\t\u00ac\n\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b8\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00bf\n\13\3\f\3\f\3\f\3\f\5\f\u00c5")
        buf.write("\n\f\3\r\3\r\3\r\5\r\u00ca\n\r\3\16\5\16\u00cd\n\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00d3\n\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u00e1\n")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00ed\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00f4\n")
        buf.write("\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00ff\n\25\3\26\3\26\3\27\3\27\5\27\u0105\n\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\5\30\u010e\n\30\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0114\n\31\3\32\3\32\3\33\3\33\3\34\3")
        buf.write("\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \3 \3 \5 \u012a\n \3!\3!\3!\3!\3!\5!\u0131\n!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\7\"\u0139\n\"\f\"\16\"\u013c\13\"")
        buf.write("\3#\3#\3#\3#\3#\3#\7#\u0144\n#\f#\16#\u0147\13#\3$\3$")
        buf.write("\3$\3$\3$\3$\7$\u014f\n$\f$\16$\u0152\13$\3%\3%\3%\3%")
        buf.write("\3%\3%\7%\u015a\n%\f%\16%\u015d\13%\3&\3&\3&\5&\u0162")
        buf.write("\n&\3\'\3\'\3\'\5\'\u0167\n\'\3(\3(\3(\3(\3(\3(\5(\u016f")
        buf.write("\n(\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0179\n)\3)\5)\u017c\n")
        buf.write(")\7)\u017e\n)\f)\16)\u0181\13)\3*\3*\3*\3*\5*\u0187\n")
        buf.write("*\3*\3*\3*\5*\u018c\n*\3+\3+\3,\3,\3,\3,\3,\3,\3,\5,\u0197")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u019e\n-\3.\3.\3.\3.\3.\5.\u01a5")
        buf.write("\n.\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01af\n/\3\60\3\60\3\60")
        buf.write("\7\60\u01b4\n\60\f\60\16\60\u01b7\13\60\3\60\3\60\3\61")
        buf.write("\5\61\u01bc\n\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\63\3\63\3\63\5\63\u01ca\n\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u01d3\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01e0\n\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39")
        buf.write("\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\5")
        buf.write(">\u0200\n>\3>\3>\3>\3>\2\7BDFHP?\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz\2\13\7\2\6\6\r\r\17\17\21\21::\3")
        buf.write("\2\25\26\3\2&)\3\2$%\3\2*+\3\2\36\37\3\2 #\4\2\31\31:")
        buf.write(":\3\2\34\35\2\u020e\2|\3\2\2\2\4\u0083\3\2\2\2\6\u0085")
        buf.write("\3\2\2\2\b\u008e\3\2\2\2\n\u0095\3\2\2\2\f\u009a\3\2\2")
        buf.write("\2\16\u009d\3\2\2\2\20\u00ab\3\2\2\2\22\u00b7\3\2\2\2")
        buf.write("\24\u00be\3\2\2\2\26\u00c4\3\2\2\2\30\u00c9\3\2\2\2\32")
        buf.write("\u00cc\3\2\2\2\34\u00d7\3\2\2\2\36\u00dd\3\2\2\2 \u00ec")
        buf.write("\3\2\2\2\"\u00f3\3\2\2\2$\u00f5\3\2\2\2&\u00f8\3\2\2\2")
        buf.write("(\u00fe\3\2\2\2*\u0100\3\2\2\2,\u0102\3\2\2\2.\u010d\3")
        buf.write("\2\2\2\60\u0113\3\2\2\2\62\u0115\3\2\2\2\64\u0117\3\2")
        buf.write("\2\2\66\u0119\3\2\2\28\u011b\3\2\2\2:\u011d\3\2\2\2<\u011f")
        buf.write("\3\2\2\2>\u0129\3\2\2\2@\u0130\3\2\2\2B\u0132\3\2\2\2")
        buf.write("D\u013d\3\2\2\2F\u0148\3\2\2\2H\u0153\3\2\2\2J\u0161\3")
        buf.write("\2\2\2L\u0166\3\2\2\2N\u016e\3\2\2\2P\u0170\3\2\2\2R\u018b")
        buf.write("\3\2\2\2T\u018d\3\2\2\2V\u0196\3\2\2\2X\u019d\3\2\2\2")
        buf.write("Z\u01a4\3\2\2\2\\\u01ae\3\2\2\2^\u01b0\3\2\2\2`\u01bb")
        buf.write("\3\2\2\2b\u01c1\3\2\2\2d\u01c9\3\2\2\2f\u01cb\3\2\2\2")
        buf.write("h\u01d4\3\2\2\2j\u01d9\3\2\2\2l\u01e1\3\2\2\2n\u01e8\3")
        buf.write("\2\2\2p\u01ec\3\2\2\2r\u01ee\3\2\2\2t\u01f0\3\2\2\2v\u01f3")
        buf.write("\3\2\2\2x\u01f6\3\2\2\2z\u01fa\3\2\2\2|}\5\4\3\2}~\7\2")
        buf.write("\2\3~\3\3\2\2\2\177\u0080\5\6\4\2\u0080\u0081\5\4\3\2")
        buf.write("\u0081\u0084\3\2\2\2\u0082\u0084\5\6\4\2\u0083\177\3\2")
        buf.write("\2\2\u0083\u0082\3\2\2\2\u0084\5\3\2\2\2\u0085\u0086\7")
        buf.write("\b\2\2\u0086\u0088\7:\2\2\u0087\u0089\5\b\5\2\u0088\u0087")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008b\7\62\2\2\u008b\u008c\5\n\6\2\u008c\u008d\7\63\2")
        buf.write("\2\u008d\7\3\2\2\2\u008e\u008f\7\f\2\2\u008f\u0090\7:")
        buf.write("\2\2\u0090\t\3\2\2\2\u0091\u0092\5\f\7\2\u0092\u0093\5")
        buf.write("\n\6\2\u0093\u0096\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0091")
        buf.write("\3\2\2\2\u0095\u0094\3\2\2\2\u0096\13\3\2\2\2\u0097\u009b")
        buf.write("\5\16\b\2\u0098\u009b\5\20\t\2\u0099\u009b\5\30\r\2\u009a")
        buf.write("\u0097\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2")
        buf.write("\u009b\r\3\2\2\2\u009c\u009e\7\33\2\2\u009d\u009c\3\2")
        buf.write("\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\5\22\n\2\u00a0\u00a1\5\24\13\2\u00a1\u00a2\7\66\2\2\u00a2")
        buf.write("\17\3\2\2\2\u00a3\u00a5\7\33\2\2\u00a4\u00a3\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00ac\7\32\2")
        buf.write("\2\u00a7\u00a9\7\32\2\2\u00a8\u00aa\7\33\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab")
        buf.write("\u00a4\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00ae\5\22\n\2\u00ae\u00af\5\24\13\2\u00af\u00b0")
        buf.write("\7\66\2\2\u00b0\21\3\2\2\2\u00b1\u00b8\7\17\2\2\u00b2")
        buf.write("\u00b8\7\r\2\2\u00b3\u00b8\7\6\2\2\u00b4\u00b8\7\21\2")
        buf.write("\2\u00b5\u00b8\5<\37\2\u00b6\u00b8\7:\2\2\u00b7\u00b1")
        buf.write("\3\2\2\2\u00b7\u00b2\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b7")
        buf.write("\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b8\23\3\2\2\2\u00b9\u00ba\5\26\f\2\u00ba\u00bb\79")
        buf.write("\2\2\u00bb\u00bc\5\24\13\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf")
        buf.write("\5\26\f\2\u00be\u00b9\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\25\3\2\2\2\u00c0\u00c5\7:\2\2\u00c1\u00c2\7:\2\2\u00c2")
        buf.write("\u00c3\7/\2\2\u00c3\u00c5\5> \2\u00c4\u00c0\3\2\2\2\u00c4")
        buf.write("\u00c1\3\2\2\2\u00c5\27\3\2\2\2\u00c6\u00ca\5\32\16\2")
        buf.write("\u00c7\u00ca\5\34\17\2\u00c8\u00ca\5\36\20\2\u00c9\u00c6")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca")
        buf.write("\31\3\2\2\2\u00cb\u00cd\7\33\2\2\u00cc\u00cb\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\5 \21\2")
        buf.write("\u00cf\u00d0\7:\2\2\u00d0\u00d2\7\64\2\2\u00d1\u00d3\5")
        buf.write("\"\22\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d5\7\65\2\2\u00d5\u00d6\5^\60")
        buf.write("\2\u00d6\33\3\2\2\2\u00d7\u00d8\7\27\2\2\u00d8\u00d9\7")
        buf.write("\3\2\2\u00d9\u00da\7\64\2\2\u00da\u00db\7\65\2\2\u00db")
        buf.write("\u00dc\5^\60\2\u00dc\35\3\2\2\2\u00dd\u00de\7:\2\2\u00de")
        buf.write("\u00e0\7\64\2\2\u00df\u00e1\5\"\22\2\u00e0\u00df\3\2\2")
        buf.write("\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3")
        buf.write("\7\65\2\2\u00e3\u00e4\5^\60\2\u00e4\37\3\2\2\2\u00e5\u00ed")
        buf.write("\7\17\2\2\u00e6\u00ed\7\r\2\2\u00e7\u00ed\7\6\2\2\u00e8")
        buf.write("\u00ed\7\21\2\2\u00e9\u00ed\7\27\2\2\u00ea\u00ed\7:\2")
        buf.write("\2\u00eb\u00ed\5<\37\2\u00ec\u00e5\3\2\2\2\u00ec\u00e6")
        buf.write("\3\2\2\2\u00ec\u00e7\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed!\3\2\2\2\u00ee\u00ef\5$\23\2\u00ef\u00f0\7\66\2")
        buf.write("\2\u00f0\u00f1\5\"\22\2\u00f1\u00f4\3\2\2\2\u00f2\u00f4")
        buf.write("\5$\23\2\u00f3\u00ee\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("#\3\2\2\2\u00f5\u00f6\5&\24\2\u00f6\u00f7\5(\25\2\u00f7")
        buf.write("%\3\2\2\2\u00f8\u00f9\t\2\2\2\u00f9\'\3\2\2\2\u00fa\u00fb")
        buf.write("\7:\2\2\u00fb\u00fc\79\2\2\u00fc\u00ff\5(\25\2\u00fd\u00ff")
        buf.write("\7:\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write(")\3\2\2\2\u0100\u0101\t\3\2\2\u0101+\3\2\2\2\u0102\u0104")
        buf.write("\7\62\2\2\u0103\u0105\5.\30\2\u0104\u0103\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\7\63\2")
        buf.write("\2\u0107-\3\2\2\2\u0108\u0109\5\60\31\2\u0109\u010a\7")
        buf.write("9\2\2\u010a\u010b\5.\30\2\u010b\u010e\3\2\2\2\u010c\u010e")
        buf.write("\5\60\31\2\u010d\u0108\3\2\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write("/\3\2\2\2\u010f\u0114\7;\2\2\u0110\u0114\7<\2\2\u0111")
        buf.write("\u0114\5*\26\2\u0112\u0114\7=\2\2\u0113\u010f\3\2\2\2")
        buf.write("\u0113\u0110\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0112\3")
        buf.write("\2\2\2\u0114\61\3\2\2\2\u0115\u0116\7\17\2\2\u0116\63")
        buf.write("\3\2\2\2\u0117\u0118\7\r\2\2\u0118\65\3\2\2\2\u0119\u011a")
        buf.write("\7\6\2\2\u011a\67\3\2\2\2\u011b\u011c\7\21\2\2\u011c9")
        buf.write("\3\2\2\2\u011d\u011e\7\27\2\2\u011e;\3\2\2\2\u011f\u0120")
        buf.write("\t\2\2\2\u0120\u0121\7\60\2\2\u0121\u0122\7;\2\2\u0122")
        buf.write("\u0123\7\61\2\2\u0123=\3\2\2\2\u0124\u0125\5@!\2\u0125")
        buf.write("\u0126\t\4\2\2\u0126\u0127\5@!\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u012a\5@!\2\u0129\u0124\3\2\2\2\u0129\u0128\3\2\2\2\u012a")
        buf.write("?\3\2\2\2\u012b\u012c\5B\"\2\u012c\u012d\t\5\2\2\u012d")
        buf.write("\u012e\5B\"\2\u012e\u0131\3\2\2\2\u012f\u0131\5B\"\2\u0130")
        buf.write("\u012b\3\2\2\2\u0130\u012f\3\2\2\2\u0131A\3\2\2\2\u0132")
        buf.write("\u0133\b\"\1\2\u0133\u0134\5D#\2\u0134\u013a\3\2\2\2\u0135")
        buf.write("\u0136\f\4\2\2\u0136\u0137\t\6\2\2\u0137\u0139\5D#\2\u0138")
        buf.write("\u0135\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2")
        buf.write("\u013a\u013b\3\2\2\2\u013bC\3\2\2\2\u013c\u013a\3\2\2")
        buf.write("\2\u013d\u013e\b#\1\2\u013e\u013f\5F$\2\u013f\u0145\3")
        buf.write("\2\2\2\u0140\u0141\f\4\2\2\u0141\u0142\t\7\2\2\u0142\u0144")
        buf.write("\5F$\2\u0143\u0140\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143")
        buf.write("\3\2\2\2\u0145\u0146\3\2\2\2\u0146E\3\2\2\2\u0147\u0145")
        buf.write("\3\2\2\2\u0148\u0149\b$\1\2\u0149\u014a\5H%\2\u014a\u0150")
        buf.write("\3\2\2\2\u014b\u014c\f\4\2\2\u014c\u014d\t\b\2\2\u014d")
        buf.write("\u014f\5H%\2\u014e\u014b\3\2\2\2\u014f\u0152\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151G\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0153\u0154\b%\1\2\u0154\u0155\5J&\2\u0155")
        buf.write("\u015b\3\2\2\2\u0156\u0157\f\4\2\2\u0157\u0158\7-\2\2")
        buf.write("\u0158\u015a\5J&\2\u0159\u0156\3\2\2\2\u015a\u015d\3\2")
        buf.write("\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015cI\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\7,\2\2\u015f\u0162")
        buf.write("\5J&\2\u0160\u0162\5L\'\2\u0161\u015e\3\2\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162K\3\2\2\2\u0163\u0164\t\7\2\2\u0164\u0167")
        buf.write("\5L\'\2\u0165\u0167\5N(\2\u0166\u0163\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167M\3\2\2\2\u0168\u0169\5P)\2\u0169\u016a")
        buf.write("\7\60\2\2\u016a\u016b\5> \2\u016b\u016c\7\61\2\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016f\5P)\2\u016e\u0168\3\2\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016fO\3\2\2\2\u0170\u0171\b)\1\2\u0171")
        buf.write("\u0172\5R*\2\u0172\u017f\3\2\2\2\u0173\u0174\f\4\2\2\u0174")
        buf.write("\u0175\78\2\2\u0175\u017b\7:\2\2\u0176\u0178\7\64\2\2")
        buf.write("\u0177\u0179\5Z.\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2")
        buf.write("\2\2\u0179\u017a\3\2\2\2\u017a\u017c\7\65\2\2\u017b\u0176")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write("\u0173\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180Q\3\2\2\2\u0181\u017f\3\2\2")
        buf.write("\2\u0182\u0183\7\20\2\2\u0183\u0184\5R*\2\u0184\u0186")
        buf.write("\7\64\2\2\u0185\u0187\5Z.\2\u0186\u0185\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\7\65\2")
        buf.write("\2\u0189\u018c\3\2\2\2\u018a\u018c\5T+\2\u018b\u0182\3")
        buf.write("\2\2\2\u018b\u018a\3\2\2\2\u018cS\3\2\2\2\u018d\u018e")
        buf.write("\5V,\2\u018eU\3\2\2\2\u018f\u0197\5X-\2\u0190\u0197\7")
        buf.write("\31\2\2\u0191\u0197\7:\2\2\u0192\u0193\7\64\2\2\u0193")
        buf.write("\u0194\5> \2\u0194\u0195\7\65\2\2\u0195\u0197\3\2\2\2")
        buf.write("\u0196\u018f\3\2\2\2\u0196\u0190\3\2\2\2\u0196\u0191\3")
        buf.write("\2\2\2\u0196\u0192\3\2\2\2\u0197W\3\2\2\2\u0198\u019e")
        buf.write("\7;\2\2\u0199\u019e\7<\2\2\u019a\u019e\5*\26\2\u019b\u019e")
        buf.write("\7=\2\2\u019c\u019e\5,\27\2\u019d\u0198\3\2\2\2\u019d")
        buf.write("\u0199\3\2\2\2\u019d\u019a\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019c\3\2\2\2\u019eY\3\2\2\2\u019f\u01a0\5> \2")
        buf.write("\u01a0\u01a1\79\2\2\u01a1\u01a2\5Z.\2\u01a2\u01a5\3\2")
        buf.write("\2\2\u01a3\u01a5\5> \2\u01a4\u019f\3\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5[\3\2\2\2\u01a6\u01af\5b\62\2\u01a7\u01af")
        buf.write("\5j\66\2\u01a8\u01af\5l\67\2\u01a9\u01af\5t;\2\u01aa\u01af")
        buf.write("\5v<\2\u01ab\u01af\5x=\2\u01ac\u01af\5z>\2\u01ad\u01af")
        buf.write("\5^\60\2\u01ae\u01a6\3\2\2\2\u01ae\u01a7\3\2\2\2\u01ae")
        buf.write("\u01a8\3\2\2\2\u01ae\u01a9\3\2\2\2\u01ae\u01aa\3\2\2\2")
        buf.write("\u01ae\u01ab\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad\3")
        buf.write("\2\2\2\u01af]\3\2\2\2\u01b0\u01b5\7\62\2\2\u01b1\u01b4")
        buf.write("\5`\61\2\u01b2\u01b4\5\\/\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b8\u01b9\7\63\2\2\u01b9_\3\2\2\2\u01ba\u01bc")
        buf.write("\7\32\2\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\5\22\n\2\u01be\u01bf\5\24\13")
        buf.write("\2\u01bf\u01c0\7\66\2\2\u01c0a\3\2\2\2\u01c1\u01c2\5d")
        buf.write("\63\2\u01c2\u01c3\7.\2\2\u01c3\u01c4\5> \2\u01c4\u01c5")
        buf.write("\7\66\2\2\u01c5c\3\2\2\2\u01c6\u01ca\5f\64\2\u01c7\u01ca")
        buf.write("\5h\65\2\u01c8\u01ca\7:\2\2\u01c9\u01c6\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01cae\3\2\2\2\u01cb")
        buf.write("\u01cc\t\t\2\2\u01cc\u01cd\78\2\2\u01cd\u01d2\7:\2\2\u01ce")
        buf.write("\u01cf\7\60\2\2\u01cf\u01d0\5> \2\u01d0\u01d1\7\61\2\2")
        buf.write("\u01d1\u01d3\3\2\2\2\u01d2\u01ce\3\2\2\2\u01d2\u01d3\3")
        buf.write("\2\2\2\u01d3g\3\2\2\2\u01d4\u01d5\7:\2\2\u01d5\u01d6\7")
        buf.write("\60\2\2\u01d6\u01d7\5> \2\u01d7\u01d8\7\61\2\2\u01d8i")
        buf.write("\3\2\2\2\u01d9\u01da\7\16\2\2\u01da\u01db\5> \2\u01db")
        buf.write("\u01dc\7\22\2\2\u01dc\u01df\5\\/\2\u01dd\u01de\7\13\2")
        buf.write("\2\u01de\u01e0\5\\/\2\u01df\u01dd\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0k\3\2\2\2\u01e1\u01e2\7\23\2\2\u01e2\u01e3")
        buf.write("\7:\2\2\u01e3\u01e4\7.\2\2\u01e4\u01e5\5n8\2\u01e5\u01e6")
        buf.write("\7\n\2\2\u01e6\u01e7\5\\/\2\u01e7m\3\2\2\2\u01e8\u01e9")
        buf.write("\5p9\2\u01e9\u01ea\t\n\2\2\u01ea\u01eb\5r:\2\u01ebo\3")
        buf.write("\2\2\2\u01ec\u01ed\5> \2\u01edq\3\2\2\2\u01ee\u01ef\5")
        buf.write("> \2\u01efs\3\2\2\2\u01f0\u01f1\7\7\2\2\u01f1\u01f2\7")
        buf.write("\66\2\2\u01f2u\3\2\2\2\u01f3\u01f4\7\t\2\2\u01f4\u01f5")
        buf.write("\7\66\2\2\u01f5w\3\2\2\2\u01f6\u01f7\7\24\2\2\u01f7\u01f8")
        buf.write("\5> \2\u01f8\u01f9\7\66\2\2\u01f9y\3\2\2\2\u01fa\u01fb")
        buf.write("\5> \2\u01fb\u01fc\78\2\2\u01fc\u01fd\7:\2\2\u01fd\u01ff")
        buf.write("\7\64\2\2\u01fe\u0200\5Z.\2\u01ff\u01fe\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202\7\65\2")
        buf.write("\2\u0202\u0203\7\66\2\2\u0203{\3\2\2\2\60\u0083\u0088")
        buf.write("\u0095\u009a\u009d\u00a4\u00a9\u00ab\u00b7\u00be\u00c4")
        buf.write("\u00c9\u00cc\u00d2\u00e0\u00ec\u00f3\u00fe\u0104\u010d")
        buf.write("\u0113\u0129\u0130\u013a\u0145\u0150\u015b\u0161\u0166")
        buf.write("\u016e\u0178\u017b\u017f\u0186\u018b\u0196\u019d\u01a4")
        buf.write("\u01ae\u01b3\u01b5\u01bb\u01c9\u01d2\u01df\u01ff")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "'boolean'", 
                     "'break'", "'class'", "'continue'", "'do'", "'else'", 
                     "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
                     "'then'", "'for'", "'return'", "'true'", "'false'", 
                     "'void'", "'nil'", "'this'", "'final'", "'static'", 
                     "'to'", "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", 
                     "'%'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", 
                     "'||'", "'&&'", "'!'", "'^'", "':='", "'='", "'['", 
                     "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT_LINE", "COMMENT_BLOCK", 
                      "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                      "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
                      "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                      "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADDOP", "SUBOP", "MULOP", "I_DIV", "F_DIV", "MOD", 
                      "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                      "GREATER_OR_EQUAL", "OR", "AND", "NOT", "CONCATENATION", 
                      "ASSIGN", "EQUAL_SIGN", "LSB", "RSB", "LP", "RP", 
                      "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", "ID", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decls = 1
    RULE_class_decl = 2
    RULE_extend_class = 3
    RULE_members = 4
    RULE_member = 5
    RULE_mutable_attribute_decl = 6
    RULE_immutable_attribute_decl = 7
    RULE_attribute_type = 8
    RULE_attribute_names = 9
    RULE_attribute_name = 10
    RULE_method_decl = 11
    RULE_normal_method = 12
    RULE_main_method = 13
    RULE_constructor = 14
    RULE_return_type = 15
    RULE_params = 16
    RULE_param = 17
    RULE_param_type = 18
    RULE_comma_sep_ids = 19
    RULE_bool_lit = 20
    RULE_array_lit = 21
    RULE_comma_sep_array_elmts = 22
    RULE_elmt = 23
    RULE_int_type = 24
    RULE_float_type = 25
    RULE_bool_type = 26
    RULE_string_type = 27
    RULE_void_type = 28
    RULE_array_type = 29
    RULE_expr = 30
    RULE_equality_expr = 31
    RULE_boolean_expr = 32
    RULE_bin_additive_expr = 33
    RULE_multiplicative_expr = 34
    RULE_concatenation_expr = 35
    RULE_not_expr = 36
    RULE_u_additive_expr = 37
    RULE_idx_expr = 38
    RULE_access_expr = 39
    RULE_new_expr = 40
    RULE_simple_expr = 41
    RULE_atom = 42
    RULE_literal = 43
    RULE_comma_sep_exprs = 44
    RULE_stmt = 45
    RULE_block_stmt = 46
    RULE_var_decl = 47
    RULE_assign_stmt = 48
    RULE_lhs = 49
    RULE_mutable_expr = 50
    RULE_array_ele = 51
    RULE_if_stmt = 52
    RULE_for_stmt = 53
    RULE_for_range = 54
    RULE_init_val = 55
    RULE_final_val = 56
    RULE_break_stmt = 57
    RULE_continue_stmt = 58
    RULE_return_stmt = 59
    RULE_method_invoc_stmt = 60

    ruleNames =  [ "program", "class_decls", "class_decl", "extend_class", 
                   "members", "member", "mutable_attribute_decl", "immutable_attribute_decl", 
                   "attribute_type", "attribute_names", "attribute_name", 
                   "method_decl", "normal_method", "main_method", "constructor", 
                   "return_type", "params", "param", "param_type", "comma_sep_ids", 
                   "bool_lit", "array_lit", "comma_sep_array_elmts", "elmt", 
                   "int_type", "float_type", "bool_type", "string_type", 
                   "void_type", "array_type", "expr", "equality_expr", "boolean_expr", 
                   "bin_additive_expr", "multiplicative_expr", "concatenation_expr", 
                   "not_expr", "u_additive_expr", "idx_expr", "access_expr", 
                   "new_expr", "simple_expr", "atom", "literal", "comma_sep_exprs", 
                   "stmt", "block_stmt", "var_decl", "assign_stmt", "lhs", 
                   "mutable_expr", "array_ele", "if_stmt", "for_stmt", "for_range", 
                   "init_val", "final_val", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_invoc_stmt" ]

    EOF = Token.EOF
    T__0=1
    COMMENT_LINE=2
    COMMENT_BLOCK=3
    BOOLEAN=4
    BREAK=5
    CLASS=6
    CONTINUE=7
    DO=8
    ELSE=9
    EXTENDS=10
    FLOAT=11
    IF=12
    INT=13
    NEW=14
    STRING=15
    THEN=16
    FOR=17
    RETURN=18
    TRUE=19
    FALSE=20
    VOID=21
    NIL=22
    THIS=23
    FINAL=24
    STATIC=25
    TO=26
    DOWNTO=27
    ADDOP=28
    SUBOP=29
    MULOP=30
    I_DIV=31
    F_DIV=32
    MOD=33
    NOT_EQUAL=34
    EQUAL=35
    LESS=36
    GREATER=37
    LESS_OR_EQUAL=38
    GREATER_OR_EQUAL=39
    OR=40
    AND=41
    NOT=42
    CONCATENATION=43
    ASSIGN=44
    EQUAL_SIGN=45
    LSB=46
    RSB=47
    LP=48
    RP=49
    LB=50
    RB=51
    SEMI=52
    COLON=53
    DOT=54
    COMMA=55
    ID=56
    INT_LIT=57
    FLOAT_LIT=58
    STRING_LIT=59
    WS=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Class_declsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.class_decls()
            self.state = 123
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Class_declContext,0)


        def class_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Class_declsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decls" ):
                return visitor.visitClass_decls(self)
            else:
                return visitor.visitChildren(self)




    def class_decls(self):

        localctx = BKOOLParser.Class_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decls)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.class_decl()
                self.state = 126
                self.class_decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.class_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def members(self):
            return self.getTypedRuleContext(BKOOLParser.MembersContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def extend_class(self):
            return self.getTypedRuleContext(BKOOLParser.Extend_classContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(BKOOLParser.CLASS)
            self.state = 132
            self.match(BKOOLParser.ID)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 133
                self.extend_class()


            self.state = 136
            self.match(BKOOLParser.LP)
            self.state = 137
            self.members()
            self.state = 138
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extend_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_extend_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtend_class" ):
                return visitor.visitExtend_class(self)
            else:
                return visitor.visitChildren(self)




    def extend_class(self):

        localctx = BKOOLParser.Extend_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_extend_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(BKOOLParser.EXTENDS)
            self.state = 141
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def members(self):
            return self.getTypedRuleContext(BKOOLParser.MembersContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = BKOOLParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_members)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.state = 143
                self.member()
                self.state = 144
                self.members()
                pass
            elif token in [BKOOLParser.RP]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutable_attribute_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Mutable_attribute_declContext,0)


        def immutable_attribute_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Immutable_attribute_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.mutable_attribute_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.immutable_attribute_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.method_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mutable_attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_type(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_typeContext,0)


        def attribute_names(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_namesContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutable_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable_attribute_decl" ):
                return visitor.visitMutable_attribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def mutable_attribute_decl(self):

        localctx = BKOOLParser.Mutable_attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mutable_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 154
                self.match(BKOOLParser.STATIC)


            self.state = 157
            self.attribute_type()
            self.state = 158
            self.attribute_names()
            self.state = 159
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Immutable_attribute_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_type(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_typeContext,0)


        def attribute_names(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_namesContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutable_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutable_attribute_decl" ):
                return visitor.visitImmutable_attribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def immutable_attribute_decl(self):

        localctx = BKOOLParser.Immutable_attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_immutable_attribute_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 161
                    self.match(BKOOLParser.STATIC)


                self.state = 164
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 165
                self.match(BKOOLParser.FINAL)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 166
                    self.match(BKOOLParser.STATIC)


                pass


            self.state = 171
            self.attribute_type()
            self.state = 172
            self.attribute_names()
            self.state = 173
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_type" ):
                return visitor.visitAttribute_type(self)
            else:
                return visitor.visitChildren(self)




    def attribute_type(self):

        localctx = BKOOLParser.Attribute_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_type)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
                self.array_type()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 180
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_nameContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attribute_names(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_namesContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_names

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_names" ):
                return visitor.visitAttribute_names(self)
            else:
                return visitor.visitChildren(self)




    def attribute_names(self):

        localctx = BKOOLParser.Attribute_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attribute_names)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.attribute_name()
                self.state = 184
                self.match(BKOOLParser.COMMA)
                self.state = 185
                self.attribute_names()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.attribute_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = BKOOLParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute_name)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.match(BKOOLParser.ID)
                self.state = 192
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 193
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_method(self):
            return self.getTypedRuleContext(BKOOLParser.Normal_methodContext,0)


        def main_method(self):
            return self.getTypedRuleContext(BKOOLParser.Main_methodContext,0)


        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_method_decl)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.normal_method()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.main_method()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(BKOOLParser.Return_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_normal_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_method" ):
                return visitor.visitNormal_method(self)
            else:
                return visitor.visitChildren(self)




    def normal_method(self):

        localctx = BKOOLParser.Normal_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_normal_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 201
                self.match(BKOOLParser.STATIC)


            self.state = 204
            self.return_type()
            self.state = 205
            self.match(BKOOLParser.ID)
            self.state = 206
            self.match(BKOOLParser.LB)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 207
                self.params()


            self.state = 210
            self.match(BKOOLParser.RB)
            self.state = 211
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_main_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_method" ):
                return visitor.visitMain_method(self)
            else:
                return visitor.visitChildren(self)




    def main_method(self):

        localctx = BKOOLParser.Main_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_main_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(BKOOLParser.VOID)
            self.state = 214
            self.match(BKOOLParser.T__0)
            self.state = 215
            self.match(BKOOLParser.LB)
            self.state = 216
            self.match(BKOOLParser.RB)
            self.state = 217
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(BKOOLParser.ID)
            self.state = 220
            self.match(BKOOLParser.LB)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 221
                self.params()


            self.state = 224
            self.match(BKOOLParser.RB)
            self.state = 225
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = BKOOLParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_return_type)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 230
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 231
                self.match(BKOOLParser.VOID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 232
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 233
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 236
                self.param()
                self.state = 237
                self.match(BKOOLParser.SEMI)
                self.state = 238
                self.params()
                pass

            elif la_ == 2:
                self.state = 240
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_type(self):
            return self.getTypedRuleContext(BKOOLParser.Param_typeContext,0)


        def comma_sep_ids(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_idsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.param_type()
            self.state = 244
            self.comma_sep_ids()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_type" ):
                return visitor.visitParam_type(self)
            else:
                return visitor.visitChildren(self)




    def param_type(self):

        localctx = BKOOLParser.Param_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_sep_idsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def comma_sep_ids(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_idsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_comma_sep_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_sep_ids" ):
                return visitor.visitComma_sep_ids(self)
            else:
                return visitor.visitChildren(self)




    def comma_sep_ids(self):

        localctx = BKOOLParser.Comma_sep_idsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comma_sep_ids)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(BKOOLParser.ID)
                self.state = 249
                self.match(BKOOLParser.COMMA)
                self.state = 250
                self.comma_sep_ids()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = BKOOLParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def comma_sep_array_elmts(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_array_elmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(BKOOLParser.LP)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT))) != 0):
                self.state = 257
                self.comma_sep_array_elmts()


            self.state = 260
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_sep_array_elmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elmt(self):
            return self.getTypedRuleContext(BKOOLParser.ElmtContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def comma_sep_array_elmts(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_array_elmtsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_comma_sep_array_elmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_sep_array_elmts" ):
                return visitor.visitComma_sep_array_elmts(self)
            else:
                return visitor.visitChildren(self)




    def comma_sep_array_elmts(self):

        localctx = BKOOLParser.Comma_sep_array_elmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comma_sep_array_elmts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 262
                self.elmt()
                self.state = 263
                self.match(BKOOLParser.COMMA)
                self.state = 264
                self.comma_sep_array_elmts()
                pass

            elif la_ == 2:
                self.state = 266
                self.elmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_litContext,0)


        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_elmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElmt" ):
                return visitor.visitElmt(self)
            else:
                return visitor.visitChildren(self)




    def elmt(self):

        localctx = BKOOLParser.ElmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elmt)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.match(BKOOLParser.STRING_LIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_int_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_type" ):
                return visitor.visitInt_type(self)
            else:
                return visitor.visitChildren(self)




    def int_type(self):

        localctx = BKOOLParser.Int_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_int_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(BKOOLParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_float_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_type" ):
                return visitor.visitFloat_type(self)
            else:
                return visitor.visitChildren(self)




    def float_type(self):

        localctx = BKOOLParser.Float_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_float_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(BKOOLParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_type" ):
                return visitor.visitBool_type(self)
            else:
                return visitor.visitChildren(self)




    def bool_type(self):

        localctx = BKOOLParser.Bool_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_bool_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(BKOOLParser.BOOLEAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_string_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_type" ):
                return visitor.visitString_type(self)
            else:
                return visitor.visitChildren(self)




    def string_type(self):

        localctx = BKOOLParser.String_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_string_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKOOLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Void_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_void_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoid_type" ):
                return visitor.visitVoid_type(self)
            else:
                return visitor.visitChildren(self)




    def void_type(self):

        localctx = BKOOLParser.Void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BKOOLParser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 286
            self.match(BKOOLParser.LSB)
            self.state = 287
            self.match(BKOOLParser.INT_LIT)
            self.state = 288
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Equality_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Equality_exprContext,i)


        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(BKOOLParser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(BKOOLParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.equality_expr()
                self.state = 291
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_OR_EQUAL) | (1 << BKOOLParser.GREATER_OR_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 292
                self.equality_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.equality_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equality_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Boolean_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Boolean_exprContext,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_equality_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_expr" ):
                return visitor.visitEquality_expr(self)
            else:
                return visitor.visitChildren(self)




    def equality_expr(self):

        localctx = BKOOLParser.Equality_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_equality_expr)
        self._la = 0 # Token type
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.boolean_expr(0)
                self.state = 298
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NOT_EQUAL or _la==BKOOLParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 299
                self.boolean_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.boolean_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bin_additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Bin_additive_exprContext,0)


        def boolean_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Boolean_exprContext,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_boolean_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expr" ):
                return visitor.visitBoolean_expr(self)
            else:
                return visitor.visitChildren(self)



    def boolean_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Boolean_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_boolean_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.bin_additive_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Boolean_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expr)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.bin_additive_expr(0) 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Bin_additive_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiplicative_exprContext,0)


        def bin_additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Bin_additive_exprContext,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bin_additive_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_additive_expr" ):
                return visitor.visitBin_additive_expr(self)
            else:
                return visitor.visitChildren(self)



    def bin_additive_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Bin_additive_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_bin_additive_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.multiplicative_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Bin_additive_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bin_additive_expr)
                    self.state = 318
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 319
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 320
                    self.multiplicative_expr(0) 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplicative_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatenation_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Concatenation_exprContext,0)


        def multiplicative_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiplicative_exprContext,0)


        def MULOP(self):
            return self.getToken(BKOOLParser.MULOP, 0)

        def I_DIV(self):
            return self.getToken(BKOOLParser.I_DIV, 0)

        def F_DIV(self):
            return self.getToken(BKOOLParser.F_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_multiplicative_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expr" ):
                return visitor.visitMultiplicative_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Multiplicative_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_multiplicative_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.concatenation_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Multiplicative_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expr)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULOP) | (1 << BKOOLParser.I_DIV) | (1 << BKOOLParser.F_DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 331
                    self.concatenation_expr(0) 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Concatenation_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Not_exprContext,0)


        def concatenation_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Concatenation_exprContext,0)


        def CONCATENATION(self):
            return self.getToken(BKOOLParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_concatenation_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatenation_expr" ):
                return visitor.visitConcatenation_expr(self)
            else:
                return visitor.visitChildren(self)



    def concatenation_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Concatenation_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_concatenation_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Concatenation_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_concatenation_expr)
                    self.state = 340
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 341
                    self.match(BKOOLParser.CONCATENATION)
                    self.state = 342
                    self.not_expr() 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def not_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Not_exprContext,0)


        def u_additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.U_additive_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_not_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_expr" ):
                return visitor.visitNot_expr(self)
            else:
                return visitor.visitChildren(self)




    def not_expr(self):

        localctx = BKOOLParser.Not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_not_expr)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(BKOOLParser.NOT)
                self.state = 349
                self.not_expr()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.ADDOP, BKOOLParser.SUBOP, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.u_additive_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class U_additive_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def u_additive_expr(self):
            return self.getTypedRuleContext(BKOOLParser.U_additive_exprContext,0)


        def ADDOP(self):
            return self.getToken(BKOOLParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(BKOOLParser.SUBOP, 0)

        def idx_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Idx_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_u_additive_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitU_additive_expr" ):
                return visitor.visitU_additive_expr(self)
            else:
                return visitor.visitChildren(self)




    def u_additive_expr(self):

        localctx = BKOOLParser.U_additive_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_u_additive_expr)
        self._la = 0 # Token type
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADDOP, BKOOLParser.SUBOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADDOP or _la==BKOOLParser.SUBOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 354
                self.u_additive_expr()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.idx_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Access_exprContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_idx_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_expr" ):
                return visitor.visitIdx_expr(self)
            else:
                return visitor.visitChildren(self)




    def idx_expr(self):

        localctx = BKOOLParser.Idx_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_idx_expr)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.access_expr(0)
                self.state = 359
                self.match(BKOOLParser.LSB)
                self.state = 360
                self.expr()
                self.state = 361
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.access_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def new_expr(self):
            return self.getTypedRuleContext(BKOOLParser.New_exprContext,0)


        def access_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Access_exprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def comma_sep_exprs(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_exprsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_access_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_expr" ):
                return visitor.visitAccess_expr(self)
            else:
                return visitor.visitChildren(self)



    def access_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Access_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_access_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.new_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Access_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_access_expr)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    self.match(BKOOLParser.DOT)
                    self.state = 371
                    self.match(BKOOLParser.ID)
                    self.state = 377
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        self.state = 372
                        self.match(BKOOLParser.LB)
                        self.state = 374
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT))) != 0):
                            self.state = 373
                            self.comma_sep_exprs()


                        self.state = 376
                        self.match(BKOOLParser.RB)

             
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class New_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def new_expr(self):
            return self.getTypedRuleContext(BKOOLParser.New_exprContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def comma_sep_exprs(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_exprsContext,0)


        def simple_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Simple_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_new_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_expr" ):
                return visitor.visitNew_expr(self)
            else:
                return visitor.visitChildren(self)




    def new_expr(self):

        localctx = BKOOLParser.New_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_new_expr)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(BKOOLParser.NEW)
                self.state = 385
                self.new_expr()
                self.state = 386
                self.match(BKOOLParser.LB)
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT))) != 0):
                    self.state = 387
                    self.comma_sep_exprs()


                self.state = 390
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB, BKOOLParser.ID, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.simple_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(BKOOLParser.AtomContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_simple_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_expr" ):
                return visitor.visitSimple_expr(self)
            else:
                return visitor.visitChildren(self)




    def simple_expr(self):

        localctx = BKOOLParser.Simple_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_simple_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = BKOOLParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_atom)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.LP, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.literal()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.match(BKOOLParser.LB)
                self.state = 401
                self.expr()
                self.state = 402
                self.match(BKOOLParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_litContext,0)


        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 409
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 410
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_sep_exprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def comma_sep_exprs(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_exprsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_comma_sep_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma_sep_exprs" ):
                return visitor.visitComma_sep_exprs(self)
            else:
                return visitor.visitChildren(self)




    def comma_sep_exprs(self):

        localctx = BKOOLParser.Comma_sep_exprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_comma_sep_exprs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 413
                self.expr()
                self.state = 414
                self.match(BKOOLParser.COMMA)
                self.state = 415
                self.comma_sep_exprs()
                pass

            elif la_ == 2:
                self.state = 417
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def method_invoc_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoc_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmt)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 422
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 423
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 424
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 425
                self.return_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 426
                self.method_invoc_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 427
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(BKOOLParser.LP)
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT))) != 0):
                self.state = 433
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 431
                    self.var_decl()
                    pass

                elif la_ == 2:
                    self.state = 432
                    self.stmt()
                    pass


                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 438
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_type(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_typeContext,0)


        def attribute_names(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_namesContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 440
                self.match(BKOOLParser.FINAL)


            self.state = 443
            self.attribute_type()
            self.state = 444
            self.attribute_names()
            self.state = 445
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.lhs()
            self.state = 448
            self.match(BKOOLParser.ASSIGN)
            self.state = 449
            self.expr()
            self.state = 450
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutable_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Mutable_exprContext,0)


        def array_ele(self):
            return self.getTypedRuleContext(BKOOLParser.Array_eleContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_lhs)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.mutable_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.array_ele()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mutable_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutable_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable_expr" ):
                return visitor.visitMutable_expr(self)
            else:
                return visitor.visitChildren(self)




    def mutable_expr(self):

        localctx = BKOOLParser.Mutable_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_mutable_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 458
            self.match(BKOOLParser.DOT)
            self.state = 459
            self.match(BKOOLParser.ID)
            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.LSB:
                self.state = 460
                self.match(BKOOLParser.LSB)
                self.state = 461
                self.expr()
                self.state = 462
                self.match(BKOOLParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_ele" ):
                return visitor.visitArray_ele(self)
            else:
                return visitor.visitChildren(self)




    def array_ele(self):

        localctx = BKOOLParser.Array_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_array_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(BKOOLParser.ID)
            self.state = 467
            self.match(BKOOLParser.LSB)
            self.state = 468
            self.expr()
            self.state = 469
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(BKOOLParser.IF)
            self.state = 472
            self.expr()
            self.state = 473
            self.match(BKOOLParser.THEN)
            self.state = 474
            self.stmt()
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 475
                self.match(BKOOLParser.ELSE)
                self.state = 476
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def for_range(self):
            return self.getTypedRuleContext(BKOOLParser.For_rangeContext,0)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(BKOOLParser.FOR)
            self.state = 480
            self.match(BKOOLParser.ID)
            self.state = 481
            self.match(BKOOLParser.ASSIGN)
            self.state = 482
            self.for_range()
            self.state = 483
            self.match(BKOOLParser.DO)
            self.state = 484
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_val(self):
            return self.getTypedRuleContext(BKOOLParser.Init_valContext,0)


        def final_val(self):
            return self.getTypedRuleContext(BKOOLParser.Final_valContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = BKOOLParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_for_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.init_val()
            self.state = 487
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 488
            self.final_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_init_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_val" ):
                return visitor.visitInit_val(self)
            else:
                return visitor.visitChildren(self)




    def init_val(self):

        localctx = BKOOLParser.Init_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_init_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Final_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_final_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinal_val" ):
                return visitor.visitFinal_val(self)
            else:
                return visitor.visitChildren(self)




    def final_val(self):

        localctx = BKOOLParser.Final_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_final_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(BKOOLParser.BREAK)
            self.state = 495
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(BKOOLParser.CONTINUE)
            self.state = 498
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(BKOOLParser.RETURN)
            self.state = 501
            self.expr()
            self.state = 502
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoc_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def comma_sep_exprs(self):
            return self.getTypedRuleContext(BKOOLParser.Comma_sep_exprsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invoc_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invoc_stmt" ):
                return visitor.visitMethod_invoc_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invoc_stmt(self):

        localctx = BKOOLParser.Method_invoc_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_method_invoc_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.expr()
            self.state = 505
            self.match(BKOOLParser.DOT)
            self.state = 506
            self.match(BKOOLParser.ID)
            self.state = 507
            self.match(BKOOLParser.LB)
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.NEW) | (1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADDOP) | (1 << BKOOLParser.SUBOP) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT))) != 0):
                self.state = 508
                self.comma_sep_exprs()


            self.state = 511
            self.match(BKOOLParser.RB)
            self.state = 512
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.boolean_expr_sempred
        self._predicates[33] = self.bin_additive_expr_sempred
        self._predicates[34] = self.multiplicative_expr_sempred
        self._predicates[35] = self.concatenation_expr_sempred
        self._predicates[39] = self.access_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolean_expr_sempred(self, localctx:Boolean_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def bin_additive_expr_sempred(self, localctx:Bin_additive_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplicative_expr_sempred(self, localctx:Multiplicative_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def concatenation_expr_sempred(self, localctx:Concatenation_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def access_expr_sempred(self, localctx:Access_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




