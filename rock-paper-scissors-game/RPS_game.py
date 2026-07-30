# """This is a Rock Paper Game"""

import random

choices = ( "r" , "p" , "s" )

while True:
    user_choice = input("Enter your Choice ... r / p / s : ").lower()
    if user_choice not in choices:
        print("Invalid Choice..!")
        continue

    comp_choice = random.choice(choices)

    print(f'You choose {user_choice}')
    print(f'Computer choose {comp_choice}')

    if user_choice == comp_choice:
        print("Its an Draw...")
    elif (
        (user_choice == 'r' and comp_choice == 's') or
        (user_choice == 's' and comp_choice == 'p') or
        (user_choice == 'p' and comp_choice == 'r')):
        print("You Win This Round...")
    else:
        print("You Loss This Round...")
    play_again = input("Do You wanna Play Again.( y / n )... ! : ").lower()
    if play_again == "n":
        print("Thanks For Playing...")
        break
