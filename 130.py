class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        h = len(board)
        w = len(board[0])
        read = [[False for n in range(w)] for m in range(h)]
        for i in range(h):
            for j in range(w):
                if read[i][j]:
                    continue
                
                if board[i][j] == "O" and not read[i][j]:
                    print i, j
                    q = [(i, j)]
                    p = 0
                    flag = True
                    read[i][j] = True
                    while p != len(q):
                        m, n = q[p]
                        p += 1
                        
                        if m == 0:
                            flag = False
                        elif board[m-1][n] == "O" and not read[m-1][n]:
                            q.append((m-1, n))
                            read[m-1][n] = True
                        if m == h-1:
                            flag = False
                        elif board[m+1][n] == "O" and not read[m+1][n]:
                            q.append((m+1, n))
                            read[m+1][n] = True
                        if n == 0:
                            flag = False
                        elif board[m][n-1] == "O" and not read[m][n-1]:
                            q.append((m, n-1))
                            read[m][n-1] = True
                        if n == w-1:
                            flag = False
                        elif board[m][n+1] == "O" and not read[m][n+1]:
                            q.append((m, n+1))
                            read[m][n+1] = True
                    
                    if flag:
                        for m, n in q:
                            board[m][n] = "X"
