class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) <= 1:
            return s
        str_len = len(s)
        longest_pal_substr = ""
        dp = [[False] * str_len for _ in range(str_len)]
        max_len = 0
        for substr_len in range(str_len):
            for start_idx in range(str_len - substr_len):
                end_idx = start_idx + substr_len
                if (s[start_idx] == s[end_idx] and (end_idx - start_idx <= 2 or dp[start_idx + 1][end_idx - 1])):
                    dp[start_idx][end_idx] = True
                    if (end_idx - start_idx + 1 > max_len):
                        max_len = end_idx - start_idx + 1
                        longest_pal_substr = s[start_idx:end_idx + 1]
        return longest_pal_substr
