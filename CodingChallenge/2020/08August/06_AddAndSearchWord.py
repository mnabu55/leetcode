'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''


class WordDictionary:

    def __init__(self):
        self.word_dict = {}

    def addWord(self, word: str) -> None:
        if word not in self.word_dict:
            self.word_dict[word] = 1
        else:
            self.word_dict[word] += 1

    def search(self, word: str) -> bool:
        return word in self.word_dict


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word = "hello"
obj.addWord(word)
print(obj.search(word))



