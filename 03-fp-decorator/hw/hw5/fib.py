def power(x, n, I, mult):
    """
    Returns x to the n power. Assumes that I is the identity matrix which multiplies with mult, and type(n) is int
    """
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = power(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(x, y)
        return y


def identity_matrix(n):
    """ Returns the identity matrix n by n """
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]


def matrix_multiply(A, B):
    BT = list(zip(*B))
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in BT] for row_a in A]


def fib(n):
    F = power([[1, 1], [1, 0]], n, identity_matrix(2), matrix_multiply)
    return F[0][1]
