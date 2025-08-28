# Given a string s, you need to perform the following operation.

# 1. Capitalize the first letter and print in a new line.
# 2. Convert the whole string to uppercase and print in a new line.

# Examples: 

# Input: s = "hello"
# Output: 
# Hello
# HELLO
# Explanation: In Hello, the first letter is capitalized. In HELLO all letters are in the uppercase.
# Input: s = "world"
# Output:
# World
# WORLD
# Explanation: In World, the first letter is capitalized. In WORLD all letters are in the uppercase.
#User function Template for python3

def changeCase(s):
    # code here to print capitalized,  and then in the upper case
    lol = int(len(s))
    first_cap = ""
    full_cap = ""
    for i in range(0,lol):
        while i == 0:
            first_cap += s[i].upper()
            full_cap += s[i].upper()
            break
        else:
            first_cap += s[i]
            full_cap += s[i].upper()
    print(first_cap)
    print(full_cap)
    return first_cap, full_cap
            
