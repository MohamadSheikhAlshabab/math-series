from math_series.series import lucas_check , fibonacci , sum_series 

def test_lucas_0():
    expected = 2
    actual = lucas_check(0)
    assert actual == expected

def test_lucas_1():
    expected = 1
    actual = lucas_check(1)
    assert actual == expected

def test_lucas_2():
    expected = 3
    actual = lucas_check(2)
    assert actual == expected

def test_lucas_3():
    expected = 4
    actual = lucas_check(3)
    assert actual == expected

def test_lucas_4():
    expected = 7
    actual = lucas_check(4)
    assert actual == expected

def test_lucas_5():
    expected = 11
    actual = lucas_check(5)
    assert actual == expected

def test_lucas_6():
    expected = 18
    actual = lucas_check(6)
    assert actual == expected

def test_lucas_7():
    expected = 29
    actual = lucas_check(7)
    assert actual == expected

def test_lucas_8():
    expected = 47
    actual = lucas_check(8)
    assert actual == expected

def test_lucas_9():
    expected = 76
    actual = lucas_check(9)
    assert actual == expected

def test_lucas_10():
    expected = 123
    actual = lucas_check(10)
    assert actual == expected

def test_lucas_11():
    expected = 199
    actual = lucas_check(11)
    assert actual == expected

def test_fibonacci_0():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fibonacci_1():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fibonacci_2():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_fibonacci_3():
    expected = 2
    actual = fibonacci(3)
    assert actual == expected

def test_fibonacci_4():
    expected = 3
    actual = fibonacci(4)
    assert actual == expected

def test_fibonacci_5():
    expected = 5
    actual = fibonacci(5)
    assert actual == expected

def test_fibonacci_6():
    expected = 8
    actual = fibonacci(6)
    assert actual == expected

def test_fibonacci_7():
    expected = 13
    actual = fibonacci(7)
    assert actual == expected

def test_fibonacci_8():
    expected = 21
    actual = fibonacci(8)
    assert actual == expected

def test_fibonacci_9():
    expected = 34
    actual = fibonacci(9)
    assert actual == expected

def test_fibonacci_10():
    expected = 55
    actual = fibonacci(10)
    assert actual == expected

def test_fibonacci_11():
    expected = 89
    actual = fibonacci(11)
    assert actual == expected

def test_fibonacci_12():
    expected = 144
    actual = fibonacci(12)
    assert actual == expected

def test_fibonacci_13():
    expected = 233
    actual = fibonacci(13)
    assert actual == expected

def test_fibonacci_14():
    expected = 377
    actual = fibonacci(14)
    assert actual == expected

def test_fibonacci_15():
    expected = 610
    actual = fibonacci(15)
    assert actual == expected

def test_fibonacci_16():
    expected = 987
    actual = fibonacci(16)
    assert actual == expected

def test_sum_0():
    expected = 2
    actual = sum_series(0)
    assert actual == expected

def test_sum_1():
    expected = 2
    actual = sum_series(1)
    assert actual == expected

def test_sum_2():
    expected = 4
    actual = sum_series(2)
    assert actual == expected

def test_sum_3():
    expected = 6
    actual = sum_series(3)
    assert actual == expected

def test_sum_4():
    expected = 10
    actual = sum_series(4)
    assert actual == expected

def test_sum_5():
    expected = 16
    actual = sum_series(5)
    assert actual == expected

def test_sum_6():
    expected = 26
    actual = sum_series(6)
    assert actual == expected

def test_sum_7():
    expected = 42
    actual = sum_series(7)
    assert actual == expected

def test_sum_8():
    expected = 68
    actual = sum_series(8)
    assert actual == expected

def test_sum_9():
    expected = 110
    actual = sum_series(9)
    assert actual == expected

def test_sum_10():
    expected = 178
    actual = sum_series(10)
    assert actual == expected

def test_sum_11():
    expected = 288
    actual = sum_series(11)
    assert actual == expected