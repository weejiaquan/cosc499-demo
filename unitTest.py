from numberSort import numSort
from wordSort import wordSort

def numberSortTest():
    numbers = [6, 9, 3, 1]
    assert numSort(numbers) == "[1, 3, 6, 9]", "Should be [1, 3, 6, 9]"

def wordSortTest():
    words = ["d","b","a","c"]
    assert numSort(words) == "['a', 'b', 'c', 'd']", "Should be ['a', 'b', 'c', 'd']"

if __name__ == "__main__":
    numberSortTest()
    wordSortTest()
    print("Everything passed")