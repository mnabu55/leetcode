'''
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
'''


class CombinationIterator:
    combination = []

    def __init__(self, characters: str, combinationLength: int):
        for i in range(0, len(characters) - (combinationLength - 1)):
            for j in range(i, len(characters) - (combinationLength - 1) ):
                self.combination.append(characters[j:(j + combinationLength)])
        print("combination: ", self.combination)

    def next(self) -> str:
        return self.combination.pop(0)

    def hasNext(self) -> bool:
        return len(self.combination) != 0


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
assert obj.next() == "ab", "case01, ng"
assert obj.hasNext() == True, "case02, ng"
assert obj.next() == "ac", "case03, ng"
assert obj.hasNext() == True, "case04, ng"
assert obj.next() == "bc", "case05, ng"
assert obj.hasNext() == False, "case06, ng"
