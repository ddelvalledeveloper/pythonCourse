# Python is easy - If statements homework
"""
In this file, we'll create a function that uses conditional statements
to determine the equality between three numbers
"""


def compareNumbers(NumberOne, NumberTwo, NumberThree):
    if (
        int(NumberOne) == int(NumberTwo)
        or int(NumberOne) == int(NumberThree)
        or int(NumberTwo) == int(NumberThree)
    ):
        return True
    else:
        return False


print(compareNumbers(1, 2, 3))  # False
print(compareNumbers(1, 1, 3))  # True
print(compareNumbers(1, 2, 1))  # True
print(compareNumbers(1, 1, 1))  # True
print(compareNumbers(1, 2, "1"))  # True
print(compareNumbers("7", "0", "7"))  # True
