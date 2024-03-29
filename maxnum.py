# https://fellowship.hackbrightacademy.com/materials/challenges/max-num/index.html?

"""Return the largest integer in a list.

Given a list of integers, return the largest. Do not use the built in 'max' method.

For example::

    >>> max_num([1, 3, 2, 4, 7, 2])
    7

    >>> max_num([5, 5, 5])
    5

    >>> max_num([10])
    10

    >>> max_num([-1, -2, -3])
    -1

    >>> max_num([-10, 0])
    0

"""


def max_num(num_list):
    """Returns largest integer from given list"""

    max_num = num_list[0]

    for num in num_list:
        if num > max_num:
            max_num = num
    
    return max_num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO YOU!\n")
