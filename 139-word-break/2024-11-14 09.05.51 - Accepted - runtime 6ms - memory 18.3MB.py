class Trie:
    def __init__(self, val: str):
        self.val = val
        self.fq = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tm = {}
        # build trie to represent wordDict
        for word in wordDict:
            # keep track of first character in word
            if tm.get(word[0]) is None:
                tnde = Trie(word[0])
                tm[word[0]] = tnde
            else:
                tnde = tm[word[0]]
            for i in range(1, len(word)):
                c = word[i]
                if tnde.fq.get(c) is None:
                    nnde = Trie(c)
                    tnde.fq[c] = nnde
                else:
                    nnde = tnde.fq[c]
                tnde = nnde
            tnde.fq['0'] = Trie('0')
        if tm.get(s[0]) is None:
            return False
        bln, memo = self.dp(s, (0, 1), {}, tm.get(s[0]), tm)
        return bln
    
    def dp(self, s: str, rng: tuple, memo: dict, trie: Optional['Trie'], tdict: dict) -> tuple:
        i = rng[0]
        j = rng[1]
        if memo.get((i,j)):
            return (False, memo)
        elif trie.val == '0':
            memo[(i, j)] = (i, j)
            i = j
            j += 1
            if i == len(s):
                return (True, memo)
            else:
                trie = tdict.get(s[i])
            if trie is None:
                memo[(i, j)] = True
                return (False, memo)
            elif memo.get((i, j)) is None:
                bln, memo = self.dp(s, (i, j), memo, trie, tdict)
                if bln:
                    return (bln, memo)
            else:
                return (False, memo)
        bln = False
        if trie.fq.get('0'):
            bln, memo = self.dp(s, (i, j), memo, trie.fq.get('0'), tdict)
        if bln is False and j < len(s):
            ntrie = trie.fq.get(s[j])
            if ntrie:
                bln, memo = self.dp(s, (i, j+1), memo, ntrie, tdict)
        memo[(i,j)] = True
        return (bln, memo)


            
            