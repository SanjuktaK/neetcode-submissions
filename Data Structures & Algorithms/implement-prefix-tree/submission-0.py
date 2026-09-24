class TrieNode:
    def __init__(self):
        self.link = [None]*26
        self.flag = False
    def containskey(self,ch):
        return self.link[ord(ch)-ord('a')] is not None
    def get(self,ch):
        return self.link[ord(ch)-ord('a')]
        
    def put(self,ch, node):
        self.link[ord(ch)-ord('a')] = node
    def setEnd(self):
        self.flag = True
    def isEnd(self):
        return self.flag
    
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.containskey(ch):
                curr.put(ch,TrieNode())
            curr = curr.get(ch)
        curr.setEnd()

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if not curr.containskey(ch):
                return False
            curr = curr.get(ch)
        return curr.isEnd() == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if not curr.containskey(ch):
                return False
            curr = curr.get(ch)
        return True
        
        