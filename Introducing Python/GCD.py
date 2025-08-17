# Given two numbers a and b. The task is to find the GCD of  a and b.
# The GCD of two numbers is the largest number that can divide both a and b perfectly.

# Examples:

# Input: a = 6, b = 9
# Output: 3
# Explanation: After 3 there is no number that can divide both 6 and 9 perfectly.
# Input: a = 10, b = 15
# Output: 5
# Explanation: 5 is the greatest common divisor of 10 and 15.
# Constraints:
# 1  ≤  a, b  ≤  100

#User function Template for python3
a = int(input())
b = int(input())


# Your code here
if a < b:
    n = a
else:
    n = b
    
for i in range(1 , n+1):
    if (a % i == 0 and b % i == 0):
        gcd = i
print(gcd)
