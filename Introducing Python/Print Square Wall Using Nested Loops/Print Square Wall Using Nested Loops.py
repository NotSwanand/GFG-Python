# Given an integer n,  write a program to print the square wall of size n using nested loops. Try not to use String multiplication.

# Examples:

# Input: n = 5
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# Explanation: Its perfect square wall. 
# Input: n = 4
# Output:
# * * * * 
# * * * * 
# * * * * 
# * * * * 
# Explanation: Its perfect square wall. 
#User function Template for python3
n = int(input())

# Your code here
for i in range(n):
    for j in range(n,0,-1):
        if j > 0:
            print("*",end=" ")
    print("")    
