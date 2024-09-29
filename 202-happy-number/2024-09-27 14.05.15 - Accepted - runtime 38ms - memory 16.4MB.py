class Solution:
    def isHappy(self, n: int) -> bool:
        ns = str(n)
        st = set()
        while n != 1:
            st.add(ns)
            n = 0
            for c in ns:
                n += (int(c))**2
            ns = str(n)
            if ns in st:
                return False
        return True
