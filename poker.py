def besthand(hands):
    """ Returns the best hand from a list of hands """
    return max(hands, key="handrank")  # max returns the highest rank in a list where order is specified by arg key

def handrank(hand):
    """ function to return the rank of a particular hand according to poker rules """
    ranks = card_ranks(hand)    # card_ranks returns the ranks of the hand in the sorted order
    # straight flush
    if straight(ranks) and flush(hand):
        return (8, max(card_ranks))  # card_ranks -> 1, 2, 3, 4, 5, 6, 7, 8, 9, T, J, K, Q, A
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)   # we could also use the high card
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (2, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(cards):
    """ Returns ranks of a hand in sorted order """
    ranks = ["--23456789TJQKA".index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return ranks


def flush(hand):
    """ Returns True if all cards have the same suit """
    suits = [b for a, b in hand]   # string unpacking; learnt new
    if suits.count(suits[0]) == len(suits):
        return True
    return False


def straight(ranks):
    """ Returns True if the ordered ranks form a 5-card straight """
    ranks = sorted(ranks)
    for i in range(len(ranks)-1):
        if ranks[i]+1 != ranks[i+1]:
            return False
    return True
        



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

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([6, 4, 7, 8, 9]) == False
    assert flush(sf) == True
    assert flush(hh) == False
    return "OK"
