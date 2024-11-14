class Graph:
    def __init__(self, val: int):
        self.val = val
        self.fq = {}
class Trie:

    def __init__(self):
        self.fq = {}

    def insert(self, word: str) -> None:
        if self.fq.get(word[0]):
            self.fq[word[0]] = self.recurseInsert(word[1:], self.fq[word[0]])
        else:
            self.fq[word[0]] = self.recurseInsert(word[1:], Graph(word[0]))
    
    def recurseInsert(self, word: str, g: Optional['Graph']) -> Optional['Graph']:
        if len(word) == 0 and g.fq.get('0') is None:
            g.fq['0'] = Graph('0')
            return g
        elif len(word) == 0:
            return g
        elif g.fq.get(word[0]):
            g.fq[word[0]] = self.recurseInsert(word[1:], g.fq[word[0]])
        else:
            g.fq[word[0]] = self.recurseInsert(word[1:], Graph(word[0]))
        return g
    
    def search(self, word: str) -> bool:
        if self.fq.get(word[0]) is None:
            return False
        return self.recurseSearch(word[1:], self.fq.get(word[0]), True)

    def recurseSearch(self, word: str, g: Optional['Graph'], exact: bool) -> bool:
        if len(word) == 0 and exact:
            if g.fq.get('0'):
                return True
            else:
                return False
        elif len(word) == 0:
            return True
        elif g.fq.get(word[0]):
            return self.recurseSearch(word[1:], g.fq[word[0]], exact)
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if self.fq.get(prefix[0]) is None:
            return False
        return self.recurseSearch(prefix[1:], self.fq.get(prefix[0]), False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)