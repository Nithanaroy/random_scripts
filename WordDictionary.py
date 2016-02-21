"""
Leetcode: https://leetcode.com/problems/add-and-search-word-data-structure-design/
"""

from sets import Set


class Node:
    def __init__(self):
        self.c = None
        self.children = Set()
        self.final = False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.r = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        n = self.r
        for c in word:
            cRef = self.findC(n, c)
            if not cRef:
                cNode = Node()
                cNode.c = c
                n.children.add(cNode)
                n = cNode
            else:
                n = cRef
        n.final = True

    def findC(self, n, c):
        """
        finds c in children for node, n
        """
        for ch in n.children:
            if ch.c == c:
                return ch
        return None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = self.r
        return self.searchHelper(word, n)

    def searchHelper(self, word, n):
        for i, c in enumerate(word):
            if c == '.':
                for ch in n.children:
                    if self.searchHelper(word[i + 1:], ch):
                        return True
                return False  # handles dot not matching any character also
            else:
                cRef = self.findC(n, c)
                if not cRef:
                    return False
                else:
                    n = cRef

        if n.final or len(n.children) == 0:  # we want complete match not sub string
            return True

        return False


def main():
    w = WordDictionary()
    w.addWord("a")
    w.addWord("ab")
    print w.search("a")
    print w.search("a.")
    print w.search("ab")
    print w.search(".a")
    print w.search(".b")
    print w.search("ab.")
    print w.search(".")
    print w.search("..")


if __name__ == '__main__':
    main()

    # Your WordDictionary object will be instantiated and called as such:
    # wordDictionary = WordDictionary()
    # wordDictionary.addWord("word")
    # wordDictionary.search("pattern")
