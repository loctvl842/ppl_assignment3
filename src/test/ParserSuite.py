import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1_attr_decl(self):
        """Test Attribute Declare 1 line 1 var"""
        input = r"""class test {}"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input, expect, 201))
