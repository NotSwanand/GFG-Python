# You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

# Examples:

# Input: arr = [54, 43, 2, 1, 5]
# Output: 53 42 1 0 4
# Explanation: Just decrement the numbers by 1.
# Input: arr = [324, 5, 2, 2]
# Output: 323 4 1 1
# Explanation: Just decrement the numbers by 1.
def decrementList(arr):
    #code here
    new =[]
    for i in arr:
        new.append(i - 1)
        
    return new
