def test_hello():
    expected = "Hello World"
    assert expected == "Hello World"

def test_fail():
    expected = "Hello World"
    assert expected == "Hello World", 'failed test internal'

def test_a1():
    print("This is my first test")
    assert 5 + 5 == 0
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def test_a2():
    assert 'a'in 'Santa', 'failed test internal'