"""
Title:
2485. Find the Pivot Integer

Description:
	Given a positive integer n, find the pivot integer x such that:
		The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
	Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Examples:
	Input: n = 8
	Output: 6
	Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

	Input: n = 1
	Output: 1
	Explanation: 1 is the pivot integer since: 1 = 1.

	Input: n = 4
	Output: -1
	Explanation: It can be proved that no such integer exist.


Constrains:
	1 <= n <= 1000
"""


class Solution:
    def pivotInteger(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return -1

        # Binary Search
        low, high = 1, n
        prev_guess = -1

        while low < high:
            guess = (low + high) // 2 

            # Check for constant loop
            if prev_guess == guess: 
                return -1
            else:
                prev_guess = guess
                
            
            # Calculate the new sums on both sides
            lower_total = sum([i for i in range(1, guess + 1)]) 
            upper_total = sum([i for i in range(guess, n + 1)]) 

            # change out pointer for binary search if needed
            if lower_total == upper_total:
                return guess
            if lower_total > upper_total:
                high = guess
            else:
                low = guess    
        
        return -1 
        



if __name__ == "__main__":
	sol = Solution()


	n = 8			# -> 6
	n = 1			# -> 1
	n = 4			# -> -1


	print(sol.pivotInteger(n=n))