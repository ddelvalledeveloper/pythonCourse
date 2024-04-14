# Python is easy - Functions homework
"""
In this file, we will define information about a musician 
and one of their songs using variables.
"""

# Name of the artist
Artist = "Marilyn Manson"
# Music genre
Genre = "Rock"
# Music genre
SubGenre = "Industrial"
# My favorite song
FavoriteSong = "Man That You Fear"
# Total duration of my favorite song (Seconds)
DurationInSeconds = 370
# Total duration of my favorite song (Minutes)
DurationInMinutes = 6.16


# Returns the name of the artist
def artist():
    return Artist


# Returns the genre of the artist
def genre():
    return Genre


# Returns the subgenre of the artist
def subgenre():
    return SubGenre


# Checks if the total duration in minutes of a song is greater than five
def isDurationinMinutesMoreThanFive(totalDuration):
    if totalDuration > 5:
        return True
    else:
        return False


print(artist())
print(genre())
print(subgenre())
print(isDurationinMinutesMoreThanFive(DurationInMinutes))
