"""
Title: 
1239. Maximum Length of a Concatenated String with Unique Characters

Description: 
    You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
    Return the maximum possible length of s.
    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example:
    Input: arr = ["un","iq","ue"]
    Output: 4
    Explanation: All the valid concatenations are:
    - ""
    - "un"
    - "iq"
    - "ue"
    - "uniq" ("un" + "iq")
    - "ique" ("iq" + "ue")
    Maximum length is 4.

    Input: arr = ["cha","r","act","ers"]
    Output: 6
    Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

    Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
    Output: 26
    Explanation: The only string in arr has all 26 characters.

Constraints:
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lowercase English letters

"""

class Solution:

    # DFS method
    def maxLength(self, arr: list[str]) -> int:
        self.arr = arr
        self.result = 0
        self.dfs(path="", idx=0)
        return self.result

    def dfs(self, path, idx):

        # Check if the current path has unique characters
        if self.isUniqueChars(path):

            # If the path is unique, update the result with the maximum length
            self.result = max(self.result, len(path))
            
        else:
            # If the path is not unique, return
            return

        # If the current index is equal to the array size, return
        if idx == len(self.arr):
            return

        # otherwise, Iterate through the array starting from the current index and make recursive calls
        for i in range(idx, len(self.arr)):
            self.dfs(path=(path + self.arr[i]), idx=(i + 1))

    # check if 
    def isUniqueChars(self, s):
        if len(set(s)) == len(s):
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    
    arr = ["un","iq","ue"]          # -> 4
    # arr = ["cha","r","act","ers"]       # -> 6
    # arr = ["abcdefghijklmnopqrstuvwxyz"]        # -> 26

    print(sol.maxLength(arr=arr))
