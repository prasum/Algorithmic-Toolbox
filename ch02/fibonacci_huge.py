# Uses python3


def fibonacci_mod_m(n, m):
    """The remainder of F[n] when divided by m.
    Given two integers n and m, output F[n] mod m (that is, the remainder of
    F[n] when divided by m).
    The algorithm uses another matrix representation of Fibonacci sequence.
    Since the algorithm make recursive calls in four places of the code,
    it turns out some of the elements are calculated many times. To make
    the algorithm work faster, already calculated items are placed into a cache.
    Samples:
    >>> fibonacci_mod_m(281621358815590, 30524)
    11963
    """
    cache = {0: 0, 1: 1}

    def fib_m(n):
        if n in cache:
            return cache[n]

        if n % 2 == 0:
            fib_half_n = fib_m(n // 2)
            result = (2 * fib_m(n // 2 - 1) + fib_half_n) * fib_half_n
        else:
            result = fib_m((n + 1) // 2) ** 2 + fib_m((n - 1) // 2) ** 2

        cache[n] = result = result % m
        return result

    return fib_m(n)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_mod_m(n, m))
