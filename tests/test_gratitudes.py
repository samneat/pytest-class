from lib.gratitudes import *

def test_formatting():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "

def test_multiple_adds():
    gratitudes = Gratitudes()
    gratitudes.add('Bikes')
    gratitudes.add('Running')
    gratitudes.add('Rugby')
    gratitudes.add('Football')
    result = gratitudes.format()
    assert result == "Be grateful for: Bikes, Running, Rugby, Football"
