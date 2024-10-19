"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for Mölkky.
"""

class Player:
    def __init__(self, name):
        """
        init
        """
        self.__name = name
        self.__score = 0
        self.__all_scores = []
        self.__average = 0

    def get_name(self):
        """
        init
        """
        return self.__name

    def get_points(self):
        """
        init
        """
        return self.__score

    def add_points(self, pts):
        """
        init
        """
        self.__score += pts
        if 40 <= self.__score <= 49:
            print(
                f"{self.__name} needs only {50 - self.__score} points. It's "
                f"better to avoid knocking down the pins with higher points.")

        return self.__score

    def has_won(self):
        """
        init
        """
        if self.__score == 50:
            return True
        elif self.__score > 50:
            self.__score = 25
            print(f"{self.__name} gets penalty points!")

    def get_average(self, pts):
        """
        init
        """
        average = 0
        self.__all_scores.append(pts)
        for i in range(0,len(self.__all_scores)):
            average += self.__all_scores[i]
        average /= len(self.__all_scores)
        if average > self.__average:
            self.__average = average
            return True
        else:
            self.__average = average
            return False

    def get_accuracy(self):
        """
        init
        """
        accuracy = 0
        accuracy_count = 0
        if len(self.__all_scores) != 0:
            for i in range(0,len(self.__all_scores)):
                if self.__all_scores[i] != 0:
                    accuracy_count += 1
            accuracy = accuracy_count / len(self.__all_scores) * 100
        return accuracy

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.get_average(pts) and throw > 2:
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, "
              f"hit percentage {player1.get_accuracy():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, "
              f"hit percentage {player2.get_accuracy():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
