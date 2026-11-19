class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                # create new node under current root node
                node.children[ch] = TrieNode()
            # create current children node as new node
            node = node.children[ch]
        
        node.isEnd = True



    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True
        
        