"""
Title:
1219. Path with Maximum Gold

Description:
	In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

	Return the maximum amount of gold you can collect under the conditions:

	- Every time you are located in a cell you will collect all the gold in that cell.
	- From your position, you can walk one step to the left, right, up, or down.
	- You can't visit the same cell more than once.
	- Never visit a cell with 0 gold.
	- You can start and stop collecting gold from any position in the grid that has some gold.

Examples:
	Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
	Output: 24
	Explanation:
	[[0,6,0],
	 [5,8,7],
	 [0,9,0]]
	Path to get the maximum gold, 9 -> 8 -> 7.

	Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
	Output: 28
	Explanation:
	[[1,0,7],
	 [2,0,6],
	 [3,4,5],
	 [0,3,0],
	 [9,0,20]]
	Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constrains:
	m == grid.length
	n == grid[i].length
	1 <= m, n <= 15
	0 <= grid[i][j] <= 100
	There are at most 25 cells containing gold.

"""

from typing import List

class Solution(object):
	def __init__(self):
		self.rows = None
		self.cols = None
		self.grid = None
		self.visited = None

	def getMaximumGold(self, grid: List[List[int]]) -> int:

		# Backtracking with Memoization
		# Recursively explore each possible move in the grid
		# Save the result for each exploration in a cache based on the position and the path taken so far
		# before making a recursive call, check if the result has already been computer
		# if yes, use the cached result to avoid redundant calculations.

		self.rows, self.cols = len(grid), len(grid[0])
		self.grid = grid
		self.visited = [[False] * self.cols for _ in range(self.rows)]
		max_gold = 0

		def backtrack(x, y):
			if x < 0 or x >= self.rows or y < 0 or y >= self.cols or self.grid[x][y] == 0 or self.visited[x][y]:
				return 0

			# Mark this cell as visited
			self.visited[x][y] = True
			current_gold = self.grid[x][y]

			# Explore all four directions
			gold_up = backtrack(x - 1, y)
			gold_down = backtrack(x + 1, y)
			gold_left = backtrack(x, y - 1)
			gold_right = backtrack(x, y + 1)

			# Calculate the maximum gold from this path
			max_gold_from_here = current_gold + max(gold_up, gold_down, gold_left, gold_right)

			# Unmark this cell as visited for other recursive calls
			self.visited[x][y] = False

			return max_gold_from_here

		# Try to start from every cell that has gold
		for i in range(self.rows):
			for j in range(self.cols):
				if self.grid[i][j] > 0:
					max_gold = max(max_gold, backtrack(i, j))

		return max_gold


if __name__ == "__main__":
	sol = Solution()

	grid = [[0,6,0],[5,8,7],[0,9,0]]			# -> 24
	grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]			# -> 28

	print(sol.getMaximumGold(grid=grid))