"""
Title:
791. Custom Sort String

Description:
	You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
	Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
	Return any permutation of s that satisfies this property.

Examples:
	Input:  order = "cba", s = "abcd" 
	Output:  "cbad" 
	Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
	Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

	Input:  order = "bcafg", s = "abcd" 
	Output:  "bcad" 
	Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
	Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.


Constrains:
	1 <= order.length <= 26
	1 <= s.length <= 200
	order and s consist of lowercase English letters.
	All the characters of order are unique.
"""

from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:

        # create hash maps of each string so that we know what characters are present
        order_dict, s_dict = defaultdict(int), defaultdict(int)
        for char in order:
            order_dict[char] += 1
        for char in s:
            s_dict[char] += 1

        ans = ""

        # loop over order, if character in order is in s, add to ans string
        for char in order:
            if char in s_dict:
                for _ in range(s_dict[char]):
                    ans += char
        
        # loop over s, if character in s not in order, add to ans string 
        for char in s:
            if char not in order_dict:
                ans += char
        return ans
        



if __name__ == "__main__":
	sol = Solution()


	order, s = "cba", "abcd" 			# -> "cbad" 
	# order, s = "bcafg", "abcd" 			# -> "bcad" 


	print(sol.customSortString(order=order, s=s))