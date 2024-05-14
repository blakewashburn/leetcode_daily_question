"""
Title: 
1750. Minimum Length of String After Deleting Similar Ends

Description: 
	Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:
		Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
		Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
		The prefix and the suffix should not intersect at any index.
		The characters from the prefix and suffix must be the same.
		Delete both the prefix and the suffix.
	Return the minimum length of s after performing the above operation any number of times (possibly zero times).

Example:
	Input: s = "ca"
	Output: 2
	Explanation: You can't remove any characters, so the string stays as is.

	Input: s = "cabaabac"
	Output: 0
	Explanation: An optimal sequence of operations is:
	- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
	- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
	- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
	- Take prefix = "a" and suffix = "a" and remove them, s = "".

	Input: s = "aabccabba"
	Output: 3
	Explanation: An optimal sequence of operations is:
	- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
	- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

Constraints:
	1 <= s.length <= 10^5
	s only consists of characters 'a', 'b', and 'c'.

"""



class Solution:
	def minimumLength(self, s: str) -> int:

		beginning_index, ending_index = 0, len(s) - 1

		# conditions for removing:
		# 1. indexes cannot intersect
		# 2. characters in prefix and suffix must be the same
		while (beginning_index < ending_index) and (s[beginning_index] == s[ending_index]):
			print(f'{s[beginning_index]}, {s[ending_index]}')
			
			# determine which character we are removing
			char_to_remove = s[beginning_index]

			# remove those characters
			beginning_index += 1
			ending_index -= 1

			# remove all additional char_to_remove from left
			while (beginning_index < ending_index + 1) and (s[beginning_index] == char_to_remove):
				beginning_index += 1
			
			# remove all additional char_to_remove from right
			while (beginning_index < ending_index + 1) and (s[ending_index] == char_to_remove):
				ending_index -= 1
		
		# print(s[beginning_index : ending_index + 1])
		return len(s[beginning_index : ending_index + 1])
        


if __name__ == "__main__":
	
	sol = Solution()
	
	s = "ca"		# -> 2
	# s = "cabaabac"		# -> 0
	# s = "aabccabba"		# -> 3
	# s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"		# -> 1
	
	
	print(sol.minimumLength(s=s))
