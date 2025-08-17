# Given an integer n. Write a program to find the first prime number greater than n.

# Examples:

# Input: n = 15
# Output: 17
# Explanation: 17 is next prime number.
# Input: n = 7
# Output: 11
# Explanation: 11 is the prime number next to 7.
# Constraints:
# 1 <= n <= 500

#User function Template for python3
n = int(input())

# Your code here
for i in range(n+1,500):
    prime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)
        break
        
