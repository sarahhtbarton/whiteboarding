# https://fellowship.hackbrightacademy.com/materials/challenges/pig-latin/index.html

"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
    
    phrase_list = phrase.split()
    pig_latin_phrase = []

    for word in phrase_list:
        if word[0] not in ('a', 'e', 'i', 'o', 'u'):
        new_word = word[1:] + word[0] + 'ay'
        pig_latin_phrase.append(new_word)
        
        else:
        new_word = word + 'yay'
        pig_latin_phrase.append(new_word)
    
    return(" ".join(pig_latin_phrase))


    # Takeaways Lessons:
    # - Cant use pop with a string -- use string splitting
    # - join format is " ".join(the_list)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. REATGAY OBJAY!\n")
