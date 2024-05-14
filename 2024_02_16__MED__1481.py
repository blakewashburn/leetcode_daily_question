"""
Title: 
1481. Least Number of Unique Integers after K Removals

Description: 
  Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example:
  Input: arr = [5,5,4], k = 1
  Output: 1
  Explanation: Remove the single 4, only 5 is left.

  Input: arr = [4,3,1,1,3,3,2], k = 3
  Output: 2
  Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Constraints:
  1 <= arr.length <= 10^5
  1 <= arr[i] <= 10^9
  0 <= k <= arr.length

"""

from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        # count frequency of each value in arr, grab only the frequencies
        frequencies = list(Counter(arr).values())
        frequencies.sort()

        # track how many values have been removed from arr
        frequency_counter = 0

        # loop until we have removed k instances of a value in arr 
        while k > 0:
            
            # if the frequency of a value in arr <= k
            if frequencies[frequency_counter] <= k:

                # remove the value and subtract the value's freqeuncy from k
                k -= frequencies[frequency_counter]
                frequency_counter += 1

            
            # if the frequency of a value in arr > k, then the value persists and results
            # in a count of the length of the remaining frequencies
            else:
                break

        return len(frequencies) - frequency_counter

        


if __name__ == "__main__":
  sol = Solution()
    
  arr, k = [5,5,4], 1      # -> 1
  arr, k = [4,3,1,1,3,3,2], 3     # -> 2

  print(sol.findLeastNumOfUniqueInts(arr=arr, k=k))
