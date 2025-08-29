# You are given a list that contains integers. You need to print the elements of the list with in reverse order with a space between them.

# Examples:

# Input: arr = [54, 43, 2, 1, 5]
# Output: 5 1 2 43 54
# Explanation: Just traverse in reverse and print the numbers.
# Input: arr = [324, 5, 2, 2]
# Output: 2 2 5 324
# Explanation: Just traverse in reverse and print the numbers.
#User function Template for python3
def listTraversalReverse(arr):
    rev = arr[::-1]
    #Write your code below
    for i in rev:
        print(i, end =" ")
        
    
    
    
    #Don't add a new line as it is provided by the driver code
