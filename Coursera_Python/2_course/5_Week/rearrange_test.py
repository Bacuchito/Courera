from rearrange import rearrange_name
import unittest

class TeastRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEquals(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEquals(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        testcase = 'Victor'
        expected = 'Victor'
        self.assertEquals(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = 'Ronan, Juan M.'
        expected = 'Juan M. Ronan'
        self.assertEquals(rearrange_name(testcase), expected)

unittest.main()