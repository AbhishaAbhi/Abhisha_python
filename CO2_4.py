#Generate a list of 4 digit numbers with all their digits even and the number is a perfect square?

import math
for i in range(1000,10000):
    squareroot=int (math.sqrt(i))
    if (squareroot * squareroot == i):
        if all (int(digit) % 2 == 0
            for digit in str(i)):
                print(i)
