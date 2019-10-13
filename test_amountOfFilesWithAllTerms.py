from unittest import TestCase

from BagOfWords import amountOfFilesWithAllTerms


class TestAmountOfFilesWithAllTerms(TestCase):
    def test_amountOfFilesWithAllTerms(self):
        self.assertEqual(
            amountOfFilesWithAllTerms(['boy', 'buy', 'flower', 'footbal', 'garden', 'grow', 'mani', 'play'],
                                      [{'boy': 2, 'buy': 0, 'flower': 0, 'footbal': 1, 'garden': 1, 'grow': 0,
                                        'mani': 0, 'play': 1},
                                       {'boy': 0, 'buy': 0, 'flower': 1, 'footbal': 0, 'garden': 1, 'grow': 1,
                                        'mani': 1, 'play': 0},
                                       {'boy': 1, 'buy': 1, 'flower': 0, 'footbal': 1, 'garden': 0, 'grow': 0,
                                        'mani': 2, 'play': 0}]),
            {'boy': 2, 'buy': 1, 'flower': 1, 'footbal': 2, 'garden': 2, 'grow': 1, 'mani': 2, 'play': 1})
