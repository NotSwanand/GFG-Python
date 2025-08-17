# Given an integer n. Write a program to print the Inverted "Right angle triangle" wall. The length of the perpendicular and base is n. Use double loop.

# Examples:

# Input: n = 4
# Output:
# * * * * 
# * * * 
# * * 
# *
# Explanation: Length of perpendicular and base of triangle is 4 .
# Input: n = 3
# Output:
# * * * 
# * * 
# *
# Explanation: Length of perpendicular and base of triangle is 3 .
# Constraints:
# 1 <= n <= 10
#User function Template for python3
n = int(input())

# Your code here
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
