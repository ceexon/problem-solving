import random

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        choice = 0
        number_of_rolls = 0
        rolled_list = []
        print("""
        Welcome To The Dice Roll Game!!
        Hope you enjoy ---

        Here are your options:
        1)Roll Dice
        q)Quit
        """)
        choice = input("Please Select An Option: ")
        if choice == 1:
            while True:
                number_of_rolls += 1
                die = self.sides + 1
                rolled = random.randrange(1,die)
                print ("""
                Your Dice is rolling \n \n \n
                ---------------------------------------------------------------
                ---------------------------------------------------------------
                ---------------------------------------------------------------
                And........... \n
                """)
                print ("You got ", rolled, " in roll ", number_of_rolls)
                rolled_list.append(rolled)
                again = input("Would like to roll again??\n y(yes)/n(no): ")
                if again == "yes" or again == "y":
                    continue
                else:
                    print("""
                    See you again soon Friend!
                    Your always welcomed
                    """)

                    return "You rolled " + ','.join(rolled_list) + ' in ' + str(number_of_rolls) + ' rolls.'

        elif choice == 'q':
            return "Did not roll Dice"


roolit = Dice()
rest = roolit.roll_die()
print(rest)
