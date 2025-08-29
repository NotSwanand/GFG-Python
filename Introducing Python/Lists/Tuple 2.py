# You are given a tuple numbers that contains a A.P sequence integer. You need to calculate the next three sequences of numbers and return the whole sequence in a tuple.

# Examples:

# Input: tup = ( 1, 5, 9, 13, 17)
# Output: 1 5 9 13 17 21 25 29
# Explanation: It's an increasing sequence by 4. So, the next three numbers are 17+4= 21,  21+4=25, 25+4=29.
# Input: arr = (3, 1 , -1, -3, -5 , -7)
# Output: 3  1  -1  -3  -5  -7  -9  -11  -13
# Explanation:  It's an decreasing sequence by 2.  So, the next three numbers are  -7-2=-9, -9-2=11, -11-2=-13

def sequence(tup):
    # code here 
    lol = list(tup)
    diff = lol[1] - lol[0]
    for i in range(3):
        add = lol[-1] + diff
        lol.append(add)
    return tuple(lol)
        
