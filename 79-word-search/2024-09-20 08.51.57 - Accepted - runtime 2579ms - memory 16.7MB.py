class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for c in word:
            ret_val = False
            for row in board:
                st = set(row)
                if c in st:
                    ret_val = True
            if ret_val is False:
                return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                bln = self.recurse(board, word, (i, j), '', set())
                if bln:
                    return True
        return False
    def recurse(self, board: List[List[str]], word: str, pos: tuple, substr: str, visited: set) -> bool:
        if substr == word:
            return True
        elif pos in visited:
            return False
        elif pos[0] < 0 or pos[0] >= len(board) or pos[1] < 0 or pos[1] >= len(board[0]):
            return False
        elif substr == word[:len(substr)]:
            visited_cpy = set([i for i in visited])
            visited_cpy.add(pos)
            substr_cpy = word[:len(substr)]
            substr_cpy += board[pos[0]][pos[1]]
            # down
            if self.recurse(board, word, (pos[0]+1, pos[1]), substr_cpy, visited_cpy):
                return True
            # right
            elif self.recurse(board, word, (pos[0], pos[1]+1), substr_cpy, visited_cpy):
                return True
            # up
            elif self.recurse(board, word, (pos[0]-1, pos[1]), substr_cpy, visited_cpy):
                return True
            # left
            elif self.recurse(board, word, (pos[0], pos[1]-1), substr_cpy, visited_cpy):
                return True
        return False






