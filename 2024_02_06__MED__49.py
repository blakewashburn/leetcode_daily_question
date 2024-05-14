"""
Title: 
49. Group Anagrams

Description: 
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input: strs = [""]
    Output: [[""]]

    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # track the anagrams
        string_dict = {}

        # loop over and sort the input strings
        for string in strs:
            sorted_string = str(sorted(string)) 

            # use sorted input string as key to anagram dictionary
            # if we have seen this anagram, add to list, otherwise, create new list
            if sorted_string in string_dict.keys():
                string_dict[sorted_string].append(string)
            else:
                string_dict[sorted_string] = [string]

        return [string_dict[key] for key in string_dict.keys()]



if __name__ == "__main__":
    sol = Solution()
    
    strs = ["eat","tea","tan","ate","nat","bat"]        # -> [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs = [""]         # -> [[""]]
    strs = ["a"]        # -> [["a"]]

    print(sol.groupAnagrams(strs=strs))
