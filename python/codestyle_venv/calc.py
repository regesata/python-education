"""This module realised class which
provide arithmetical function such as
addition, subtraction, multiplication and
division .

Classes:
    Calculator
"""

__version__ = "0.1"
__author__ = "Artur Denesiuk"


class Calc:
    """
    A class represents calculator.
    All methods are static

    Methods
    -------
    addition():
        Returns result of addition first with second
    subtraction():
        Returns result of subtraction second from first
    multiplication():
        Returns result of multiplication first with second
    division():
        Returns result of division first by second
    """

    @staticmethod
    def addition(first: float, second: float) -> float:
        """Method realise the addition of two numbers

        :param first: First number
        :param second: Second number
        :returns: result of addition
        :rtype: float

        """

        return first + second

    @staticmethod
    def subtraction(first: float, second: float) -> float:
        """Method realise the subtraction of two numbers

        :param first: First number
        :param second: Second number
        :returns: result of subtraction
        :rtype: float

        """
        return first - second

    @staticmethod
    def multiplication(first: float, second: float) -> float:
        """Method realise the multiplication of two numbers

        :param first: First number
        :param second: Second number
        :returns: result of multiplication
        :rtype: float

        """

        return first * second

    @staticmethod
    def division(first: float, second: float) -> float:
        """Method realise the division of two numbers

        :param first: First number
        :param second: Second number
        :returns: result of division
        :rtype: float
        """

        return first / second


if __name__ == "__main__":
    print(f"Addition: {Calc.addition(1.2, 5)}")
    print(f"Subtraction: {Calc.subtraction(17.2, 15)}")
    print(f"Multiplication: {Calc.multiplication(13.5, 15.4)}")
    print(f"Division: {Calc.division(1.2, 5)}")
