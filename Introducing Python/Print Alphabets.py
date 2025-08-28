# Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2 in a single line.
# Note: Print all characters with a single space after it and all in a single line. Don't add a new line after printing.

# Examples:

# Input: c1 = 'a', c2 = 'z'
# Output: "a b c d e f g h i j k l m n o p q r s t u v w x y z "
# Explanation: Printed alphabets from a to z.
# Input: c1 = "h", c2 = "u"
# Output: "h i j k l m n o p q r s t u "
# Explanation: Printed alphabets from h to u.
#User function Template for python3

def alphabets(c1,c2):
    
    #Code below to print alphabets from c1 to c2
    # Don't provide a new line after printing
    start = int(ord(c1))
    end = int(ord(c2))
    for i in range(start, end+1):
        print(chr(i), end=" ")
