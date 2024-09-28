"""
COMP.CS.100 - Programming 1

Author: Quentin Tuffery
    id: dvb366
    email: quentin.tuffery@tuni.fi
"""

def capitalize_initial_letters(sentence):
    """
    This function creates an acronym based of the words given as an input
    :param sentence: string, sentence of words
    :return sentence_capitalized: string, sentence with first letter of each word in
    uppercase, the rest in lowcase
    """

    words = sentence.split()

    for index in range (0, len(words)):
        words[index] = words[index].capitalize()

    sentence_capitalized = " ".join(words)

    return sentence_capitalized