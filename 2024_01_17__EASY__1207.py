"""
Title: 
1207. Unique Number of Occurrences

Description: 
    Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example:
    Input: arr = [1,2,2,1,1,3]
    Output: true
    Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

    Input: arr = [1,2]
    Output: false

    Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
    Output: true


Constraints:
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000

"""

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        freq = Counter(arr)

        known_freqs = set([])
        for key in freq:
            if freq[key] in known_freqs:
                return False
            known_freqs.add(freq[key])
        
        return True
        

if __name__ == "__main__":
    sol = Solution()
    
    arr = [1,2,2,1,1,3]          # -> true
    arr = [1,2]          # -> false
    arr = [-3,0,1,-3,1,1,1,-3,10,0]          # -> true

    print(sol.uniqueOccurrences(arr=arr))
