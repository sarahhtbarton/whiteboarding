# https://fellowship.hackbrightacademy.com/materials/challenges/show-evens/index.html

"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

"""


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    evens_list = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            evens_list.append(i)
    
    return evens_list


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
