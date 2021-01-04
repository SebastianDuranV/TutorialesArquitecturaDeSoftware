from romanos import convertToRomans

def test_romans():
    assert convertToRomans(10) == 'X'
    assert convertToRomans(40) == 'XL'
    assert convertToRomans(101) == 'CI'