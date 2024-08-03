class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        memo = {'kill_cols': set(), 'kill_diag': {}}
        boards = self.recurse(board, 0, memo)
        return boards
    
    def recurse(self, board: List[str], row: int, memo: dict) -> List[List[str]]:
        ret_bds = []
        if row == len(board):
            ret_bd = [''.join(arr) for arr in board]
            return [ret_bd]
        for col in range(len(board[row])):
            new_col = True
            if memo.get('kill_cols') and col in memo.get('kill_cols'):
                new_col = False
            if self.checkValid(memo, (row, col)):
                if memo.get('kill_cols') and memo.get('kill_diag'):
                    memo['kill_cols'].add(col)
                    memo['kill_diag'] = self.getDiagKRows(len(board), (row, col), memo['kill_diag'])
                else:
                    memo['kill_cols'] = set([col])
                    memo['kill_diag'] = self.getDiagKRows(len(board), (row, col), {})

                board[row][col] = 'Q'
                nboards = self.recurse(board, row + 1, memo)
                [ret_bds.append(bd) for bd in nboards]
                if new_col:
                    memo['kill_cols'].remove(col)
                dct = memo['kill_diag']
                del dct[(row, col)]
                memo['kill_diag'] = dct
                board[row][col] = '.'
        return ret_bds
    
    def getDiagKRows(self, n: int, pos: tuple, kill_diag: dict) -> dict:
        i = pos[0]
        j = pos[1]
        dset = set()
        first_run = True
        while i < n and j < n:
            if first_run:
                while i > 0 and j > 0:
                    i -= 1
                    j -= 1
                first_run = False
            dset.add((i, j))
            i += 1
            j += 1
        
        i = pos[0]
        j = pos[1]
        first_run = True
        while i < n and j >= 0:
            if first_run:
                while i > 0 and j < n:
                    i -= 1
                    j += 1
                first_run = False
            dset.add((i, j))
            i += 1
            j -= 1
        kill_diag[pos] = dset
        return kill_diag

    def checkValid(self, memo: dict, pos: tuple) -> bool:
        kill_cols = memo.get('kill_cols')
        kill_diag = memo.get('kill_diag')
        if kill_cols is None and kill_diag is None:
            return True
        if pos[1] in kill_cols:
            return False
        
        diag_set = set()
        for k, v in kill_diag.items():
            for v2 in v:
                diag_set.add(v2)
        if (pos[0], pos[1]) in diag_set:
            return False
        return True