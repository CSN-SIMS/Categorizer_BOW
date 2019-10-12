from unittest import TestCase

from BagOfWords import sortArray


class TestSortArray(TestCase):
    def test_sortStringArray(self):
        self.assertEqual(sortArray(['c','q','a','aa', 'A']), ['A','a','aa','c','q'])

   # def test_sortmixArray(self):
    #    self.assertRaises(TypeError, sortArray(['c','q','a',2,'aa', 'A',1] ))
