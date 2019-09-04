from thing import Thing

def test_value():
    t = Thing(42)
    assert t.Value == 42
