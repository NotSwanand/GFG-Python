# You are given a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. 

# Examples:

# Input: n = 5
# Output: 5 10 15 20 25 30 35 40 45 50
# Input: n = 6
# Output: 6 12 18 24 30 36 42 48 54 60

# Constraints:
# 1 ≤ n ≤ 10

#User function Template for python3
n = int(input())

# Your code here
for i in range(1,11):
    print(n*i, end=" ")
