# https://fellowship.hackbrightacademy.com/materials/challenges/is-palindrome/index.html

"""Is this word a palindrome?

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

Treat spaces and uppercase letters normally:

    >>> is_palindrome("Racecar")
    False
"""


def is_palindrome(word):
    """Return True/False if this word is a palindrome."""

    word_reversed = word[::-1]

    return word == word_reversed

    # Notes:
    # Another way to solve:
    # for i in range(len(word)):
    #     if word[i] != word[len(word) - 1 - i]:
    #         return False
    
    # return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!")
