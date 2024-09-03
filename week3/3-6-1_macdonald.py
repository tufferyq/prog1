# COMP.CS.100
# Quentin Tuffery, quentin.tuffery@tuni.fi, student id : dvb366
# Project 1 : Game of Matchsticks

"""
This is my project on the song Old macdonald
"""

def print_verse(animal,noise):
    """
    prints a verse with the correct animal and noise
    :param animal: string, the name of the animal of the verse
    :param noise: string, the noise made by the animal of the verse
    """
    print(f"Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {noise} {noise} here")
    print(f"And a {noise} {noise} there")
    print(f"Here a {noise}, there a {noise}")
    print(f"Everywhere a {noise} {noise}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")



def main():
    print_verse("cow", "moo")
    print("")
    print_verse("pig", "oink")
    print("")
    print_verse("duck", "quack")
    print("")
    print_verse("horse", "neigh")
    print("")
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()
