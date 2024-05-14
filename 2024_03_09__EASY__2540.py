"""
Title:
2540. Minimum Common Value

Description:
	Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
	Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Examples:
	Input: nums1 = [1,2,3], nums2 = [2,4]
	Output: 2
	Explanation: The smallest element common to both arrays is 2, so we return 2.

	Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
	Output: 2
	Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.


Constrains:
	1 <= nums1.length, nums2.length <= 10^5
	1 <= nums1[i], nums2[j] <= 10^9
"""


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:

        # two pointers method
        counter_1, counter_2 = 0, 0
        nums1_len, nums2_len = len(nums1), len(nums2)

        # loop until we have checked all values in shortest array
        while counter_1 < nums1_len and counter_2 < nums2_len:

            #  check for a match
            if nums1[counter_1] == nums2[counter_2]:
                return nums1[counter_1]

            # increment the values of the counter who resulted in a smaller number
            if nums1[counter_1] > nums2[counter_2]:
                counter_2 += 1
            else:
                counter_1 += 1
        
        return -1                   



if __name__ == "__main__":
	sol = Solution()

	nums1, nums2 = [1,2,3], [2,4]			# -> 2
	# nums1, nums2 = [1,2,3,6], [2,3,4,5]			# -> 2

	print(sol.getCommon(nums1=nums1, nums2=nums2))