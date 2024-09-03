"""
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""
def repeat_name(name, length):
    """
    1 or 3 times. It will repeat the name X times
    :param name: string, the name of the person in the verse
    :param length: int, the amount of times to repeat the name
    """
    if length == 1:
        print(f"{name}, {name}", end='')
    if length == 3:
        print(f"{name}, {name} Bear\n{name}, {name} Bear\n{name},"
                f" {name} Bear")

def verse(sentence, name):
    """
    :param name: string, the name of the person in the verse
    :param sentance: string, the sentance.
    """
    print(f"{sentence}")
    repeat_name(name, 1)
    print(f"\n{sentence}")
    repeat_name(name, 3)
    print(f"{sentence}")
    repeat_name(name, 1)
    print(" Bear")


def main():
    verse("I know someone you don't know", "Yogi")
    print("")
    verse("Yogi has a best friend too", "Boo Boo")
    print("")
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
