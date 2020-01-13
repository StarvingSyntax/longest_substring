# P
# Function will take a string 
# find the longest subString with nonrepeating Characters within the subString
# 
# E 
#  
# D
#
# Takes in String, return integer(length of subString)
# A
# Create variable to store longest Sting
# Create dictionary to store used characters
# Loop over String adding to LongString if not in the dictionary
# Once you get to a repeated Char/You hit a Char in the Dicionary return length of LongString


def longestString(longString):
    ourString = longString[0]
    finalString = ''
    visitedChars = {} #Track characters
    
    for char in range(1, len(longString)): # Start from index 1
        if char != longString[longString.index(char) - 1]: # If not same as last index
            ourString += char
            visitedChars[char] == char #Add to Dict
        else:
            finalString = ourString # Move Our subString
            visitedChars = {} # Clear Dict
            ourString = char # Start Over b/c longest might not be at the beginning
    
    print(len(finalString))
    
    
    
print(longestString('abcabcbb'))