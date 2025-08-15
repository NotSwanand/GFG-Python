# Given an integer n. Write a program to return the last digit of the number.

# Examples:

# Input: n = 10
# Output: 0
# Input: n = 9768
# Output: 8
# Constraints:

# -109 ≤ n ≤ 109

class Solution:
    def lastDigit(self, n: int) -> int:
        #Code here
        n = abs(n)
        return n % 10
