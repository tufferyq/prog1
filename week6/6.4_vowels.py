"""
COMP.CS.100 - Programming 1

Author: Quentin Tuffery
    id: dvb366
    email: quentin.tuffery@tuni.fi
"""


def main():
    word = input("Enter a word: ")
    vowels = 0
    consonants = 0

    for index in range (0,len(word)):
        if word[index] in ['a','e','i','o','u','y']:
            vowels += 1
        else: consonants += 1
        index += 1

    print(f'The word "{word}" contains {vowels} vowels and {consonants} consonants.', end = "")


if __name__ == "__main__":
    main()