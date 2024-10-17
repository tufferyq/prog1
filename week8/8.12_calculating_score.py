"""
COMP.CS.100 - Programming 1
Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""

#def add_scores(dictionary):
 #   """
  #  this function adds scores to the dictionary.
   # :param dictionary:
   # """
   # #adding scores inside
   # name = input("enter name: ")
    #score = input("enter score: ")
    #dictionary[name] = score
    #return dictionary

def main():
    #select & open file
    filename = input("Enter the name of the score file: ")
    scores = {}
    scores_file = open(filename, mode="r")

    #add_scores(scores)
    for line in scores_file:
        line = line.rstrip()
        name, score = line.split()
        if name not in scores.keys():
            scores[name] = int(score)
        else: scores[name] += int(score)

    #print result scores
    print("Contestant score:")
    for name in sorted(scores):
        print(f"{name} {scores[name]}")

    scores_file.close()


if __name__ == "__main__":
    main()