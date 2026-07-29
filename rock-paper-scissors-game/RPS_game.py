# """This is a Rock Paper Game"""
# import random

# choices = ( "r" , "p" , "s" )

# while True:
#     user_choice = input("Enter your Choice ... r / p / s : ").lower()
#     if user_choice not in choices:
#         print("Invalid Choice..!")
#         continue

#     comp_choice = random.choice(choices)

#     print(f'You choose {user_choice}')
#     print(f'Computer choose {comp_choice}')

#     if user_choice == comp_choice:
#         print("Its an Draw...")
#     elif (
#         (user_choice == 'r' and comp_choice == 's') or
#         (user_choice == 's' and comp_choice == 'p') or
#         (user_choice == 'p' and comp_choice == 'r')):
#         print("You Win This Round...")
#     else:
#         print("You Loss This Round...")
#     play_again = input("Do You wanna Play Again.( y / n )... ! : ").lower()
#     if play_again == "n":
#         print("Thanks For Playing...")
#         break


# import time 

# my_time = int(input("Enter the time in seconds : "))

# for i in range(my_time,0,-1):
#     time.sleep(1)
#     seconds =  i % 60
#     minutes = int((i / 60) % 60)
#     hours = int((i / 3600) % 60)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
        

# print("Happy Birthday to me!")



# import time, sys

# text = "Singing line in progress..."
# for i in range(len(text)):
#     print(text[:i+1], end='\r', flush=True)
#     time.sleep(0.05)
# print()  # move to new line after done
# import time
# import sys

# lyrics = [
#     ("Twinkle twinkle little star", 1.5),
#     ("How I wonder what you are", 1.5),
#     ("Up above the world so high", 1.5),
#     ("Like a diamond in the sky", 2)
# ]

# for line, delay in lyrics:
#     for char in line:
#         print(char, end='', flush=True)
#         time.sleep(0.09)   # smaller = faster typing, larger = slower typing
#     print()                # move to next line after full sentence
#     time.sleep(delay)      # pause before next lyric

