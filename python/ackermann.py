

class InvalidInputException(Exception):
    pass


def ackermann_peter(m, n):
    """
    The two argument variant of the Ackermann function.
    """
    if m < 0 or n < 0:
        raise InvalidInputException("m and n both need to be greater than 0")
    elif m == 0:
        return n + 1
    elif n == 0:
        return ackermann_peter(m - 1, 1)
    else:
        return ackermann_peter(m - 1, ackermann_peter(m, n - 1))


def ackermann_peter_faster(m, n):
    """

    """
    if m < 0 or n < 0:
        raise InvalidInputException("m and n both need to be greater than 0")
    elif m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2 * n + 3
    elif m == 3:
        try:
            result = (1 << (n + 3)) - 3
        except OverflowError:
            result = (2 ** (n + 3)) - 3
        return result
    elif n == 0:
        return ackermann_peter_faster(m - 1, 1)
    else:
        return ackermann_peter_faster(m - 1, ackermann_peter_faster(m, n - 1))



def ackermann_peter_faster_memo(m, n, memo={(4, 1): 65533, (3, 1): 13}):
    """

    """
    if m < 0 or n < 0:
        raise InvalidInputException("m and n both need to be greater than or equal to 0")
    elif m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2 * n + 3
    elif (m, n) in memo:
        return memo[(m, n)]
    elif m == 3:
        try:
            result = (1 << (n + 3)) - 3
        except OverflowError:
            result = (2 ** (n + 3)) - 3
        memo[(m, n)] = result
        return result
    elif n == 0:
        result = ackermann_peter_faster_memo(m - 1, 1)
        memo[(m, n)] = result
        return result
    else:
        new_n = ackermann_peter_faster_memo(m, n - 1)
        result = ackermann_peter_faster_memo(m - 1, new_n)
        memo[(m, n)] = result
        return result


# def print_ackermann_peter_calls(m, n):
#     format_string = "ackermann_peter(%d, %s)"
#     n_string = str(n)
#     ms = [m]
#     ns = [n]
#     keep_printing = True
#     while keep_printing:
#         m2 = ms.pop()
#         m1 = m2 - 1
#         n1 = ns.pop()
#         if m2 == 0 and len(ms) == 0 and len(ns) == 0:
#             print n1
#             keep_printing = False
#         elif m2 == 0
