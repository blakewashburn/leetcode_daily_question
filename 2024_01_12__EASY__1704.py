"""
Title: 
1704. Determine if String Halves Are Alike

Description: 
    You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
    Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
    Return true if a and b are alike. Otherwise, return false.

Example:
    Input: s = "book"
    Output: true
    Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

    Input: s = "textbook"
    Output: false
    Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
    Notice that the vowel o is counted twice.

Constraints:
    2 <= s.length <= 1000
    s.length is even.
    s consists of uppercase and lowercase letters.

"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        first_half_vowel_count, second_half_vowel_count = 0, 0
        
        half_length = len(s) // 2
        for i in range(half_length): 
            if s[i] in vowels:
                first_half_vowel_count += 1
            if s[i + half_length] in vowels:
                second_half_vowel_count += 1
        
        return True if first_half_vowel_count == second_half_vowel_count else False



if __name__ == "__main__":
    sol = Solution()
    
    s = "book"      # -> true
    s = "textbook"      # -> false


    print(sol.halvesAreAlike(s=s))
