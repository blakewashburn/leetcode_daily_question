"""
Title: 
169. Majority Element

Description: 
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example:
    Input: nums = [3,2,3]
    Output: 3

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

"""

from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return Counter(nums).most_common()[0][0]


if __name__ == "__main__":
    sol = Solution()
    
    nums = [3,2,3]      # -> 3
    nums = [2,2,1,1,1,2,2]      # -> 2


    print(sol.majorityElement(nums=nums))
