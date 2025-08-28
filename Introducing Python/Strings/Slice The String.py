# Given a string s, you need to slice it so that the output is a substring that contains all the characters except the first and last.
# Note: The length of the s will be greater than 2. 

# Examples:

# Input: s = "Hello"
# Output: ell
# Explanation: The first and last character are ignored.
# Input: s = "World"
# Output: orl
# Explanation: The first and last characters are ignored.
# Hint: You can use s.substring(start, end)
#User function Template for python3

def sliceString(s):
    #Write your code below
    l=len(s)
    sol = s[1:l-1:1]
    return sol

