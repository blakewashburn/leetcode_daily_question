"""
Title: 
2108. Find First Palindromic String in the Array

Description: 
    Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
    A string is palindromic if it reads the same forward and backward.

Example:
    Input: words = ["abc","car","ada","racecar","cool"]
    Output: "ada"
    Explanation: The first string that is palindromic is "ada".
    Note that "racecar" is also palindromic, but it is not the first.

    Input: words = ["notapalindrome","racecar"]
    Output: "racecar"
    Explanation: The first and only string that is palindromic is "racecar".

    Input: words = ["def","ghi"]
    Output: ""
    Explanation: There are no palindromic strings, so the empty string is returned.

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists only of lowercase English letters.

"""


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]: return word
        return ""


if __name__ == "__main__":
    sol = Solution()
    
    words = ["abc","car","ada","racecar","cool"]         # -> "ada"
    words = ["notapalindrome","racecar"]         # -> "racecar"
    words = ["def","ghi"]            # -> ""

    print(sol.firstPalindrome(words=words))
