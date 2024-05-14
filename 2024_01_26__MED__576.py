"""
Title: 
576. Out of Boundary Paths

Description: 
    There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
    Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example:
    Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
    Output: 6

    Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
    Output: 12


Constraints:
    1 <= m, n <= 50
    0 <= maxMove <= 50
    0 <= startRow < m
    0 <= startColumn < n
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        mod = 10**9 + 7

        # 2D vector represent the number of ways to reach each cell
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1    # starting point
        count = 0

        # Iterate over possible moves
        for _ in range(maxMove):
            temp = [[0] * n for _ in range(m)]

            # for each cell in the 2D vector
            for i in range(m):
                for j in range(n):

                    # if cell is on the boundary, increment count by value of cell
                    if i == m - 1:
                        count = (count + dp[i][j]) % mod
                    if j == n - 1:
                        count = (count + dp[i][j]) % mod
                    if i == 0:
                        count = (count + dp[i][j]) % mod
                    if j == 0:
                        count = (count + dp[i][j]) % mod
                    
                    
                    temp[i][j] = (
                        ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) % mod +
                        ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)) % mod
                    ) % mod

            dp = temp

        return count


if __name__ == "__main__":
    sol = Solution()
    
    m, n, maxMove, startRow, startColumn = 2, 2, 2, 0, 0            # -> 6
    m, n, maxMove, startRow, startColumn = 1, 3, 3, 0, 1            # -> 12


    print(sol)
