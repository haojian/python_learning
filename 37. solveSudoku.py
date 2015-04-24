class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
	def solveSudoku(self, board):
		self.dfs(board)
		
	def dfs(self, board):
		for row in range(9):
			for col in range(9):
				if board[row][col] == '.':
					for k in "123456789":
					    board[row][col] = k
					    if self.isValid(board, row, col) and self.dfs(board):
							return True
				        board[row][col] = '.'
					return False
		return True

	def isValid(self, board, tr, tc):
		target = board[tr][tc]
		board[tr][tc] = 'D'
		#check row 
		for row in range(9):
			if board[row][tc] == target:
				return False
		#check col
		for col in range(9):
			if board[tr][col] == target:
				return False
		#check cube
		for row in range(3):
			for col in range(3):
				if board[(tr/3)*3+row][(tc/3)*3+col] == target:
					return False
		board[tr][tc] = target
		return True