class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, string):
        size = len(string)
        if size == 0:
            self.node.isEnd = True
            return
        else:
            if string[0] in self.node.child:
                self.node.child[string[0]].insert(string[1:])
            else:
                self.node.child[string[0]] = Trie()
                self.node.child[string[0]].insert(string[1:])
        return

    def search(self, word):
        temp = self.node
        while self.node.isEnd is False:
            if word[i] not in temp.child:
                return False
            else:
                if temp.child
        if temp.isEnd == True:
            return True
        else:
            return False


trie = Trie()
trie.insert("Jain")
trie.insert("Jain Paul")
trie.insert("Jain Paul Maliyakkal")
print(trie.search("a"))
