# Given a string s of single space-separated words. Capitalize the first letter of all words and count the number of the words in the string. Print the line and the number in separate lines with new line character at the end.

# Examples:

# Input: s = "welcome to the world of geeks"
# Output: 
# Welcome To The World Of Geeks
# 6
# Input: s = "are you enjoying programming"
# Output:
# Are You Enjoying Programming
# 4 
#User function Template for python3
s = input()

# Your code here
i = 0
count = 1
while i in range(len(s)):
    if i == 0:
        print(s[i].upper(), end ="")
        i += 1
    elif s[i] == " ":
        print(" "+s[i+1].upper(), end ="")
        i += 2
        count += 1
    else: 
        print(s[i], end="")
        i += 1
        
print()
print(count)
        
