class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ret_str = ""
        while i < max(len(word1), len(word2)):
            if i < len(word1):
                ret_str += word1[i]
            if i < len(word2):
                ret_str += word2[i]
            i += 1
        return ret_str