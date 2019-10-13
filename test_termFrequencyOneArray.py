from unittest import TestCase

from BagOfWords import TermFrequencyOneArray


class TestTermFrequencyOneArray(TestCase):
    def test_TermFrequencyOneArray(self):
        self.assertAlmostEqual(TermFrequencyOneArray([2, 0, 0, 1, 5, 0, 0, 3]), [2.0, 0, 0, 1.0, 3.321928094887362, 0, 0, 2.584962500721156])
