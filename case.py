# https://fellowship.hackbrightacademy.com/materials/challenges/snake-to-camel/index.html

"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""


def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    underscore_index = variable_name.index("_")
    
    camel_case = variable_name[:underscore_index]
    camel_case += variable_name[underscore_index+1:].title()

    return camel_case



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
