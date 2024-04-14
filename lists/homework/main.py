# Python is easy - Lists homework
"""
In this file, we will create two lists. The first list will contain unique values, 
while the second list will have duplicate values already present on the first list. 
This will be achieved with the help of a single function designed to check whether a 
value is unique or not. Based on this, the function will decide which list to add the value to.
"""


def addElementToList(ValueToAdd):
    ElementExists = MyUniqueList.count(ValueToAdd)
    if ElementExists == 0:
        MyUniqueList.append(ValueToAdd)
        return True
    else:
        MyLeftovers.append(ValueToAdd)
        print(
            "Value "
            + chr(34)
            + str(ValueToAdd)
            + chr(34)
            + " already present in the list."
        )
        return False


MyUniqueList = []
MyLeftovers = []

print("Initial list")
print(MyUniqueList)
AddResult = addElementToList(1)
if AddResult:
    print(MyUniqueList)

AddResult = addElementToList("Hello")
if AddResult:
    print(MyUniqueList)

AddResult = addElementToList("Hello")
if AddResult:
    print(MyUniqueList)

AddResult = addElementToList("World")
if AddResult:
    print(MyUniqueList)

AddResult = addElementToList(["Hi"])
if AddResult:
    print(MyUniqueList)


print("Final list")
print(MyUniqueList)
print("Left over list")
print(MyLeftovers)
