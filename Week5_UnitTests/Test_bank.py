from Bank_w5 import bank
def test_bank1():
    assert bank('hello') == '0$'
def test_bank2():
    assert bank('Hey') == '20$'
def test_bank3():
    assert bank('Whatever') == '100$'