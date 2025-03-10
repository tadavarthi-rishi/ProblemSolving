class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if haystack == needle:
        #     return 0

        # for i in range(len(haystack)):
        #     for j in range(i+1, len(haystack)+1):
        #         if haystack[i:j]==needle:
        #             return i
        # return -1

        if haystack == needle:
            return 0

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
