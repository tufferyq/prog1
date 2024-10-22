"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplifies the divisor and numerator of the fraction
        """
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        new_numerator = self.__numerator // divisor
        new_denominator = self.__denominator // divisor
        return Fraction(new_numerator, new_denominator)

    def complement(self):
        """
        Calculates the complement fraction of the current fraction

        :return Fraction(new_numerator, self.__denominator): complement of
        the current fraction
        """
        new_numerator = self.__numerator * (-1)
        return Fraction(new_numerator, self.__denominator)

    def reciprocal(self):
        """
        Calculates the reciprocal fraction of the current fraction

        :return Fraction(new_numerator, self.__denominator):
        object, reciprocal of
        the current fraction
        """
        new_numerator = self.__denominator
        new_denominator = self.__numerator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, fraction):
        """
        Multiplies 2 fractions together
        :param fraction: fraction to multiply the current object fraction with

        :return Fraction(new_numerator, self.__denominator): object, result
        of the
        multiplication of the 2 fractions
        """
        new_numerator = self.__numerator * fraction.__numerator
        new_denominator = self.__denominator * fraction.__denominator
        return Fraction(new_numerator,new_denominator)

    def divide(self, fraction):
        """
        Divides 2 fractions together
        :param fraction: fraction to divide the current object fraction with

        :return Fraction(new_numerator, self.__denominator): object, result
        of the
        division of the 2 fractions
        """
        reciprocal = fraction.reciprocal()
        new_numerator = self.__numerator * reciprocal.__numerator
        new_denominator = self.__denominator * reciprocal.__denominator
        return Fraction(new_numerator,new_denominator)

    def add(self, fraction):
        """
        Adds the param fraction to the object fraction
        :param fraction: object, fraction to add to the current object
        fraction

        :return Fraction(new_numerator, self.__denominator): object, result
        of the addition
        """
        frac1_numerator = self.__numerator * fraction.__denominator
        frac2_numerator = fraction.__numerator * self.__denominator
        fracs_denominator = self.__denominator * fraction.__denominator

        result_numerator = frac1_numerator + frac2_numerator
        result_denominator = fracs_denominator
        return Fraction(result_numerator,result_denominator)

    def deduct(self,fraction):
        """
        Deducts the param fraction from the object fraction
        :param fraction: object, fraction to deduct to the current object
        fraction

        :return Fraction(new_numerator, self.__denominator): object, result
        of the deduction
        """
        frac1_numerator = self.__numerator * fraction.__denominator
        frac2_numerator = fraction.__numerator * self.__denominator
        fracs_denominator = self.__denominator * fraction.__denominator

        result_numerator = frac1_numerator - frac2_numerator
        result_denominator = fracs_denominator
        return Fraction(result_numerator, result_denominator)

    def __lt__(self, other):
        """
        Defines the "lesser than" comparison. The 2 fractions are put to
        the same denominator, and then we compare the 2 numerators
        """
        frac1_numerator = self.__numerator * other.__denominator
        frac2_numerator = other.__numerator * self.__denominator
        return frac1_numerator < frac2_numerator

    def __gt__(self, other):
        """
        Defines the "greater than" comparison. The 2 fractions are put to
        the same denominator, and then we compare the 2 numerators
        """
        frac1_numerator = self.__numerator * other.__denominator
        frac2_numerator = other.__numerator * self.__denominator
        return frac1_numerator > frac2_numerator

    def __str__(self):
        """
                :returns: str, a string-presentation of the fraction in the format
                               numerator/denominator.
                """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def fractionize(fraction_string):
    """
    Turns the fractions of the string type into 2 int values for nmerator
    and denominator. In the end, turns it into a Function class object

    :param fraction_string: string, initial fraction entered with keyboard
    :return fraction: Fraction class object

    """
    numerator, denominator = fraction_string.split("/")
    fraction = Fraction(int(numerator), int(denominator))
    return fraction

def main():

    fraction_dict = {}

    while True:
        command = input("> ")

        if command == "add":
            new_fraction = input("Enter a fraction in the form "
                                 "integer/integer: ")
            new_fraction = fractionize(new_fraction)

            fraction_name = input('Enter a name: ')

            fraction_dict[fraction_name] = new_fraction

        elif command == "print":
            fraction_name = input('Enter a name: ')

            try:
                print(f"{fraction_name} = {fraction_dict[fraction_name]}")
            except KeyError:
                print(f"Name {fraction_name} was not found")

        elif command == "list":
            keyslist = sorted(fraction_dict.keys())
            for key in keyslist:
                    print(f"{key} = {fraction_dict[key]}")

        elif command == "*":
            frac1_key = input("1st operand: ")

            try:
                frac1 = fraction_dict[frac1_key]
            except KeyError:
                print(f"Name {frac1_key} was not found")
                continue

            frac2_key = input("2nd operand: ")

            try:
                frac2 = fraction_dict[frac2_key]
            except KeyError:
                print(f"Name {frac2_key} was not found")
                continue

            result = frac1.multiply(frac2)

            print(f"{frac1} * {frac2} = {result}")
            print(f"simplified {result.simplify()}")

        elif command == "file":
            filename = input("Enter the name of the file: ")

            try:
                file = open(filename, mode='r')

                for file_line in file:
                    file_line = file_line.rstrip()
                    fraction_name, fraction = file_line.split("=")
                    fraction = fractionize(fraction)

                    fraction_dict[fraction_name] = fraction

            except ValueError:
                print("Error: the file cannot be read.")
                continue

            except FileNotFoundError:
                print("Error: the file cannot be read.")
                continue

            file.close()

        elif command == "quit":
            print("Bye bye!")
            return

        else:
            print("Unknown command!")
            continue

if __name__ == '__main__':
    main()