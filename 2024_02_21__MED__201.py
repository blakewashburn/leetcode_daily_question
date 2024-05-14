"""
Title: 
201. Bitwise AND of Numbers Range

Description: 
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example:
  Input: left = 5, right = 7
  Output: 4

  Input: left = 0, right = 0
  Output: 0

  Input: left = 1, right = 2147483647
  Output: 0

Constraints:
  0 <= left <= right <= 2^31 - 1

"""



class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    shift = 0
    while left < right:
      left >>= 1
      right >>= 1
      shift += 1
    return left << shift
        


if __name__ == "__main__":
  sol = Solution()
  


  print(sol)
