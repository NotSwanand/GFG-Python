# Given a number n find the prime factorization of the number.

# Note: Print the prime factors in non-decreasing order.

# Examples:

# Input: n = 100
# Output: 2 2 5 5
# Explanation: 100 = 2 * 2 * 5 * 5
# Input: n = 27
# Output: 3 3 3
# Explanation: 27 = 3 * 3 * 3 
# Constraint:
# 2 <= n <= 200

class Solution:
    def printPrimeFactorization(self, n):
        #code here
        while n % 2 == 0:
            print(2, end=" ")
            n //= 2
            
        i = 3
        while i*i <= n:
            while n % i == 0:
                print(i, end= " ")
                n //= i
            i+=2
            
        if n > 2:
            print(n, end=" ")
                
