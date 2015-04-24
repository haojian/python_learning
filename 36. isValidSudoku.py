class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
		#check row 
		for row in range(9):
			counter = [0]*9
			for col in range(9):
				if board[row][col] == '.':
					continue
				if counter[ int(board[row][col])-1 ] == 0:
					counter[ int(board[row][col])-1 ] = 1
				else:
					return False
		#check column
		for col in range(9):
			counter = [0]*9
			for row in range(9):
				if board[row][col] == '.':
					continue
				if counter[ int(board[row][col])-1 ] == 0:
					counter[ int(board[row][col])-1 ] = 1
				else:
					return False
		#check cube
		for row in range(3):
			for col in range(3):
				counter = [0]*9
				for subrow in range(3):
					for subcol in range(3):
						final_row = row*3 + subrow
						final_col = col*3 + subcol
						if board[final_row][final_col] == '.':
							continue
						if counter[ int(board[final_row][final_col])-1 ] == 0:
							counter[ int(board[final_row][final_col])-1 ] = 1
						else:
							return False
		
		return True
		
		
if __name__ == "__main__":
	sol = Solution()
	print sol.isValidSudoku([".........",".........",".9......1","8........",".99357...",".......4.","...8.....",".1....4.9","...5.4..."])
	print sol.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
	