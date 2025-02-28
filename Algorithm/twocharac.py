#!/bin/python3

from itertools import combinations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def is_alternating(s):
    """Check if a string alternates between two characters."""
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def alternate(s):
    """Find the longest alternating string with only two distinct characters."""
    unique_chars = set(s)
    max_length = 0

    for char1, char2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c in (char1, char2)]
        if is_alternating(filtered):
            max_length = max(max_length, len(filtered))

    return max_length

if __name__ == '__main__':

    l = int(input().strip())
    s = input().strip()

    result = alternate(s)

    print(result)