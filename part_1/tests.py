from .samples import karatsuba


def test_karatsuba():
    assert karatsuba(1234, 5432) == 6703088
    assert karatsuba(123, 5432) == 668136
    # assert karatsuba(12345, 6789) == 83810205
    # assert karatsuba(12, 5432) == 65184
    # assert karatsuba(100, 14) == 1400
    # assert karatsuba(100, 2) == 200
    assert karatsuba(0, 0) == 0
    assert karatsuba(0, 1) == 0
    # assert karatsuba(0, 1000) == 0
    # assert karatsuba(10, 1000) == 10000




