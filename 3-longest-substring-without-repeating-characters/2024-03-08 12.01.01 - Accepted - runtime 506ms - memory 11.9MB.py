class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = set()
        ln = 0
        maxln = 0
        arr = [c for c in s]
        i = 0
        while (arr and i < len(arr)):
            c = arr[i]
            ln += 1
            if c in st:
                ln = 0
                st = set()
                arr.pop(0)
                i = 0
                continue
            if ln > maxln:
                maxln = ln
            st.add(c)
            i += 1
        return maxln


        