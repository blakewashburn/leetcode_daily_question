"""
Title: 
977. Squares of a Sorted Array

Description: 
	Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example:
	Input: nums = [-4,-1,0,3,10]
	Output: [0,1,9,16,100]
	Explanation: After squaring, the array becomes [16,1,0,9,100].
	After sorting, it becomes [0,1,9,16,100].

	Input: nums = [-7,-3,2,3,11]
	Output: [4,9,9,49,121]

Constraints:
	1 <= nums.length <= 10^4
	-10^4 <= nums[i] <= 10^4
	nums is sorted in non-decreasing order.

"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([i ** 2 for i in nums])
        


if __name__ == "__main__":
     
	sol = Solution()
	nums = [-4,-1,0,3,10]			# -> [0,1,9,16,100]
	# nums = [-7,-3,2,3,11]				# -> Output: [4,9,9,49,121]


	print(sol.sortedSquares(nums=nums))
