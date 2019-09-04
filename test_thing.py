from thing import Thing

def test_value():
    t = Thing(42)
    assert t.Value == 42
def test_str():
    t = Thing(42)
    assert str(t) == "Thing: 42"