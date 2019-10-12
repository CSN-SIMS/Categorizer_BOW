from unittest import TestCase
from BagOfWords import *


class TestTokenize(TestCase):
    def test_tokenize(self):
        self.assertEqual(tokenize('My name is Tom!'), ['My', 'name', 'is', 'Tom', '!'])

