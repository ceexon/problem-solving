import random

class Dice:
    def __init__(self, my_roll, sides = 6):
        self.my_roll = my_roll
        self.sides = sides

    def roll_die(self):
        sides = self.sides
        choice = 0
        number_of_rolls = 0
        start = 0
        print("""
        Welcome To The Dice Roll Game!!
        Hope you enjoy ---

        Here are your options:
        1)Roll Dice
        q)Quit
        """)
        while True:
            if self.my_roll == 0:
                return "You Did not Roll The Dice At All"
                
            choice = str(input("Please Select An Option: "))
            if not choice.isdigit():
                if choice == "q":
                    return "You Did not Roll The Dice At All"
                else:
                    print ("Please Select from the above choices")
                    continue
            else:
                choice = int(choice)
                if choice == 1:
                    rolled_list = []
                    while start < self.my_roll:
                        start+= 1
                        number_of_rolls += 1
                        die = sides
                        rolled = random.randint(1,die)
                        print ("""
                        Your Dice is rolling \n \n
                        ---------------------------------------------------------------
                        ---------------------------------------------------------------
                        ---------------------------------------------------------------
                        And........... \n \n
                        """)
                        print ("You got ", rolled, " in roll ", number_of_rolls ,rolled_list.append(str(rolled)))
                        again = str(input("\t\tWould like to roll again??\n \t\ty(yes to continue)\n\t\tany other key(to stop)): "))
                        if again == "yes" or again == "y":
                            continue
                        else:
                            print("""
                            See you again soon Friend!
                            Your always welcomed
                            """)
                            if len(rolled_list) > 1:
                                return rolled_list

                            else:
                                return rolled_list
                    else:
                        return rolled_list

                elif choice != 1 or choice < 0:
                    print ("Please Select from the above choices")
                    continue
