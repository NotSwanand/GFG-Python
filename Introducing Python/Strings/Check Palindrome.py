# Given a string s, you need to check if it is palindrome or not. A palidrome is a string that reads the same from front and back.

# Note: Ignore the case in this question.

# Examples:

# Input: s = "Hello"
# Output: false
# Explanation: Hello is not equal to olleH so it's not a palindrome.
# Input: s = "TenEt"
# Output: true
# Explanation: TenEt == tEneT as we are ignoring the case.
def isPalindrome(s):
    #code here
    s = s.lower()
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low]!= s[high]:
            return False
        low = low+1
        high= high-1
    else:
        return True
