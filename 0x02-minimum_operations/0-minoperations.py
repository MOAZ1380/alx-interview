#!/usr/bin/python3
'''Coding challenge.'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result '''
    count = 0
    while(n > 1):
        if (n % 3 == 0):
            n //= 3
            count += 3
        elif (n % 2 == 0):
            n //= 2
            count += 2
        else:
            count += n
            n = 1
    return count
