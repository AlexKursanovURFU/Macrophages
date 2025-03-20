from src.model import SIR


def test_SIR():
    assert SIR([0,0,0],0,(1,1)) == [0,0,0]
    assert SIR([1,1,1],0,(1,1)) == [-1,0,1]
