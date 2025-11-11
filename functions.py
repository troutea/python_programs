def fibonacci(n: int) -> int:
    """Return the n the """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    for f in range(n - 1):
        result = (n_minus2 + n_minus1)
        n_minus2 = n_minus1
        n_minus1 = result

    return result


x = fibonacci(10)
print(x)
