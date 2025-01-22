def test_hello():
    expected = "Hello World"
    assert expected == "Hello World"

def test_fail():
    expected = "Hello World"
    assert expected == "Hellso World", 'failed test internal'

def test_a1():
    assert 9/5 == 1.8, 'failed test internal'

def test_a2():
    assert 'a'in 'Santa', 'failed test internal'