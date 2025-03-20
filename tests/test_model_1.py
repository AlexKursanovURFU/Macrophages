from src.model import SIR
def test_SIR():
    assert SIR([0,0,0],0,(0,0)) == [0,0,0]