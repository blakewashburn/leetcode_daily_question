"""
Title:
2441. Largest Positive Integer That Exists With Its Negative

Description:
	Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
	Return the positive integer k. If there is no such integer, return -1.

Examples:
	Input: nums = [-1,2,-3,3]
	Output: 3
	Explanation: 3 is the only valid k we can find in the array.

	Input: nums = [-1,10,6,7,-7,1]
	Output: 7
	Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

	Input: nums = [-10,8,6,7,-2,-3]
	Output: -1
	Explanation: There is no a single valid k, we return -1.


Constrains:
	1 <= nums.length <= 1000
	-1000 <= nums[i] <= 1000
	nums[i] != 0
"""


class Solution(object):
    def findMaxK(self, nums: list[int]) -> int:

        # sort
        nums.sort()

        while nums:

            # If front and back of list are the same, we found our largest k
            # If not, remove the largest value, from either the front or back 

            if nums[0] == (-1) * nums[-1]:
                return nums[-1]
            elif abs(nums[0]) > abs(nums[-1]):
                nums.pop(0)
            else:
                nums.pop(-1)
        
        return -1



if __name__ == "__main__":
	sol = Solution()

        
	nums = [-1,2,-3,3]			# -> 3
	nums = [-1,10,6,7,-7,1]			# -> 7
	nums = [-10,8,6,7,-2,-3]		# -> -1


	print(sol.findMaxK(nums=nums))