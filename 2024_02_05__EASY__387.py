"""
Title: 
387. First Unique Character in a String

Description: 
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example:
    Input: s = "leetcode"
    Output: 0

    Input: s = "loveleetcode"
    Output: 2

    Input: s = "aabb"
    Output: -1

Constraints:
    1 <= s.length <= 10^5
    s consists of only lowercase English letters.

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # track what characters are not unique and the first index of each character
        seen_twice = set()
        index_dict = {}
        for (index, char) in enumerate(s):
            if char in index_dict: 
                seen_twice.add(char)
            else:
                index_dict[char] = index
        
        # find unique characters
        seen_once = set(index_dict.keys()) - seen_twice

        # find the lowest index among unique characters
        possible_ans = [index_dict[key] for key in seen_once]
        if possible_ans:
            return min(possible_ans)
        else:
            return -1



if __name__ == "__main__":
    sol = Solution()
    
    s = "leetcode"       # -> 0
    # s = "loveleetcode"       # -> 2
    # s = "aabb"       # -> -1

    print(sol.firstUniqChar(s=s))
