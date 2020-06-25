###########################################
# Author: Malay Agarwal
# Problem: 
# Write a function that takes a list of strings
# and prints each on a new line in a frame
# *******
# *Hello*
# *world*
# *in   *
# *an   *
# *hour *
# *******
###########################################

# starting simple for Day1 to get used to git
def stringInFrame():
    inputString = input("input a word/sentence: ")
    convertedList = inputString.split(" ")
    longestWord = 0
    for elem in convertedList:
        if len(elem) > longestWord:
            longestWord = len(elem)
    return('*'*(longestWord+2))
    for elem in convertedList:
        if len(elem) < longestWord:
            elem = elem + (' ')*(longestWord - len(elem))
        return('*'+elem+'*')
    return('*'*(longestWord+2))

print(stringInFrame)