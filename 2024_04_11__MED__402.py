"""
Title:
402. Remove K Digits

Description:
	Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Examples:
	Input: num = "1432219", k = 3
	Output: "1219"
	Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

	Input: num = "10200", k = 1
	Output: "200"
	Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

	Input: num = "10", k = 2
	Output: "0"
	Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Constrains:
	1 <= k <= num.length <= 10^5
	num consists of only digits.
	num does not have any leading zeros except for the zero itself.
"""


class Solution(object):
    def removeKdigits(self, num: str, k: int) -> str:

        # Stack and Backtracking method
        # we want to remove num[i] is num[i] > num[i+1]

        stack = []

        # loop over all digits
        for i in range(len(num)): 
            
            # backtrack as needed if previous value is higher than current value
            while stack and stack[-1] > num[i] and k:
                stack.pop()
                k-= 1
            
            # add current digit to stack
            stack.append(num[i])
        
        # Now we have an sorted list and must remove the last k values from the back
        while k:
            stack.pop()
            k -= 1

        # remove leading zeros and return the remaining digits of num
        ans = ''.join(stack).lstrip('0')
        return ans if ans != "" else "0"


if __name__ == "__main__":
	sol = Solution()

	num, k = "1432219", 3			# -> "1219"
	# num, k = "10200", 1				# -> "200"
	# num, k = "10", 2			# -> "0"


	print(sol.removeKdigits(num=num, k=k))