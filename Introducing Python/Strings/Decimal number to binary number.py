# Given a decimal number n (positive) in string format, compute its binary string equivalent and return it. 
# Note: Don't add a new line at the end.

# Examples:

# Input: n = 7
# Output: 111
# Input: n = 33
# Output: 100001
#User function Template for python3
#Complete the below function
def toBinary(n):
    #Your code here
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = res +str(n%2)
        n = n//2
    return res[::-1]
    
