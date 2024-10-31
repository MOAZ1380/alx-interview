#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):

    while(x < len(data)):
        byte = data[x]
        num_bytes = 0

        if (byte & 0b10000000) == 0:
            num_bytes = 1
        elif (byte & 0b11000000) == 0b11000000:
            num_bytes = 2
        elif (byte & 0b11100000) == 0b11100000:
            num_bytes = 3
        elif (byte & 0b11110000) == 0b11110000:
            num_bytes = 4
        else:
            return False

        if x + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            if (data[x + j] & 0b11000000) != 0b10000000:
                return False
        x += num_bytes
    return True
