"""
Title:
42. Trapping Rain Water

Description:
	Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Examples:
	Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
	Output: 6
	Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

	Input: height = [4,2,0,3,2,5]
	Output: 9


Constrains:
	n == height.length
	1 <= n <= 2 * 10^4
	0 <= height[i] <= 10^5
"""


class Solution(object):
    def trap(self, height: list[int]) -> int:

        # Use two arrays to determine the walls that we will use to calcuate trapped water

        n = len(height)
        left, right = [0] * n, [0] * n
        
        # Loop over left array, set highest height as either current height or 
        # highest we have seen in the past
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        
        # Loop over right array backwards, set highest height as either current height or 
        # highest we have seen in the past
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        
        # trapped water = lower of the highest values between left and right - the current height
        trappedWater = 0
        for i in range(n):
            trappedWater += min(left[i], right[i]) - height[i]
        
        return trappedWater  
        

if __name__ == "__main__":
	sol = Solution()

	height = [0,1,0,2,1,0,1,3,2,1,2,1]			# -> 6
	height = [4,2,0,3,2,5]			# -> 9

	print(sol.trap(heigh=height))