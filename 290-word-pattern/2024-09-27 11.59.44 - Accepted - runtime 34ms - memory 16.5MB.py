class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()
        if len(s_arr) != len(pattern):
            return False
        
        i = 0
        p_dct = {}
        s_st = set()
        while i < len(s_arr):
            v = p_dct.get(pattern[i])
            if v and v != s_arr[i]:
                return False
            elif v is None and s_arr[i] in s_st:
                return False
            elif v is None:
                p_dct[pattern[i]] = s_arr[i]
                s_st.add(s_arr[i])
            i += 1
        return True