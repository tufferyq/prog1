# COMP.CS.100
# Creator: Quentin Tuffery
# Student id number: dvb366

def main():
    string = input("How do you feel? (1-10) ")
    feel = int(string)

    if feel == 1:
        print("A suitable smiley would be :'(")
    elif feel >1 and feel < 4:
        print("A suitable smiley would be :-(")
    elif feel >= 4 and feel <= 7:
        print("A suitable smiley would be :-|")
    elif feel >7 and feel <10:
        print("A suitable smiley would be :-)")
    elif feel == 10:
        print("A suitable smiley would be :-D")
    else:
        print("Bad input!")

if __name__ == "__main__":
    main()