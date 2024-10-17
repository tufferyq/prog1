"""
COMP.CS.100 - Programming 1
Author: Quentin Tuffery
id: dvb366
email: quentin.tuffery@tuni.fi
"""

def get_valid_integer(prompt):
    """
    Demande à l'utilisateur de saisir un entier et vérifie qu'il est valide.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def main():
    # Demander la largeur et la hauteur
    width = get_valid_integer("Enter the width of a frame: ")
    height = get_valid_integer("Enter the height of a frame: ")

    # Demander le caractère d'impression
    print_mark = input("Enter a print mark: ")
    print()

    # Afficher le cadre
    for _ in range(height):
        print(width * print_mark)

if __name__ == "__main__":
    main()