"""
COMP.CS.100 - Programming 1

Author: Quentin Tuffery
    id: dvb366
    email: quentin.tuffery@tuni.fi
"""


def reverse_name(name):
    """
    This function inverts the order of the two words that the user gives
    :param name: string, 2 words separated by a "," defined by user
    :return reversed_name: string, 2 words reversed
    """
    if "," in name:

        name = name.split(",")

        word1 = name[0]
        word1 = word1.strip()

        word2 = name[1]
        word2 = word2.strip()

        if word1 == word2 == "":
            result = ""

        elif word1 == "":
            result = (f"{word2}")

        elif word2 == "":
            result = (f"{word1}")

        else: result = (f"{word2} {word1}")

    else:
        result = name

    return result
