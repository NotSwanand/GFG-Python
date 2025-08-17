# Given an integer n. Write a program to print the Right angle triangle. The length of the perpendicular and base is n.  

# Examples :

# Input: n = 9
# Output:
# *
# * *
# *   *
# *     *
# *       *
# *         *
# *           *
# *             *
# * * * * * * * * * 
# Explanation: Length of perpendicular and base of triangle is 9.
# Input: n = 4
# Output:
# *
# * *
# *   *
# * * * *
# Explanation: Length of perpendicular and base of triangle is 4.
class Solution:
    def printPattern(self, n):
        #Code here
        for i in range(1,n+1):
            if i == 1:
                print("*")
            elif i == n:
                print("* "*i)
            else:
                print("*" + " "*(2*i-3) + "*")
