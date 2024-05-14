"""
Title:
2962. Count Subarrays Where Max Element Appears at Least K Times

Description:
	You are given an integer array nums and a positive integer k.
	Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
	A subarray is a contiguous sequence of elements within an array.

Examples:
	Input: nums = [1,3,2,3,3], k = 2
	Output: 6
	Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

	Input: nums = [1,4,2,1], k = 3
	Output: 0
	Explanation: No subarray contains the element 4 at least 3 times.


Constrains:
	1 <= nums.length <= 10^5
	1 <= nums[i] <= 10^6
	1 <= k <= 10^5
"""


class Solution(object):
    def countSubarrays(self, nums: list[int], k: int) -> int:

        # Sliding Window Approach

        max_num = max(nums)
        start, ans, max_num_count = 0, 0, 0

        # loop over all values in nums 
        for end in range(len(nums)):

            # check for max_num
            if nums[end] == max_num:
                max_num_count += 1

            # shrink window until we are back at fewer than k max_nums
            while max_num_count == k:

                # remove a max_num
                if nums[start] == max_num:
                    max_num_count -= 1
                
                # shrink window
                start += 1
            
            # accumulate the count of subarrays that meet the condition
            ans += start
        
        return ans
        



if __name__ == "__main__":
	sol = Solution()


	nums, k = [1,3,2,3,3], 2			# -> 6
	# nums, k = [1,4,2,1], 3				# -> 0


	print(sol.countSubarrays(nums=nums, k=k))