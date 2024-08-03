class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if words is None or len(words) == 0:
            return []
        ln = len(words[0])
        words.sort()
        wrdsln = len(words)
        wrd_set = set(words)
        sols = []
        for i in range(len(s)):
            if s[i:i+ln] in wrd_set:
                ptl_sol_lst = [s[j:j+ln] for j in range(i, i+(wrdsln*ln), ln)]
                ptl_sol_lst.sort()
                if ptl_sol_lst == words:
                    sols.append(i)
        return sols 


