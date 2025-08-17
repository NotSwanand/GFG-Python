# You are given a string s, you need to print its characters at even indices (index starts at 0).

# Examples:

# Input: s = "Geeks"
# Output: Ges
# Explanation: The even indices characters are printed.
# Input: s = "DoctorPhenomenal"
# Output: DcoPeoea
# Explanation: The even indices characters are printed.
class Solution:
    def print_even_indices(self, s: str):
        #code here
        result=""
        length = len(s)
        for i in range(length):
            if i %  2 == 0:
                result += s[i]
        
        print(result, end="")
                
                
