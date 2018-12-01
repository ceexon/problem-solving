import random

def roll_die(sides):
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
    choice = int(input("Please Select An Option: "))
    if choice == 1:
        while True:
            number_of_rolls += 1
            die = sides
            rolled = random.randint(1,die)
            print ("""
            Your Dice is rolling \n \n \n
            ---------------------------------------------------------------
            ---------------------------------------------------------------
            ---------------------------------------------------------------
            And........... \n
            """)
            print ("You got ", rolled, " in roll ", number_of_rolls)
            rolled_list.append(rolled)
            again = str(input("Would like to roll again??\n y(yes)/n(no): "))
            if again == "yes" or again == "y":
                print( "\n\n\n\n\n\t\tshvkgsjhsjjhsh \t\t",)
            else:
                print("""
                See you again soon Friend!
                Your always welcomed
                """)

                values = ','.join(rolled_list)

                return "You rolled " + values + ' in ' + str(number_of_rolls) + ' rolls.'

    # elif choice == 'q':
    #     return "Did not roll Dice"


roll_die(6)
