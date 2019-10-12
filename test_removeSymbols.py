from unittest import TestCase

from BagOfWords import removeSymbols


class TestRemoveSymbols(TestCase):
    def test_removeSymbols(self):
        arrayOfString = ['.','String','!', 'Hello!', ',', '?', '!!','??']
        self.assertListEqual(removeSymbols(arrayOfString),['String', 'Hello!'])
       # self.assertRaises(TypeError, list)
        #self.assertRaises(ValueError, int)
