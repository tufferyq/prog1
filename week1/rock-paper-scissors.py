# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

def main():
    player1 = input("Player 1, enter your choice (R/P/S): ")
    player2 = input("Player 2, enter your choice (R/P/S): ")

#conditions in which there is a tie
    if player1 == "R" and player2 == "R":
        print("It's a tie!")
    elif player1 == "S" and player2 == "S":
        print("It's a tie!")
    elif player1 == "P" and player2 == "P":
        print("It's a tie!")

# conditions in which player 1 wins
    elif player1 == "R" and player2 == "S":
        print("Player 1 won!")

    elif player1 == "P" and player2 == "R":
        print("Player 1 won!")

    elif player1 == "S" and player2 == "P":
        print("Player 1 won!")

# conditions in which player 2 wins
    elif player2 == "R" and player1 == "S":
        print("Player 2 won!")

    elif player2 == "P" and player1 == "R":
        print("Player 2 won!")

    elif player2 == "S" and player1 == "P":
        print("Player 2 won!")

if __name__ == "__main__":
    main()