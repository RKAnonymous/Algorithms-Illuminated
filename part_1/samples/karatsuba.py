from typing import Any, Set, Tuple, Union


def normalize(x: str, y: str) -> Union[str, any]:
    diff = len(x) - len(y)

    if diff > 0:
        y = "0" * diff + str(y)
        return x, y

    x = "0" * abs(diff) + x
    # print(x, y)
    return x, y


def karatsuba(x: int, y: int):
    x = str(x)
    y = str(y)
    if len(x) % 2 != 0 or len(y) % 2 != 0:
        x, y = normalize(x, y)

    n = len(x)
    mid = n//2

    if n == 1:
        return int(x) * int(y)
    else:
        # a, b := first and second halves of x
        a = int(x[:mid])
        b = int(x[mid:])

        # c, d := first and second halves of y
        c = int(y[:mid])
        d = int(y[mid:])

        # compute p := a + b and q := c + d using grade - school addition
        p = a + b
        q = c + d

        # recursively compute ac := a · c, bd := b · d, and pq := p · q
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        pq = karatsuba(p, q)

        # compute adbc := pq - ac - bd using grade - school addition
        adbc = pq - ac - bd

        # compute 10^n · ac + 10^n/2 · adbc + bd using grade-school addition and return the result
        result = 10 ** n * ac + 10 ** (n / 2) * adbc + bd
        return result

print(karatsuba(2718281828459045235360287471352662497757247093699959574966967627, 3141592653589793238462643383279502884197169399375105820974944592))