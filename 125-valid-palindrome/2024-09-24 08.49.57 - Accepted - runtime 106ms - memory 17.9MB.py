class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strlwr = 'abcdefghijklmnopqrstuvwxyz0123456789'
        st = set([i for i in strlwr])
        pal = ""
        for c in s:
            if c.lower() in st:
                pal += c.lower()
        rpal = [pal[i] for i in range(len(pal)-1, -1, -1)]
        rpals = "".join(rpal)
        return rpals == pal