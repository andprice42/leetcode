class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        one_list = []
        zero_list = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                liveNs = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if k == i and l == j:
                            continue
                        elif k >= 0 and k < len(board) and l >= 0 and l < len(board[0]) and board[k][l] == 1:
                            liveNs += 1
                if liveNs == 3 and board[i][j] == 0:
                    one_list.append((i, j))
                elif liveNs < 2 and board[i][j] == 1:
                    zero_list.append((i, j))
                elif liveNs > 3 and board[i][j] == 1:
                    zero_list.append((i, j))
        
        for i, j in one_list:
            board[i][j] = 1
        for i, j in zero_list:
            board[i][j] = 0
                
