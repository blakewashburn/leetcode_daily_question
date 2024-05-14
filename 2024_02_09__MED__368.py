"""
Title: 
368. Largest Divisible Subset

Description: 
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example:
    Input: nums = [1,2,3]
    Output: [1,2]
    Explanation: [1,3] is also accepted.

    Input: nums = [1,2,4,8]
    Output: [1,2,4,8]

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 10^9

"""



class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:

        #  sort in ascending order to ensure only consider elements that come before the current element
        nums.sort()

        # dp[i] represents the length of the largest divisible subset ending at index i
        n = len(nums)
        dp = [1] * n
        max_size, max_index = 1, 0

        # For each element nums[i]
        for i in range(1, n):
        
            # iterate through all elements before it (nums[j], where j < i) 
            for j in range(i):

                # check if nums[i] is divisible by nums[j]
                if nums[i] % nums[j] == 0:

                    # If divisible and adding nums[i] to subset results in larger subset, update the dp[i] value
                    dp[i] = max(dp[i], dp[j] + 1)

                    # keep track of the maximum subset length and index
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        result = []
        num = nums[max_index]

        # iterate through the dp array from the end to reconstruct the largest divisible subset
        # start from the element that corresponds to the maximum subset length and backtrack by adding 
        # elements to the result vector (v) while ensuring that each element divides the next element in the subset.
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append(nums[i])
                num = nums[i]
                max_size -= 1

        return result



if __name__ == "__main__":
    sol = Solution()
    
    nums = [1,2,3]          # -> [1,2]
    nums = [1,2,4,8]        # -> [1,2,4,8]

    print(sol.largestDivisibleSubset(nums=nums))
