"""
COMP.CS.100 - Programming 1
Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""

def main():
    # select & open file
    filename = input("Enter the name of the score file: ")
    scores = {}
    try:
        scores_file = open(filename, mode="r")
    except:
        print("There was an error in reading the file.")
        return

    # convert text to a dictionary
    for line in scores_file:
        line = line.rstrip()
        try:
            name, score = line.split(" ")
        except ValueError:
            print(f"There was an erroneous line in the file:")
            print(line)
            return

        try:
            score = int(score)
        except ValueError:
            print(f"There was an erroneous score in the file:")
            print(score)
            return

        if name not in scores:
            scores[name] = score
        else:
            scores[name] += score

    # print result scores
    print("Contestant score:")
    for name in sorted(scores):
        print(f"{name} {scores[name]}")

    scores_file.close()


if __name__ == "__main__":
    main()
