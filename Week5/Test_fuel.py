from Fuel_w5 import convert, gauge

def test1():
    assert convert('3/4') == '75%'
def test2():
    assert gauge('99/100') == 'F'
def test3():
    assert gauge('1/100') == 'E'
def test4():
    assert convert('1/0') == 'Error due to zero division'
def test5():
    assert convert('cat') == 'Invalid input'