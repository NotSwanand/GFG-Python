# Given an integer n find the sum of the first n natural number.

# Examples:

# Input: n = 10
# Output: 55
# Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
# Input: n = 5
# Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15.
class Solution:
    def sumOfNumbers(self, n):
        # code here
        sum= 0
        for i in range(n+1):
            sum = sum + i
        
        return sum
