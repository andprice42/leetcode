class Solution:
    def kthCharacter(self, k: int) -> str:
        abcs = 'abcdefghijklmnopqrstuvwxyza'
        ad = {}
        for i in range(1, len(abcs)):
            ad[abcs[i-1]] = abcs[i]
        
        word = "a"
        while len(word) < k:
            aw = ""
            for c in word:
                aw += ad[c]
            word += aw
        return word[k-1]