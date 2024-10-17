"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price):
        """

        A product object is initialized with the name and
        the initial amount of money in the wallet.

        :param name: str, the name of the product
        :param price: float, how much money this product costs
        """

        self.__name = name
        self.__price = price
        self.__sale = 0

    def set_sale_percentage(self, sale):
        """
        When the sale is needed to change, this method will handle it

        :param sale: float, new sale percentage of the selected product
        """
        self.__sale = sale
        return True

    def get_price(self):
        """
        When a person's saled price is needed to be printed on
        screen this method will handle it.

        :return saledprice: float, initial price with the affected sale %
        """
        saledprice = self.__price * (1-self.__sale/100)
        return saledprice

    def printout(self):
        """
        When a product's data is needed to be printed on
        screen this method will handle it.  Also good
        for debugging and testing purposes.
        """

        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale:.2f}")

def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
