# https://fellowship.hackbrightacademy.com/materials/challenges/anagram-of-palindrome/index.html

"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    char_count_dict = {}

    for char in word:
        if char_count_dict.get(char) == None:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    
    # It's a palindrome if the number of odd-counts is either 0 or 1

    odd_count = 0

    for value in char_count_dict.values():
        if value % 2 != 0:
            odd_count += 1
    
    return odd_count == 0 or odd_count == 1


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
