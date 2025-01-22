class TestClass:
    def test_type(self):
        assert type(1) == int

    def test_a2(self):
        assert type(1.3) == float

    def test_a3(self):
        assert type('abc') == str

    def test_a4(self):
        assert type([1,2,3]) == list

    def test_a5(self):
        assert type((1,2,3)) == tuple

    def test_a6(self):
        assert str.upper('abc') == 'ABC'