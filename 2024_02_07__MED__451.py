"""
Title: 
451. Sort Characters By Frequency

Description: 
    Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example:
    Input: s = "tree"
    Output: "eert"
    Explanation: 'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

    Input: s = "cccaaa"
    Output: "aaaccc"
    Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
    Note that "cacaca" is incorrect, as the same characters must be together.

    Input: s = "Aabb"
    Output: "bbAa"
    Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.

Constraints:
    1 <= s.length <= 5 * 10^5
    s consists of uppercase and lowercase English letters and digits.

"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        ans = ''
        sorted_counter = Counter(s).most_common()
        for letter, freq in sorted_counter:
            ans += ''.join(letter for _ in range(freq))
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    s = "tree"           # -> "eert"
    s = "cccaaa"         # -> "aaaccc"
    s = "Aabb"           # -> "bbAa"

    print(sol.frequencySort(s=s))
