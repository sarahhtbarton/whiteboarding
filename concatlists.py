# https://fellowship.hackbrightacademy.com/materials/challenges/concat-lists/index.html

"""Given two lists, concatenate the second list at the end of the first.

For example, given ``[1, 2]`` and ``[3, 4]``::

    >>> concat_lists([1, 2], [3, 4])
    [1, 2, 3, 4]

It should work if either list is empty::

    >>> concat_lists([], [1, 2])
    [1, 2]

    >>> concat_lists([1, 2], [])
    [1, 2]

    >>> concat_lists([], [])
    []
"""


def concat_lists(list1, list2):
    """Combine lists."""
    
    concatenated = list1 + list2
    return concatenated
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
