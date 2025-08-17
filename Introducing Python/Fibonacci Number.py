# Given an integer n. Write a program to find the nth Fibonacci number.

# F(0)= 0, F(1)=1
# The nth Fibonacci number is given by the forumla F(n) = F(n-1) + F(n-2). The first few fibonacci numbers are: 0 1 1 2 3 5. . . . 

# Examples:

# Input: n = 4
# Output: 3
# Explanation: In the series 0 1 1 2 3 5...... the fourth fibonacci number is 3.
# Input: n = 5
# Output: 5
# Explanation: In the series 0 1 1 2 3 5 8...... the fifth fibonacci number is 5.

#User function Template for python3
#Back-end complete function Template for Python 3
n = int(input())

########### Write your code below ###############
fib = 0

if n == 0:
    fib = 0
elif n == 1:
    fib = 1
else:
    a,b = 0,1
    for i in range(2,n+1):
        a, b = b, a + b
    fib = b
    
    

########### Write your code above ###############
print(fib)
