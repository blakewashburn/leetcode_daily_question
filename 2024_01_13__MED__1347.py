"""
Title: 
1347. Minimum Number of Steps to Make Two Strings Anagram

Description: 
    You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
    Return the minimum number of steps to make t an anagram of s.
    An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example:
    Input: s = "bab", t = "aba"
    Output: 1
    Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

    Input: s = "leetcode", t = "practice"
    Output: 5
    Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

    Input: s = "anagram", t = "mangaar"
    Output: 0
    Explanation: "anagram" and "mangaar" are anagrams.

Constraints:
    1 <= s.length <= 5 * 104
    s.length == t.length
    s and t consist of lowercase English letters only.

"""

from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_dict, t_dict = defaultdict(int), defaultdict(int)

        # loop over all letters in s and t to calculate frequency
        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1
        
        # subtract the number of letters in t that appear in s from s number frequency
        for t_key in t_dict.keys():
            if t_key in s_dict:
                s_dict[t_key] -= t_dict[t_key]
        
        ans = 0

        # calculate the number of lettes in s that are missing from t after subtraction
        for s_key in s_dict.keys():
            if s_dict[s_key] > 0:
                ans += s_dict[s_key]
        
        return ans

        # SIMPLE METHOD - SAME AS MINE BUT LOW CODE
        # counter_s = Counter(s)
        # counter_t = Counter(t)
        # diff = counter_s - counter_t
        # return sum(diff.values())


if __name__ == "__main__":
    sol = Solution()

    s, t = "bab", "aba"      # -> 1
    # s, t = "leetcode", "practice"       # -> 5
    # s, t = "anagram", "mangaar"         # -> 0

    print(sol.minSteps(s=s, t=t))
