import functools


def comparator(a, b):

    if a == b:
        return 0

    a = str(a)
    b = str(b)

    if int(a+b) < int(b+a):
        return 1
    else:
        return -1


def list_to_string(_list):
    return ''.join(map(str, _list))


def largest_int(_input):
    _output = sorted(_input, key=functools.cmp_to_key(comparator))
    return list_to_string(_output)

