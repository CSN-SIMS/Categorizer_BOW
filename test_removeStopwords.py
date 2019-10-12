from unittest import TestCase
from BagOfWords import *

class TestRemoveStopwordsLowerCase(TestCase):
    def test_removeStopwords(self):
        self.assertEqual(removeStopwordsLowerCase(['Test', 'the']), ['test'])
