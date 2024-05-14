"""
Title: 
645. Set Mismatch

Description: 
    You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
    You are given an integer array nums representing the data status of this set after the error.
    Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example:
    Input: nums = [1,2,2,4]
    Output: [2,3]
    Example 2:

    Input: nums = [1,1]
    Output: [1,2]

Constraints:
    2 <= nums.length <= 10^4
    1 <= nums[i] <= 10^4

"""

from collections import defaultdict

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        # find which number is missing
        missing_num = set([i for i in range(1, len(nums))]) - set(nums)
        if missing_num == set():
            missing_num = len(nums)
        else:
            missing_num = missing_num.pop()

        # find the duplicate number
        freq = defaultdict(int)
        for num in nums:
            if freq[num] > 0:
                return [num, missing_num]
            else:
                freq[num] = 1


if __name__ == "__main__":
    sol = Solution()
    
    nums = [1,2,2,4]            # -> [2,3]
    nums = [1,1]                # -> [1,2]

    print(sol.findErrorNums(nums=nums))
