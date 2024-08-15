class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = self.recurse(word1, word2, {})
        cmbstr = word1 + word2
        return memo[cmbstr]
    def recurse(self, word1: str, word2: str, memo: dict) -> dict:
        comb_str = word1 + word2
        if memo.get(comb_str):
            return memo
        elif len(word1) == 0 and len(word2) == 0:
            memo[""] = 0
            return memo
        elif len(word1) == 0:
            memo = self.recurse(word1, word2[1:], memo)
            ncstr = word1 + word2[1:]
            memo[comb_str] = memo[ncstr] + 1
        elif len(word2) == 0:
            memo = self.recurse(word1[:-1], word2, memo)
            ncstr = word1[:-1] + word2
            memo[comb_str] = memo[ncstr] + 1
        elif word1[0] == word2[0]:
            i = 0
            ln1 = len(word1)
            ln2 = len(word2)
            while i < min(ln1, ln2) and word1[i] == word2[i]:
                i += 1
            memo = self.recurse(word1[i:], word2[i:], memo)
            ncstr = word1[i:] + word2[i:]
            memo[comb_str] = memo[ncstr]
        elif len(word1) < len(word2):
            nword1 = word2[0] + word1
            ncstr1 = nword1 + word2
            memo = self.recurse(nword1, word2, memo)
            nword1 = word2[0] + word1[1:]
            memo = self.recurse(nword1, word2, memo)
            ncstr2 = nword1 + word2
            memo[comb_str] = min(memo[ncstr1], memo[ncstr2]) + 1
        elif len(word1) > len(word2):
            nword1 = word1[1:]
            memo = self.recurse(nword1, word2, memo)
            ncstr1 = nword1 + word2
            nword1 = word2[0] + word1[1:]
            memo = self.recurse(nword1, word2, memo)
            ncstr2 = nword1 + word2
            nword1 = word2[0] + word1
            memo = self.recurse(nword1, word2, memo)
            ncstr3 = nword1 + word2
            memo[comb_str] = min(memo[ncstr1], memo[ncstr2], memo[ncstr3]) + 1
        elif len(word1) == len(word2):
            nword1 = word2[0] + word1[1:]
            memo = self.recurse(nword1, word2, memo)
            ncstr1 = nword1 + word2
            nword1 = word2[0] + word1
            memo = self.recurse(nword1, word2, memo)
            ncstr2 = nword1 + word2
            memo = self.recurse(word1[1:], word2, memo)
            ncstr3 = word1[1:] + word2
            memo[comb_str] = min(memo[ncstr1], memo[ncstr2], memo[ncstr3]) + 1
        return memo