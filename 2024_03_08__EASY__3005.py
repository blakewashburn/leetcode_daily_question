"""
Title: 
3005. Count Elements With Maximum Frequency

Description: 
  You are given an array nums consisting of positive integers.
  Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
  The frequency of an element is the number of occurrences of that element in the array.

Example:
  Input: nums = [1,2,2,3,1,4]
  Output: 4
  Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
  So the number of elements in the array with maximum frequency is 4.

  Input: nums = [1,2,3,4,5]
  Output: 5
  Explanation: All elements of the array have a frequency of 1 which is the maximum.
  So the number of elements in the array with maximum frequency is 5.

Constraints:
  1 <= nums.length <= 100
  1 <= nums[i] <= 100

"""

from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:

        freq = defaultdict(int)
        max_freq = 0
        ans = 0

        # Calcualte the frequency of each num in nums and track max_freq
        for num in nums:
            freq[num] += 1
            max_freq = max(max_freq, freq[num])
        
        # search through dict for how many num in nums have max_freq
        for key in freq.keys():
            if freq[key] == max_freq:
                ans += freq[key]

        return ans
        

if __name__ == "__main__":
  sol = Solution()
    

  nums = [1,2,2,3,1,4]     # -> 4
  # nums = [1,2,3,4,5]     # -> 5


  print(sol.maxFrequencyElements(nums=nums))
