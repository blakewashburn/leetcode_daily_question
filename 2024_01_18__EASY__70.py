"""
Title: 
70. Climbing Stairs

Description: 
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
    1 <= n <= 45

"""


class Solution:

    #Top Down Dynamic Programming using Memorization

    def take_step(self, steps_to_reach_the_top, dp):

        # Check if we are one or fewer steps from the top
        if (steps_to_reach_the_top <= 1):
            return 1
    
        # Check if answer for subproblem already exist
        if(dp[steps_to_reach_the_top] != -1):
            return dp[steps_to_reach_the_top]
    
        # Recursively call for subproblems and store their result in dp
        # This is solving the subproblem
        dp[steps_to_reach_the_top] = self.take_step(steps_to_reach_the_top - 1, dp) + self.take_step(steps_to_reach_the_top - 2, dp)

        return dp[steps_to_reach_the_top]


    def climbStairs(self, n: int) -> int:

        # Create dp arr where dp[i] represent number of ways to reach the ith stair from the bottom 
        dp = [-1] * (n + 1)

        return self.take_step(n, dp)




if __name__ == "__main__":
    sol = Solution()
    
    n = 2            # -> 2
    n = 3           # -> 3

    print(sol.climbStairs(n=n))
