# General structure

"""
def functionName(Input):
    Action
    return Output
"""


def addOne(value):
    return value + 1


# def addOneAddTwo(valueOne, valueTwo):
#     return valueOne + 1, valueTwo + 2

# resultPlusOne, resultPlusTwo = addOneAddTwo(1, 2)
# print(resultPlusOne)
# print(resultPlusTwo)


def addOneAddTwo(valueOne, valueTwo):
    output = valueOne + 1
    output += valueTwo + 2
    return output


var1 = 0
result = addOne(var1)
# print(result)

result = addOne(5)
# print(result)

result = addOne(1.8)
# print(result)

result = addOne(6.3 + 3.4)
# print(result)


resultaddOneAddTwo = addOneAddTwo(1, 2)
print(resultaddOneAddTwo)
