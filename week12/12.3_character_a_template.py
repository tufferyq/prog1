"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:

    def __init__(self, name):
        """

        """
        self.__name = name
        self.__items = []

    def give_item(self, item):
        """
        adds an item in the list of items of the selected character
        """
        self.__items.append(item)

    def printout(self):
        """

        """
        list_without_duplicates = sorted(list(dict.fromkeys(self.__items)))

        print(f"Name: {self.__name}")
        if not self.__items:
            print("  --nothing--")
        else:
            for item in list_without_duplicates:
                print(f"  {self.how_many(item)} {item}")

    def get_name(self):
        """
        Returns the name of the selected character

        :return self.__name: string, name of the character
        """
        return self.__name

    def remove_item(self,item):
        """
        removes an item from the list of items of the selected character
        """
        if item in self.__items:
            self.__items.remove(item)

    def has_item(self,item):
        """
        checks if the selected item is in the items list of the character

        :return True: bool, if the item is in the list
        """
        if item in self.__items:
            return True
        else:
            return False

    def how_many(self,item):
        """

        """
        count = self.__items.count(item)
        return count

def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
