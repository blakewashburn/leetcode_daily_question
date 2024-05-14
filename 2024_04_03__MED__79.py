"""
Title:
79. Word Search

Description:
	Given an m x n grid of characters board and a string word, return true if word exists in the grid.
	The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Examples:
	Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
	Output: true

	Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
	Output: true

Constrains:
	m == board.length
	n = board[i].length
	1 <= m, n <= 6
	1 <= word.length <= 15
	board and word consists of only lowercase and uppercase English letters.
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        # determine if we can use a letter from the board
        def valid_letter(cur_loc:tuple, next_letter:str, used:set):
            
            # check if valid location on board
            if 0 <= cur_loc[0] < rows and 0 <= cur_loc[1] < cols:

                # check if letter is correct:
                if next_letter == board[cur_loc[0]][cur_loc[1]]:

                    # check that location has not been used before
                    if cur_loc not in used:
                        return True
            return False

        # facilitate looking for the desired word using recursion
        def find_word(remaining_letters:str, cur_loc:tuple, used:set):

            # Base case
            if remaining_letters == "":
                return True
            
            # determine if we can follow this path
            if valid_letter(cur_loc=cur_loc, next_letter=remaining_letters[0], used=used):
                used.add(cur_loc)

                # check above
                if find_word(cur_loc=(cur_loc[0]-1, cur_loc[1]), remaining_letters=remaining_letters[1:], used=used):
                    return True
                # check below
                if find_word(cur_loc=(cur_loc[0]+1, cur_loc[1]), remaining_letters=remaining_letters[1:], used=used):
                    return True
                # check left
                if find_word(cur_loc=(cur_loc[0], cur_loc[1]-1), remaining_letters=remaining_letters[1:], used=used):
                    return True
                # check right
                if find_word(cur_loc=(cur_loc[0], cur_loc[1]+1), remaining_letters=remaining_letters[1:], used=used):
                    return True
                
                used.remove(cur_loc)
            
            return False


        rows = len(board)
        cols = len(board[0])

        # Loop over every character in board
        for i in range(rows):
            for j in range(cols):
                if find_word(remaining_letters=word, cur_loc=(i, j), used=set()):
                    return True
        return False



if __name__ == "__main__":
	sol = Solution()


	board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"		# -> true
	# board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "SEE" 		# -> true

	print(sol.exist(board=board, word=word))