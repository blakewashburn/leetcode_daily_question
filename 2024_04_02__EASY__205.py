"""
Title:
205. Isomorphic Strings

Description:
	Given two strings s and t, determine if they are isomorphic.
	Two strings s and t are isomorphic if the characters in s can be replaced to get t.
	All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Examples:
	Input: s = "egg", t = "add"
	Output: true

	Input: s = "foo", t = "bar"
	Output: false

	Input: s = "paper", t = "title"
	Output: true


Constrains:
	1 <= s.length <= 5 * 10^4
	t.length == s.length
	s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):

            # if char in s has been seen before
            if s[i] in s_to_t:

                # if char in t has been seen before
                if t[i] in t_to_s:

                    # if they do not equal each other, break
                    if s_to_t[s[i]] != t[i] or t_to_s[t[i]] != s[i]:
                        return False
                
                # if char in t has not been seen before
                else:
                    return False
            
            # if char in s has not been seen before
            else:

                # if char in t has not been seen before
                if t[i] not in t_to_s:

                    # Add both associations
                    s_to_t[s[i]] = t[i]
                    t_to_s[t[i]] = s[i]
                
                # if char in t has been seen before
                else:
                    return False
            
        return True



if __name__ == "__main__":
	sol = Solution()

	s, t = "egg", "add"			# -> true
	# s, t = "foo", "bar"			# -> false
	# s, t = "paper", "title"			# -> true


	print(sol.isIsomorphic(s=s, t=t))