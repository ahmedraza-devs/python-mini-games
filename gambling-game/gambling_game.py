# --------------Gambling Game-----------------

import random

def spin_row():
    symbols = ['🤖' , '👻' , '👽' , '👾' , '👹']

    return [random.choice(symbols) for _ in range(3)]
    

def print_row(row):
    
    print("*******************************")
    print("     |     ".join(row))
    print("*******************************\n")
    

def get_payout(row , bet):
   
    if row[0] == row[1] == row[2] :
        if row[0] == '🤖':
            return bet * 5
        elif row[0] == '👻':
            return bet * 8 
        elif row[0] == '👽':
            return bet * 12
        elif row[0] == '👾':
            return bet * 15
        elif row[0] == '👹':
            return bet * 30         
    return 0

def main():
    
    balance = 100

    print("*******************************")
    print("    Welcome to Gamble🤤🤑     ")
    print("*******************************")
    print("   Symbols 🤖 👻 👽 👾 👹   ")
    print("*******************************\n")

    while balance > 0 : 
        print(f"Current Balance is : €{balance:.2f}")
        print("*******************************")

        bet = input("Place your Bet Amount : ")

        if not bet.isdigit():
            print("Please enter a Valid Digit...")
            continue

        bet = int(bet)

        if bet > balance :
            print("Insufficient Funds...🥲")
            continue

        if bet <= 0 :
            print("Bet amount must be greater than 0...😒")

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
              
        print_row(row)
        
        payout = get_payout(row , bet)

        if payout > 0 :
            print(f"You Won🤑!...€{payout}")
        else:
            print("You lose this round...😞\n")

        balance += payout
        print(f"Your Remaining Balance is : €{balance:.2f}\n")

        play_again = input("Do you wanna bet again...? (Y/N) : ").upper()
        if play_again != 'Y':
            break
    
    print()
    print(f"Your Final balance is €{balance:.2f}\n")
    print("*******************************")
    print("    Thanks for gambling...😉   ")
    print("*******************************")

if __name__ == '__main__':
    main()