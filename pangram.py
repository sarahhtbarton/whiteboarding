# https://fellowship.hackbrightacademy.com/materials/challenges/pangram/index.html

"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    alphabet_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    sentence_set = set()

    for char in sentence:
        if char in alphabet_set:
            sentence_set.add(char.lower())
    
    return alphabet_set == sentence_set

    # Notes:
    # create an empty set with `set()` not `set{}`
    # sets are unordered, so two sets can equal each other even if not in same order


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
