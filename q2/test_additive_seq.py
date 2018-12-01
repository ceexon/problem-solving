import unittest
from additive_seq import Additive

class TestAdditive(unittest.TestCase):
    def setUp(self):
        global addit,addit_not
        addit = Additive("6,6,12,18,30,48")
        addit_not = Additive("6,6,12,18,32,48")

    def tearDown(self):
        pass

    def test_additive_func(self):
        self.assertEqual(addit.additive_func(), "String is additive")
        self.assertEqual(addit_not.additive_func(), "String is not additive")

if __name__ == '__main__':
    unittest.main()
