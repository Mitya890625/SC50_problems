from Twttr_w5 import shorten

def test_twttr():
    assert shorten('Mitya') == 'Mty'
    assert shorten('MITYA') == 'MTY'
    assert shorten('How are you?') == 'Hw r y?'
