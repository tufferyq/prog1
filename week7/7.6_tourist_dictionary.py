"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""
def translate_word(word, dictionary):
    """
    this function translates the given word from english to spanish,
    if it exists in the dictionary
    :param word: str, english word
    :param dictionary: dictionary, english to spanish words
    """

    if word in dictionary:
        print(f"{word} in Spanish is {dictionary[word]}")

    else:
        print(f"The word {word} could not be found from the dictionary.")

def translate_text(text, dictionary):
    """
    this function translates the given text from english to spanish.
    If the words are not in the dictionary, they will be printed in english
    :param text: str, multiple words
    :param dictionary: dictionary, english to spanish words
    """
    text = text.split()
    for index in range(len(text)):
        if text[index] in dictionary:
            text[index] = dictionary[text[index]]
        else:
            pass
        index += 1

    text = " ".join(text)
    return text

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            translate_word(word, english_spanish)

        elif command == "A":
            word_english = input("Give the word to be added in English: ")
            word_spanish = input("Give the word to be added in Spanish: ")
            english_spanish[word_english] = word_spanish

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]

            else:
                print(f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            for row in sorted(english_spanish):
                print(row, english_spanish[row])

        elif command == "Q":
            print("Adios!")
            return

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            text = translate_text(text,english_spanish)
            print(f"The text, translated by the dictionary:")
            print(text)

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
