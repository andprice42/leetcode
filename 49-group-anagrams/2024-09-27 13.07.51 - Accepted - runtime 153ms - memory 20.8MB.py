class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            st = set()
            for c in s:
                if c in st:
                    i = 0
                    stay = True
                    while stay:
                        nc = "{0}{1}".format(c, i)
                        if nc not in st:
                            stay = False
                            st.add(nc)
                        else:
                            i += 1
                else:
                    st.add(c)
            lst = list(st)
            lst.sort()
            tst = tuple(lst)
            if mp.get(tst):
                mp[tst].append(s)
            else:
                mp[tst] = [s]
        return [v for k, v in mp.items()]