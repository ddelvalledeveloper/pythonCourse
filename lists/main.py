# TestList = ["element1", "element2", "element3"]
# TestList = [0, 1, 2]
Scores = [70, 85, 67.5, 90, 80]

"""
print(Scores)  # The whole array
print(Scores[2])  # The element with index 2
print(Scores[4])  # The element with index 4
print(Scores[-1])  # Backwards - The first element from the end to the beginning
print(
    Scores[0:2]
)  # Get multiple values, not including the index value after the colon ":"
print(
    Scores[1:3]
)  # Get multiple values, not starting on the beginning and not including the index value after the colon ":

print(Scores[2:])  # Get multiple values, from index 2 till the end of the array
"""

"""
print(Scores)
Scores[0] = 75  # Change the value of an element of the array
# Scores[0] = "Hello"
print(Scores)
"""

"""
print(Scores)
Scores[1:3] = (
    []
)  # Remove elements from the array. Start on index 1 up to but not including index 3
print(Scores)
"""

"""
print(Scores)
Scores[2] = ["Hello", "World"]  # Replace the value of an element with an array.
print(Scores)
print(
    Scores[2][0]
)  # Gets the first element of the array present in the third element of the parent array
"""

"""
print(Scores)
Scores.append(82)  # Adds a new value to the array
print(Scores)
print(Scores.count(82))
"""

li = [["john", "doe"]]
print(li[-1][-1])
