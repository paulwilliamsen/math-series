from series import fibonacci, lucas, sum_series


def test_first():
  actual = fibonacci(1)
  expected = 0
  assert actual == expected

def test_second():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_third():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_four():
  actual = lucas(2)
  expected = 1
  assert actual == expected

def test_five():
  actual = lucas(4)
  expected = 4
  assert actual == expected

def test_six():
  actual = lucas(3)
  expected = 3
  assert actual == expected

def test_sum_series_fib1():
    actual = sum_series(1, 0, 1)
    expected = 0
    assert actual == expected
def test_sum_series_fib2():
    actual = sum_series(4, 0, 1)
    expected = 2
    assert actual == expected
# def test_sum_series_fib3():
#     actual = sum_series(8, 0, 1)
#     expected = 13
#     assert actual == expected