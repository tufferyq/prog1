"""
COMP.CS.100 - Programming 1

Author: Quentin Tuffery
    id: dvb366
    email: quentin.tuffery@tuni.fi
"""

def create_an_acronym(allwords):
    """
    This function creates an acronym based of the words given as an input
    :param allwords: string, words
    :return acronym: string, first letter of each word joined together
    """
    acronym = ""

    words = allwords.split()

    for word in words:
        acronym += word[0]

    acronym = acronym.upper()

    return acronym