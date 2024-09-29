class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        ninths = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        i = 0
        for row in board:
            rst = set()
            for j in range(9):
                nin = (3)*(i // 3) + j // 3
                if row[j] == ".":
                    continue
                elif row[j] in rst:
                    return False
                elif row[j] in cols[j]:
                    return False
                elif row[j] in ninths[nin]:
                    return False
                else:
                    rst.add(row[j])
                    cols[j].add(row[j])
                    ninths[nin].add(row[j])
            i += 1
        return True

                