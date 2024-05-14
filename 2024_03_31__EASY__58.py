"""
Title:
58. Length of Last Word

Description:
	Given a string s consisting of words and spaces, return the length of the last word in the string.
	A word is a maximal substring consisting of non-space characters only.

Examples:
	Input: s = "Hello World"
	Output: 5
	Explanation: The last word is "World" with length 5.

	Input: s = "   fly me   to   the moon  "
	Output: 4
	Explanation: The last word is "moon" with length 4.

	Input: s = "luffy is still joyboy"
	Output: 6
	Explanation: The last word is "joyboy" with length 6.


Constrains:
	1 <= s.length <= 10^4
	s consists of only English letters and spaces ' '.
	There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        ans, last_char = "", ""

        # loop over 
        for char in s:

            # if we get a space, set last character as space
            if char == " ":
                last_char = " " 

            # if we get a non-space and our last character was a space, start ans over
            elif last_char == " ":
                ans = char
                last_char = char

            # add to the current word
            else:
                ans += char
                last_char = char
        
        return len(ans)




if __name__ == "__main__":
	sol = Solution()





	print(sol)