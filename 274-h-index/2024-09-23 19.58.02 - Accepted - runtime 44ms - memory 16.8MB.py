class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = len(citations)
        cnt = 0
        for i in citations:
            while i < h and cnt < h:
                h -= 1
            if cnt == h:
                return h
            cnt += 1
        return h