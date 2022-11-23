# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\7\3\u008d\n\3\f\3\16\3\u0090\13")
        buf.write("\3\3\3\5\3\u0093\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7")
        buf.write("\4\u009d\n\4\f\4\16\4\u00a0\13\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\7")
        buf.write("9\u016d\n9\f9\169\u0170\139\3:\6:\u0173\n:\r:\16:\u0174")
        buf.write("\3;\6;\u0178\n;\r;\16;\u0179\3;\3;\7;\u017e\n;\f;\16;")
        buf.write("\u0181\13;\3;\5;\u0184\n;\3;\5;\u0187\n;\3<\3<\5<\u018b")
        buf.write("\n<\3<\6<\u018e\n<\r<\16<\u018f\3=\3=\7=\u0194\n=\f=\16")
        buf.write("=\u0197\13=\3=\3=\3>\3>\3>\5>\u019e\n>\3?\3?\3?\3?\3@")
        buf.write("\3@\7@\u01a6\n@\f@\16@\u01a9\13@\3@\3@\5@\u01ad\n@\3@")
        buf.write("\3@\3A\3A\7A\u01b3\nA\fA\16A\u01b6\13A\3A\3A\3A\5A\u01bb")
        buf.write("\nA\3A\3A\3B\3B\3B\3\u009e\2C\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\64g\65i\66k\67m8o9q:s;u<w\2y={\2}>\177?\u0081@\u0083")
        buf.write("A\3\2\16\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\t\2$$^^ddhhppttvv\6\2\f\f\17\17$$^^")
        buf.write("\5\2\13\f\16\17\"\"\6\2\f\f\17\17GHQQ\3\2$$\3\2^^\2\u01cf")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2")
        buf.write("\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3")
        buf.write("\2\2\2\5\u008a\3\2\2\2\7\u0098\3\2\2\2\t\u00a6\3\2\2\2")
        buf.write("\13\u00ae\3\2\2\2\r\u00b4\3\2\2\2\17\u00ba\3\2\2\2\21")
        buf.write("\u00c3\3\2\2\2\23\u00c6\3\2\2\2\25\u00cb\3\2\2\2\27\u00d3")
        buf.write("\3\2\2\2\31\u00d9\3\2\2\2\33\u00dc\3\2\2\2\35\u00e0\3")
        buf.write("\2\2\2\37\u00e4\3\2\2\2!\u00eb\3\2\2\2#\u00f0\3\2\2\2")
        buf.write("%\u00f4\3\2\2\2\'\u00fb\3\2\2\2)\u0100\3\2\2\2+\u0106")
        buf.write("\3\2\2\2-\u010b\3\2\2\2/\u010f\3\2\2\2\61\u0114\3\2\2")
        buf.write("\2\63\u011a\3\2\2\2\65\u0121\3\2\2\2\67\u0124\3\2\2\2")
        buf.write("9\u012b\3\2\2\2;\u012d\3\2\2\2=\u012f\3\2\2\2?\u0131\3")
        buf.write("\2\2\2A\u0133\3\2\2\2C\u0135\3\2\2\2E\u0137\3\2\2\2G\u013a")
        buf.write("\3\2\2\2I\u013d\3\2\2\2K\u013f\3\2\2\2M\u0141\3\2\2\2")
        buf.write("O\u0144\3\2\2\2Q\u0147\3\2\2\2S\u014a\3\2\2\2U\u014d\3")
        buf.write("\2\2\2W\u014f\3\2\2\2Y\u0151\3\2\2\2[\u0154\3\2\2\2]\u0156")
        buf.write("\3\2\2\2_\u0158\3\2\2\2a\u015a\3\2\2\2c\u015c\3\2\2\2")
        buf.write("e\u015e\3\2\2\2g\u0160\3\2\2\2i\u0162\3\2\2\2k\u0164\3")
        buf.write("\2\2\2m\u0166\3\2\2\2o\u0168\3\2\2\2q\u016a\3\2\2\2s\u0172")
        buf.write("\3\2\2\2u\u0177\3\2\2\2w\u0188\3\2\2\2y\u0191\3\2\2\2")
        buf.write("{\u019d\3\2\2\2}\u019f\3\2\2\2\177\u01a3\3\2\2\2\u0081")
        buf.write("\u01b0\3\2\2\2\u0083\u01be\3\2\2\2\u0085\u0086\7o\2\2")
        buf.write("\u0086\u0087\7c\2\2\u0087\u0088\7k\2\2\u0088\u0089\7p")
        buf.write("\2\2\u0089\4\3\2\2\2\u008a\u008e\7%\2\2\u008b\u008d\n")
        buf.write("\2\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0092\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0091\u0093\7\17\2\2\u0092\u0091\3\2\2")
        buf.write("\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\7\f\2\2\u0095\u0096\3\2\2\2\u0096\u0097\b\3\2\2\u0097")
        buf.write("\6\3\2\2\2\u0098\u0099\7\61\2\2\u0099\u009a\7,\2\2\u009a")
        buf.write("\u009e\3\2\2\2\u009b\u009d\13\2\2\2\u009c\u009b\3\2\2")
        buf.write("\2\u009d\u00a0\3\2\2\2\u009e\u009f\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a2\7,\2\2\u00a2\u00a3\7\61\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a5\b\4\2\2\u00a5\b\3\2\2\2\u00a6\u00a7\7d\2")
        buf.write("\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7")
        buf.write("n\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\n\3\2\2\2\u00ae\u00af\7d\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7m\2\2\u00b3\f\3\2\2\2\u00b4\u00b5\7e\2\2\u00b5\u00b6")
        buf.write("\7n\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7u\2\2\u00b9\16\3\2\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\20\3\2\2\2\u00c3\u00c4\7f\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\22\3\2\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca\24")
        buf.write("\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7z\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7f\2\2\u00d1\u00d2\7u\2\2\u00d2\26\3\2\2\2\u00d3\u00d4")
        buf.write("\7h\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7v\2\2\u00d8\30\3\2\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7h\2\2\u00db\32\3\2\2\2\u00dc\u00dd")
        buf.write("\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7v\2\2\u00df\34")
        buf.write("\3\2\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3")
        buf.write("\7y\2\2\u00e3\36\3\2\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7i\2\2\u00ea \3\2\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec\u00ed\7j\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\"\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7t\2\2\u00f3$\3\2\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7p\2\2\u00fa&\3")
        buf.write("\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe")
        buf.write("\7w\2\2\u00fe\u00ff\7g\2\2\u00ff(\3\2\2\2\u0100\u0101")
        buf.write("\7h\2\2\u0101\u0102\7c\2\2\u0102\u0103\7n\2\2\u0103\u0104")
        buf.write("\7u\2\2\u0104\u0105\7g\2\2\u0105*\3\2\2\2\u0106\u0107")
        buf.write("\7x\2\2\u0107\u0108\7q\2\2\u0108\u0109\7k\2\2\u0109\u010a")
        buf.write("\7f\2\2\u010a,\3\2\2\2\u010b\u010c\7p\2\2\u010c\u010d")
        buf.write("\7k\2\2\u010d\u010e\7n\2\2\u010e.\3\2\2\2\u010f\u0110")
        buf.write("\7v\2\2\u0110\u0111\7j\2\2\u0111\u0112\7k\2\2\u0112\u0113")
        buf.write("\7u\2\2\u0113\60\3\2\2\2\u0114\u0115\7h\2\2\u0115\u0116")
        buf.write("\7k\2\2\u0116\u0117\7p\2\2\u0117\u0118\7c\2\2\u0118\u0119")
        buf.write("\7n\2\2\u0119\62\3\2\2\2\u011a\u011b\7u\2\2\u011b\u011c")
        buf.write("\7v\2\2\u011c\u011d\7c\2\2\u011d\u011e\7v\2\2\u011e\u011f")
        buf.write("\7k\2\2\u011f\u0120\7e\2\2\u0120\64\3\2\2\2\u0121\u0122")
        buf.write("\7v\2\2\u0122\u0123\7q\2\2\u0123\66\3\2\2\2\u0124\u0125")
        buf.write("\7f\2\2\u0125\u0126\7q\2\2\u0126\u0127\7y\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7v\2\2\u0129\u012a\7q\2\2\u012a8\3")
        buf.write("\2\2\2\u012b\u012c\7-\2\2\u012c:\3\2\2\2\u012d\u012e\7")
        buf.write("/\2\2\u012e<\3\2\2\2\u012f\u0130\7,\2\2\u0130>\3\2\2\2")
        buf.write("\u0131\u0132\7\61\2\2\u0132@\3\2\2\2\u0133\u0134\7^\2")
        buf.write("\2\u0134B\3\2\2\2\u0135\u0136\7\'\2\2\u0136D\3\2\2\2\u0137")
        buf.write("\u0138\7#\2\2\u0138\u0139\7?\2\2\u0139F\3\2\2\2\u013a")
        buf.write("\u013b\7?\2\2\u013b\u013c\7?\2\2\u013cH\3\2\2\2\u013d")
        buf.write("\u013e\7>\2\2\u013eJ\3\2\2\2\u013f\u0140\7@\2\2\u0140")
        buf.write("L\3\2\2\2\u0141\u0142\7>\2\2\u0142\u0143\7?\2\2\u0143")
        buf.write("N\3\2\2\2\u0144\u0145\7@\2\2\u0145\u0146\7?\2\2\u0146")
        buf.write("P\3\2\2\2\u0147\u0148\7~\2\2\u0148\u0149\7~\2\2\u0149")
        buf.write("R\3\2\2\2\u014a\u014b\7(\2\2\u014b\u014c\7(\2\2\u014c")
        buf.write("T\3\2\2\2\u014d\u014e\7#\2\2\u014eV\3\2\2\2\u014f\u0150")
        buf.write("\7`\2\2\u0150X\3\2\2\2\u0151\u0152\7<\2\2\u0152\u0153")
        buf.write("\7?\2\2\u0153Z\3\2\2\2\u0154\u0155\7?\2\2\u0155\\\3\2")
        buf.write("\2\2\u0156\u0157\7]\2\2\u0157^\3\2\2\2\u0158\u0159\7_")
        buf.write("\2\2\u0159`\3\2\2\2\u015a\u015b\7}\2\2\u015bb\3\2\2\2")
        buf.write("\u015c\u015d\7\177\2\2\u015dd\3\2\2\2\u015e\u015f\7*\2")
        buf.write("\2\u015ff\3\2\2\2\u0160\u0161\7+\2\2\u0161h\3\2\2\2\u0162")
        buf.write("\u0163\7=\2\2\u0163j\3\2\2\2\u0164\u0165\7<\2\2\u0165")
        buf.write("l\3\2\2\2\u0166\u0167\7\60\2\2\u0167n\3\2\2\2\u0168\u0169")
        buf.write("\7.\2\2\u0169p\3\2\2\2\u016a\u016e\t\3\2\2\u016b\u016d")
        buf.write("\t\4\2\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016fr\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0171\u0173\t\5\2\2\u0172\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175t\3\2\2\2\u0176\u0178\t\5\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u0186\3\2\2\2\u017b\u017f\7\60\2")
        buf.write("\2\u017c\u017e\t\5\2\2\u017d\u017c\3\2\2\2\u017e\u0181")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0184\5w<\2\u0183")
        buf.write("\u0182\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0187\3\2\2\2")
        buf.write("\u0185\u0187\5w<\2\u0186\u017b\3\2\2\2\u0186\u0185\3\2")
        buf.write("\2\2\u0187v\3\2\2\2\u0188\u018a\t\6\2\2\u0189\u018b\t")
        buf.write("\7\2\2\u018a\u0189\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d")
        buf.write("\3\2\2\2\u018c\u018e\t\5\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190x\3\2\2\2\u0191\u0195\7$\2\2\u0192\u0194\5{>\2\u0193")
        buf.write("\u0192\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3")
        buf.write("\2\2\2\u0198\u0199\7$\2\2\u0199z\3\2\2\2\u019a\u019b\7")
        buf.write("^\2\2\u019b\u019e\t\b\2\2\u019c\u019e\n\t\2\2\u019d\u019a")
        buf.write("\3\2\2\2\u019d\u019c\3\2\2\2\u019e|\3\2\2\2\u019f\u01a0")
        buf.write("\t\n\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\b?\2\2\u01a2")
        buf.write("~\3\2\2\2\u01a3\u01a7\7$\2\2\u01a4\u01a6\5{>\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a8\3\2\2\2\u01a8\u01ac\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01aa\u01ad\t\13\2\2\u01ab\u01ad\n\f\2\2\u01ac\u01aa")
        buf.write("\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01af\b@\3\2\u01af\u0080\3\2\2\2\u01b0\u01b4\7$\2\2\u01b1")
        buf.write("\u01b3\5{>\2\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01ba\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b7\u01b8\7^\2\2\u01b8\u01bb\n")
        buf.write("\b\2\2\u01b9\u01bb\n\r\2\2\u01ba\u01b7\3\2\2\2\u01ba\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\bA\4\2\u01bd")
        buf.write("\u0082\3\2\2\2\u01be\u01bf\13\2\2\2\u01bf\u01c0\bB\5\2")
        buf.write("\u01c0\u0084\3\2\2\2\24\2\u008e\u0092\u009e\u016e\u0174")
        buf.write("\u0179\u017f\u0183\u0186\u018a\u018f\u0195\u019d\u01a7")
        buf.write("\u01ac\u01b4\u01ba\6\b\2\2\3@\2\3A\3\3B\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT_LINE = 2
    COMMENT_BLOCK = 3
    BOOLEAN = 4
    BREAK = 5
    CLASS = 6
    CONTINUE = 7
    DO = 8
    ELSE = 9
    EXTENDS = 10
    FLOAT = 11
    IF = 12
    INT = 13
    NEW = 14
    STRING = 15
    THEN = 16
    FOR = 17
    RETURN = 18
    TRUE = 19
    FALSE = 20
    VOID = 21
    NIL = 22
    THIS = 23
    FINAL = 24
    STATIC = 25
    TO = 26
    DOWNTO = 27
    ADDOP = 28
    SUBOP = 29
    MULOP = 30
    I_DIV = 31
    F_DIV = 32
    MOD = 33
    NOT_EQUAL = 34
    EQUAL = 35
    LESS = 36
    GREATER = 37
    LESS_OR_EQUAL = 38
    GREATER_OR_EQUAL = 39
    OR = 40
    AND = 41
    NOT = 42
    CONCATENATION = 43
    ASSIGN = 44
    EQUAL_SIGN = 45
    LSB = 46
    RSB = 47
    LP = 48
    RP = 49
    LB = 50
    RB = 51
    SEMI = 52
    COLON = 53
    DOT = 54
    COMMA = 55
    ID = 56
    INT_LIT = 57
    FLOAT_LIT = 58
    STRING_LIT = 59
    WS = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'boolean'", "'break'", "'class'", "'continue'", "'do'", 
            "'else'", "'extends'", "'float'", "'if'", "'int'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
            "'^'", "':='", "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", 
            "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_LINE", "COMMENT_BLOCK", "BOOLEAN", "BREAK", "CLASS", 
            "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
            "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
            "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ADDOP", "SUBOP", 
            "MULOP", "I_DIV", "F_DIV", "MOD", "NOT_EQUAL", "EQUAL", "LESS", 
            "GREATER", "LESS_OR_EQUAL", "GREATER_OR_EQUAL", "OR", "AND", 
            "NOT", "CONCATENATION", "ASSIGN", "EQUAL_SIGN", "LSB", "RSB", 
            "LP", "RP", "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", "ID", 
            "INT_LIT", "FLOAT_LIT", "STRING_LIT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "COMMENT_LINE", "COMMENT_BLOCK", "BOOLEAN", "BREAK", 
                  "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", 
                  "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                  "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                  "TO", "DOWNTO", "ADDOP", "SUBOP", "MULOP", "I_DIV", "F_DIV", 
                  "MOD", "NOT_EQUAL", "EQUAL", "LESS", "GREATER", "LESS_OR_EQUAL", 
                  "GREATER_OR_EQUAL", "OR", "AND", "NOT", "CONCATENATION", 
                  "ASSIGN", "EQUAL_SIGN", "LSB", "RSB", "LP", "RP", "LB", 
                  "RB", "SEMI", "COLON", "DOT", "COMMA", "ID", "INT_LIT", 
                  "FLOAT_LIT", "EXPONENT", "STRING_LIT", "CHAR", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	err_char = ['\r','\n',EOFError]
            	if self.text[-1] in err_char:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise ErrorToken(self.text)

     


