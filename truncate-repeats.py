# https://fellowship.hackbrightacademy.com/materials/challenges/truncate-repeats/index.html

"""Truncate repeating characters into one character.

For example:

>>> truncate('aaaaabbbbbcccaaaa')
'abca'

>>> truncate('hi there')
'hi there'

The function should be able to handle special characters, punctuation, and/or
numbers:

>>> truncate('hi   !!! wooow')
'hi ! wow'
"""

def truncate(string):
    """Truncate repeating characters in a string."""

    truncated_string = string[0]
    
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            truncated_string += string[i]

    return truncated_string


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
