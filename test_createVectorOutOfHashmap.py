from unittest import TestCase

from BagOfWords import createVectorOutOfHashmap


class TestCreateVectorOutOfHashmap(TestCase):
    def test_createVectorOutOfHashmap(self):
        self.assertEqual(createVectorOutOfHashmap({'word1': 4, 'word2': 2, 'word3': 0}), [4,2,0])
