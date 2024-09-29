"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    word_count = {}
    print("Enter rows of text for word counting. Empty row to quit.")

    text = "initiate value"

    while text != "":
        text = input("")
        if text != "":
            text = text.lower().split()
            for word in text:
                if word in word_count:
                    word_count[word] += 1
                else: word_count[word] = 1

    for word in sorted(word_count):
        print(f"{word} : {word_count[word]} times")





if __name__ == "__main__":
    main()
