import unittest
from pass_ver import Password

class TestPassword(unittest.TestCase):

    def setUp(self):
        global Password
        ret_value = 0
        global Passd,Passd1,Passd2,Passd3,Passd4,Passd5,Passd6
        Passd = Password("**BKco$53")
        Passd1 = Password("BK#Ddd")
        Passd2 = Password("BK@DD545")
        Passd3 = Password("BK$DD545".lower())
        Passd4 = Password("TRevo123")
        Passd5 = Password("Tr3$")
        Passd6 = Password("Tr3$jd63jj3jjs7")

    def tearDown(self):
        # print ("Passed This Test")
        pass

    def test_check_for_int(self):
        self.assertTrue(Passd.check_for_int())
        self.assertTrue(Passd2.check_for_int())
        self.assertTrue(Passd3.check_for_int())
        self.assertTrue(Passd4.check_for_int())
        self.assertTrue(Passd5.check_for_int())
        self.assertTrue(Passd6.check_for_int())

        with self.assertRaises(ValueError):
            Passd1.check_for_int()

    def test_check_for_lower(self):
        self.assertTrue(Passd.check_for_lower())
        self.assertTrue(Passd1.check_for_lower())
        self.assertTrue(Passd3.check_for_lower())
        self.assertTrue(Passd4.check_for_lower())

        with self.assertRaises(ValueError):
            Passd2.check_for_lower()

    def test_check_for_upper(self):
        self.assertTrue(Passd.check_for_upper())
        self.assertTrue(Passd1.check_for_upper())
        self.assertTrue(Passd2.check_for_upper())
        self.assertTrue(Passd4.check_for_upper())
        self.assertTrue(Passd5.check_for_upper())
        self.assertTrue(Passd6.check_for_upper())

        with self.assertRaises(ValueError):
            Passd3.check_for_upper()

    def test_check_for_characters(self):
        self.assertTrue(Passd.check_for_characters())
        self.assertTrue(Passd1.check_for_characters())
        self.assertTrue(Passd2.check_for_characters())
        self.assertTrue(Passd3.check_for_characters())
        self.assertTrue(Passd5.check_for_characters())
        self.assertTrue(Passd6.check_for_characters())

        with self.assertRaises(ValueError):
            Passd4.check_for_characters()

    def test_check_for_pass_length(self):
        self.assertTrue(Passd.check_for_pass_lenght())
        self.assertTrue(Passd1.check_for_pass_lenght())
        self.assertTrue(Passd2.check_for_pass_lenght())
        self.assertTrue(Passd3.check_for_pass_lenght())
        self.assertTrue(Passd4.check_for_pass_lenght())

        with self.assertRaises(ValueError):
            Passd5.check_for_pass_lenght()
            Passd6.check_for_pass_lenght()

if __name__ == '__main__':
    unittest.main()
