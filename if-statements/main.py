# General structure

"""
if condition:
    Action
else:
    OtherAction
"""

Click = False

Likes = 0

Click = True

if Click == True:
    Likes += 1
    Click = False

# print(Likes)


Temperature = 20
# Temperature = 14
# Temperature = 15
Thermostat = 15

# print(Thermostat)
if Temperature <= 15:
    Thermostat += 5

# print(Thermostat)

if Temperature >= 20:
    Thermostat -= 3
# print(Thermostat)


# Time = "Day"
# Time = "Night"
Time = "Morning"
# Sleepy = False
Sleepy = False
InBed = True
Pajamas = "Off"

# if Time == "Night" and Sleepy == True:
#     Pajamas = "On"

if Time == "Night" or Sleepy == True:
    Pajamas = "On"
elif Time == "Morning" and InBed == True:
    Pajamas = "On"
else:
    Pajamas = "Off"

print(Pajamas)
