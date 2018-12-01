import unittest
from dice_for_testing  import Dice
import random

class TstDice(unittest.TestCase):

    def setUp(self):
        global die_roll_1,die_roll_2,die_roll_3
        die_roll_1 = Dice(8,6)
        die_roll_2 = Dice(0,6)

        # die_roll_3 but user inputs q to quit so no roll
        die_roll_3 = Dice(4,6)

    def tearDown(self):
        pass

    def test_dice_roll(self):
        result = die_roll_1.roll_die()
        self.assertTrue(len(result) in range(9))

    def test_when_roll_0(self):
        result = die_roll_2.roll_die()
        self.assertEqual(result, "You Did not Roll The Dice At All")

    def test_when_select_q(self):
        result = die_roll_3.roll_die()
        self.assertEqual(result, "You Did not Roll The Dice At All")

if __name__ == '__main__':
    unittest.main()
