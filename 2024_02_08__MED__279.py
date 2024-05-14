"""
Title: 
279. Perfect Squares

Description: 
    Given an integer n, return the least number of perfect square numbers that sum to n.
    A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.

    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.

Constraints:
    1 <= n <= 10^4

"""


class Solution:
    def numSquares(self, n: int) -> int:

        # dynamic programming

        # initialize to max integers expect first value
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # loop over all integers between 1 and n
        for current_n in range(1, n + 1):
            min_val = float('inf')
            perfect_square_base = 1

            # loop over all perfect squares less than the current n
            while perfect_square_base ** 2 <= current_n:
                min_val = min(min_val, dp[current_n - perfect_square_base ** 2] + 1)
                perfect_square_base += 1

            # once we have checked all of the perfect squares less than the current_n, 
            # we have calculated the fewest number of perfect squares required to get to current_n
            dp[current_n] = min_val

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
