from src.parameters import get_param

def test_get_param():
    assert get_param() == (0.1, 0.05)