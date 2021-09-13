class TrieNode:
    def __init__(self):
        self.data = None
        self.next = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, data):
        n = self.root
        for i in word:
            if i not in n.next:
                n.next[i] = TrieNode()
            n = n.next[i]
        n.data = data

    def search(self, word):
        n = self.root
        for i in word:
            if i not in n.next:
                return False
            else:
                n = n.next[i]
        return n.data

    def match(self, line, index):
        linelen = len(line)
        n = self.root
        while index < linelen:
            if line[index] in n.next:
                n = n.next[line[index]]
                index = index + 1
            else:
                break
        return (n.data, index)
