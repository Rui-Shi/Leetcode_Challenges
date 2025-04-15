# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        
        while start < end:
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            while end < end and vowels.find(word[end]) == -1:
                end -= 1
            
            word[start], word[end] = word[end], word[start]
            
            start += 1
            end -= 1
            
        return ''.join(word)
            
            
                
            
        