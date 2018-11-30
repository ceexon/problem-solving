import unittest
from palindromes import palind

class testPalindrome(unittest.TestCase):

    def test_palind_no_space(self):
        self.assertEqual(palind("madam"), "madam")
        self.assertEqual(palind("level"), "level")

    def test_palind_with_space(self):
        self.assertEqual(palind("nurses run"), "nurses run")
        self.assertEqual(palind("less ssel"), 'less ssel')
        self.assertEqual(palind("lesss sel"), 'lesss sel')
        self.assertEqual(palind("lesss sel"), 'lesss sel')

if __name__ == '__main__':
    unittest.main()
