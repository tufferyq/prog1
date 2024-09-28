"""
COMP.CS.100 - Programming 1

Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""



def count_abbas(word):
    """
    this function counts the amount of times the word "abba" appears in the word(s) given  by the user
    :param word: string, given by the user
    :return count: int, amount of times the word "abba" appears
    """
    abba = True
    searchedword = "abba"
    counter = 0
    startat = 0

    while abba:
        indexfound = word[startat:len(word)].find(searchedword)

        if indexfound == -1:
            abba = False

        else:
            counter += 1
            startat += indexfound+1
    return counter
