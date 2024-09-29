class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.split()
        return " ".join([s_arr[i] for i in range(len(s_arr)-1, -1, -1)])