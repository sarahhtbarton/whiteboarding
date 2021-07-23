# https://fellowship.hackbrightacademy.com/materials/challenges/has-more-vowels/index.html

"""Does word contain more vowels than non-vowels?

If the word is over half vowels, it should return True:

    >>> has_more_vowels("moose")
    True

If it's half vowels (or less), it's false:

    >>> has_more_vowels("mice")
    False

    >>> has_more_vowels("graph")
    False

Don't consider "y" as a vowel:

    >>> has_more_vowels("yay")
    False

Uppercase vowels are still vowels:

    >>> has_more_vowels("Aal")
    True
"""


def has_more_vowels(word):
    """Does word contain more vowels than non-vowels?"""

    vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}

    vowel_count = 0
    const_count = 0

    for char in word:
        if char in vowels:
            vowel_count += 1
        else:
            const_count += 1
    
    return vowel_count > const_count

    # Notes:
    # Create a set with {}



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
