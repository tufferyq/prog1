"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

def convert_grades(grades):
    """
    This function converts every grade above 0 to the number 6.
    :param grades: list, list of grades
    """
    for value in grades:
        if value != 0:
            index = grades.index(value)
            grades[index] = 6

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
