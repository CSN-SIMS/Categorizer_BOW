from unittest import TestCase

from BagOfWords import createVectorsFromArrayWithHashmaps, hashmapWordOccurency, loadingFilesIntoArray


class TestCreateVectorsFromArrayWithHashmaps(TestCase):
    def test_createVectorsFromArrayWithHashmaps(self):
        self.assertEqual(createVectorsFromArrayWithHashmaps(
            [{'boy': 2, 'flower': 0, 'footbal': 1, 'garden': 1, 'grow': 0, 'mani': 0, 'play': 1},
             {'boy': 0, 'flower': 1, 'footbal': 0, 'garden': 1, 'grow': 1, 'mani': 1, 'play': 0}]),
            [[2, 0, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 1, 0]])