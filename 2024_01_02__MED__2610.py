"""
Title: 
2610. Convert an Array Into a 2D Array With Conditions

Description: 
    You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
    - The 2D array should contain only the elements of the array nums.
    - Each row in the 2D array contains distinct integers.
    - The number of rows in the 2D array should be minimal.
    Return the resulting array. If there are multiple answers, return any of them.

    Note that the 2D array can have a different number of elements on each row.

Example:
    Input: nums = [1,3,4,1,2,3,1]
    Output: [[1,3,4,2],[1,3],[1]]
    Explanation: We can create a 2D array that contains the following rows:
    - 1,3,4,2
    - 1,3
    - 1
    All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.

    Input: nums = [1,2,3,4]
    Output: [[4,3,2,1]]
    Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= nums.length

"""

from collections import defaultdict

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:

        ans = []
        # create a dictionary, key = number in num, element = how many of key are in nums
        freq_of_nums = defaultdict(int)
        for num in nums:
            freq_of_nums[num] += 1

        # loop over keys in dictionary
        for key in freq_of_nums:
            row_counter = 0

            # loop on key until we use all values of the key
            while freq_of_nums[key] != 0:

                # check if we need a new row
                if row_counter >= len(ans): 
                    ans.append([key])
                    freq_of_nums[key] -= 1
                    row_counter += 1
                else:
                    ans[row_counter].append(key)
                    freq_of_nums[key] -= 1
                    row_counter += 1
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    nums = [1,3,4,1,2,3,1]      # -> [[1,3,4,2],[1,3],[1]]
    # nums = [1,2,3,4]            # -> [[4,3,2,1]]

    print(sol.findMatrix(nums=nums))

    
