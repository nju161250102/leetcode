class NumInfo(object):
    def __init__(self, num_list, pos, order):
        self.num_p = 0
        self.num_list = num_list
        self.pos = pos
        self.order = order
        
class Solution(object):
    def row_check(self, board, pos):
        result = range(1, 10)
        for num in board[pos[0]]:
            if num != '.':
                result.remove(int(num))
        return result
    
    def column_check(self, board, pos):
        result = range(1, 10)
        for i in range(0, 9):
            if board[i][pos[1]] != '.':
                result.remove(int(board[i][pos[1]]))
        return result
    
    def box_check(self, board, pos):
        result = range(1, 10)
        x_k = pos[0] / 3
        y_k = pos[1] / 3
        for i in range(x_k * 3, x_k * 3 + 3):
            for j in range(y_k * 3, y_k * 3 + 3):
                if board[i][j] != '.':
                    result.remove(int(board[i][j]))
        return result
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        empty_list = []
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    empty_list.append((i, j))
        
        stack = []
        i = 0
        while i < len(empty_list):
            pos = empty_list[i]
            possible = [j for j in self.row_check(board, pos) if j in self.column_check(board, pos) and j in self.box_check(board, pos)]
            if len(possible) == 0:
                while True:
                    if len(stack) == 0:
                        return
                    info = stack[-1]
                    if info.num_p == len(info.num_list) - 1:
                        board[info.pos[0]][info.pos[1]] = '.'
                        stack.pop()
                    else:
                        info.num_p += 1
                        board[info.pos[0]][info.pos[1]] = str(info.num_list[info.num_p])
                        i = info.order
                        break
            else:
                stack.append(NumInfo(possible, pos, i))
                board[pos[0]][pos[1]] = str(possible[0])
            i += 1