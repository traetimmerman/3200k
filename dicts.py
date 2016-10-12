def hist(s):
    """returns the histogram of the characters in s

    >>> hist("AAGGT")
    {'A': 2, 'T': 1, 'G': 2}

    >>> hist("!!xx")
    {'!': 2, 'x': 2}

    """
    solution = {}
    for char in s:
        if char not in solution:
            solution[char] = 1
        else:
            solution[char] += 1
    return solution


def str_to_int(s):
    """converts a string to an integer value

    >>> str_to_int('s')
    115

    >>> str_to_int('st!ll')
    11511633108108L

    hint: the built in ord and chr functions

    """
    result = ''
    for char in s:
        result += str(ord(char))
    return int(result)


def null_list(length):
    """return a list of all None values of given length

    >>> null_list(3)
    [None, None, None]

    >>> null_list(1)
    [None]

    """
    return [None] * length
    
if __name__ == "__main__":
    import doctest
doctest.testmod()
