from lib.counter import *

def test_counts_to():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == 'Counted to 10 so far'