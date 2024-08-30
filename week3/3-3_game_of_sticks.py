# COMP.CS.100
# Quentin Tuffery, quentin.tuffery@tuni.fi, student id : dvb366
# Project 1 : Game of Matchsticks

"""
This program is a game of sticks!
Turn by turn, players remove between 1 and 3 sticks.
The player who removes the last stick loses!
"""

def main():

    print("Game of sticks")

    sticksremaining = 21 # defining the initial number of sticks
    player = 1 # defining the player playing first

    while sticksremaining > 0: # the game doesn't stop until there are no
        # sticks left

        nbsticks = int(input(f"Player {player} enter how many sticks to "
                             "remove: "))
        if nbsticks > 0 and nbsticks <= 3 :
            sticksremaining -= nbsticks
            if sticksremaining > 0:
                print (f"There are {sticksremaining} sticks left")
                if player == 1:
                    player = 2
                else :
                    player = 1
            continue

        else:
            print("Must remove between 1-3 sticks!")
            continue

    print(f"Player {player} lost the game!")

if __name__ == "__main__":
    main()