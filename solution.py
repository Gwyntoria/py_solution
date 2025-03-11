class Solution:

    def __init__(self):
        pass

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        max_len = 0
        start = 0
        str_len = len(s)

        for i in range(str_len):
            # Check for odd-length palindromes centered at i
            left, right = i, i
            while left >= 0 and right < str_len and s[left] == s[right]:
                left -= 1
                right += 1
            current_length = right - left - 1
            if current_length > max_len:
                max_len = current_length
                start = left + 1

            # Check for even-length palindromes centered between i and i+1
            left, right = i, i + 1
            while left >= 0 and right < str_len and s[left] == s[right]:
                left -= 1
                right += 1
            current_length = right - left - 1
            if current_length > max_len:
                max_len = current_length
                start = left + 1

        return s[start : start + max_len]


if __name__ == "__main__":
    s = Solution()

    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ac"))
