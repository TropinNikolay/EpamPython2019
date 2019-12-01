def collatz_steps(n):
    assert n > 0 and isinstance(n, int)
    counter = 0

    def wrapper(n):
        nonlocal counter
        if n == 1:
            return counter
        elif n % 2 == 0:
            counter += 1
            return wrapper(n / 2)
        else:
            counter += 1
            return wrapper(3 * n + 1)

    return wrapper(n)


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(27) == 111
assert collatz_steps(1000000) == 152
