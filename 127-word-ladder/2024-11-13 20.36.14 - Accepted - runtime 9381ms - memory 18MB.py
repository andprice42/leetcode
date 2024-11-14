class lnde:
    def __init__(self, val: tuple, next: Optional['lnde']=None):
        self.val = val
        self.next = next
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        fq = lnde((beginWord, 1))
        tail = fq
        wordset = set(wordList)
        while fq:
            fstr = fq.val[0]
            depth = fq.val[1]
            if fstr == endWord:
                return depth
            hit_list = []
            for v in wordset:
                if sum([1 for i in range(len(fstr)) if fstr[i] == v[i]]) == (len(fstr) - 1):
                    tail.next = lnde((v, depth+1))
                    tail = tail.next
                    hit_list.append(v)
            for h in hit_list:
                wordset.remove(h)
            fq = fq.next
        return 0