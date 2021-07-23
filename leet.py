# https://fellowship.hackbrightacademy.com/materials/challenges/leet-speak/index.html

"""Translate phrase to "leet-speak".

For example::

    >>> translate_leet("Hi Balloonicorn")
    'Hi B@1100nic0rn'

    >>> translate_leet("Hackbright is the Shizzle")
    'H@ckbrigh7 i5 7h3 5hizz13'

"""


def translate_leet(phrase):
    """Translates input into "leet-speak"."""

    leet_dict = {'a': '@', 'l': '1', 'o': '0', 't': '7', 's': '5', 'e': '3', 'S': '5'}
    leet_phrase = ''

    for char in phrase:
        if leet_dict.get(char) is not None:
            leet_phrase = leet_phrase + leet_dict[char]
        else:
            leet_phrase = leet_phrase + char
    
    return leet_phrase

    # Notes:
    # Cleaner way to do this:
    # for char in phrase:
    #     translated += leet_speak.get(char.lower(), char)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. AE3S0M3!\n")
