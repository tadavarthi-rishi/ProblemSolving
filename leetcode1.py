# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# Companies
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


class Solution:
    def reverseVowels(s: str) -> str:
        vowels = []
        output = []
        for i in s:
            if i in 'aeiouAEIOU':
                vowels.append(i)
        temp = len(vowels)-1
        for i in s:
            if i in 'aeiouAEIOU':
                output.append(vowels[temp])
                temp-=1
            else:
                output.append(i)
        return ''.join(output)
    

    print(reverseVowels("IceCreAm")) # "AceCreIm"