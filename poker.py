def besthand(hands):
    """ Returns the best hand from a list of hands """
    return max(hands, key="handrank")  # max returns the highest rank in a list where order is specified by arg key

def handrank(hand):
    """ function to return the rank of a particular hand according to poker rules """
    pass


def test_poker():
    """ tests for functions in poker program """
    tk = "3D 3S 4H 8C AS".split()
    hh = "7D 2S 4H 8C AS".split()
    sf = "6C 7C 8C 9C TC".split()
    assert besthand([tk, hh, sf]) == sf
    assert besthand([tk, hh]) == tk
    assert besthand([hh, hh]) == hh
    assert besthand([hh]) == hh
    assert besthand([sf] + 100*[hh]) == sf

    # 1st 2 is ranking of the hand among all hands, 3 is the rank of the card
    assert handrank(tk) == (2, 3)

    # 1st 6 is the rank of the hand among all hands, 10 is the highest card in hand
    assert handrank(sf) == (8, 10)
    
    return "OK"
