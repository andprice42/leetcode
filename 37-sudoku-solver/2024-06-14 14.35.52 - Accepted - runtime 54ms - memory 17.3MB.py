class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nbd = self.sudokuSolver(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = nbd[i][j]

    def sudokuSolver(self, board: List[List[str]]) -> List[List[str]]:
        bln, rows, cols, nins = self.checkValidSudoku(board)
        if bln is False:
            return board
        bmap = {}
        cnt = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cnt += 1
                    bmap[(i,j)] = {board[i][j]}
                else:
                    nin = (3)*(i // 3) + j // 3
                    bmap[(i,j)] = {str(k) for k in range(1,10) if (str(k) not in rows[i] and str(k) not in cols[j] and str(k) not in nins[nin])}
        solved, board, rows, cols, nins, bmap = self.applyRules(board, rows, cols, nins, bmap)
        if solved is False:
            cnt = 1
            while cnt > 0:
                cnt = 0
                cnts = self.getCounts(bmap)
                for i in range(9):
                    for j in range(9):
                        nin = (3)*(i // 3) + j // 3
                        vals = list(bmap[(i, j)])
                        if len(vals) == 1:
                            continue
                        sbdictn = cnts['n{}'.format(nin)]
                        sbdictc = cnts['c{}'.format(j)]
                        sbdictr = cnts['r{}'.format(i)]
                        x = 0
                        stay = True
                        while x < len(vals) and stay is True:
                            v = vals[x]
                            if sbdictn[v] == 1:
                                print("({}, {})".format(i, j))
                                cnt += 1
                                board[i][j] = v
                                rows[i].add(v)
                                cols[j].add(v)
                                nins[nin].add(v)
                                stay = False
                            elif sbdictc[v] == 1:
                                print("({}, {})".format(i, j))
                                cnt += 1
                                board[i][j] = v
                                rows[i].add(v)
                                cols[j].add(v)
                                nins[nin].add(v)
                                stay = False
                            elif sbdictr[v] == 1:
                                print("({}, {})".format(i, j))
                                cnt += 1
                                board[i][j] = v
                                rows[i].add(v)
                                cols[j].add(v)
                                nins[nin].add(v)
                                stay = False
                            x += 1
                valid, rows, cols, nins = self.checkValidSudoku(board)
                if valid is False:
                    return board
                bmap = {}
                cnt1 = 0
                for i in range(9):
                    for j in range(9):
                        if board[i][j] != ".":
                            cnt1 += 1
                            bmap[(i,j)] = {board[i][j]}
                        else:
                            nin = (3)*(i // 3) + j // 3
                            bmap[(i,j)] = {str(k) for k in range(1,10) if (str(k) not in rows[i] and str(k) not in cols[j] and str(k) not in nins[nin])}
                solved, board, rows, cols, nins, bmap = self.applyRules(board, rows, cols, nins, bmap)
            bvals = [(len(v), k, v) for k, v in bmap.items() if len(v) > 1]
            bvals.sort()
            ogbd = [[i for i in row] for row in board]
            ogrows = {k: v for k, v in rows.items()}
            ogcols = {k: v for k, v in cols.items()}
            ognins = {k: v for k, v in nins.items()}
            ogbmap = {k: v for k, v in bmap.items()}
            for i in range(len(bvals)):
                bvtpl = bvals[i]
                for j in bvtpl[2]:
                    board[bvtpl[1][0]][bvtpl[1][1]] = j
                    solved, board, rows, cols, nins, bmap = self.applyRules(board, rows, cols, nins, bmap)
                    valid, rows, cols, nins = self.checkValidSudoku(board)
                    if solved and valid:
                        print("here")
                        return board
                    elif self.checkValidSudoku(board) is False:
                        board = ogbd
                        rows = ogrows
                        cols = ogcols
                        nins = ognins
                        bmap = ogbmap
                    else:
                        board = self.sudokuSolver(board)
                        valid, rows, cols, nins =  self.checkValidSudoku(board)
                        if valid is False:
                            board = ogbd
                            rows = ogrows
                            cols = ogcols
                            nins = ognins
                            bmap = ogbmap
                        elif self.applyRules(board, rows, cols, nins, bmap)[0]:
                            print(board)
                            return board
        return board
    
    def getCounts(self, bmap: dict) -> dict:
        ret_dict = {}
        for i in range(9):
            for j in range(9):
                nin = (3)*(i // 3) + j // 3
                vals = bmap[(i, j)]
                sbdict = ret_dict.get('n{}'.format(nin))
                ret_dict['n{}'.format(nin)] = self.helper(sbdict, vals)

                sbdict = ret_dict.get('r{}'.format(i))
                ret_dict['r{}'.format(i)] = self.helper(sbdict, vals)

                sbdict = ret_dict.get('c{}'.format(j))
                ret_dict['c{}'.format(j)] = self.helper(sbdict, vals)
        return ret_dict

    def helper(self, sbdict: dict, vals: set) -> dict:
        if sbdict:
            subdict = sbdict.copy()
            for v2 in vals:
                nov = True
                for k, v in subdict.items():
                    if k == v2:
                        sbdict[k] = v + 1
                        nov = False
                if nov:
                    sbdict[v2] = 1
        else:
            sbdict = {k: 1 for k in vals}
        return sbdict

    def applyRules(self, board: List[List[str]], rows: dict, cols: dict, nins: dict, bmap: dict) -> tuple:
        cnt = 1
        while cnt > 0:
            cnt = 0
            for k, v in bmap.items():
                if len(v) == 1 and board[k[0]][k[1]] == ".":
                    cnt += 1
                    val = v.pop()
                    board[k[0]][k[1]] = val
                    nin = (3)*(k[0] // 3) + k[1] // 3
                    rows[k[0]].add(val)
                    cols[k[1]].add(val)
                    nins[nin].add(val)
            unsolved = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        bmap[(i,j)] = {board[i][j]}
                    else:
                        unsolved = True
                        nin = (3)*(i // 3) + j // 3
                        bmap[(i,j)] = {str(k) for k in range(1,10) if (str(k) not in rows[i] and str(k) not in cols[j] and str(k) not in nins[nin])}
                    if cnt == 0 and unsolved:
                        return (False, board, rows, cols, nins, bmap)
        return (True, board, rows, cols, nins, bmap)

    def checkValidSudoku(self, board: List[List[str]]) -> tuple:
        rows = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        cols = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        ninths = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        i = 0
        for row in board:
            rst = set()
            for j in range(9):
                nin = (3)*(i // 3) + j // 3
                if row[j] == ".":
                    continue
                elif row[j] in rows[i]:
                    return False, None, None, None
                elif row[j] in cols[j]:
                    return False, None, None, None
                elif row[j] in ninths[nin]:
                    return False, None, None, None
                else:
                    rows[i].add(row[j])
                    cols[j].add(row[j])
                    ninths[nin].add(row[j])
            i += 1
        return True, rows, cols, ninths