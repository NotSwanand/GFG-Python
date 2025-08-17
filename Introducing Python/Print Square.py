# Given an integer n, write a program to print the square of size n using "*" character. 

# Examples :

# Input: n = 4
# Output:
# * * * *
# *     *
# *     *
# * * * *
# Explanation: It's a square! Each side contains n = 4 .
# Input: n = 3
# Output:
# * * * 
# *   *
# * * *
# Explanation: It's a square! Each side contains n = 3 .
# Constraints:
# 1 ≤ n ≤ 10

#User function Template for python3
n = int(input())

# Your code here
for i in range(n):
    space = (2*n) - 5
    if i == 0 or i == n-1:
        print("* "*(n-1)+"*")
    else:
        print("*", " "*space, "*")
