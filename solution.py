class Solution:

    def __init__(self):
        pass

    # 5. Longest Palindromic Substring
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

    # 925. Long Pressed Name
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name_len = len(name)
        typed_len = len(typed)
        name_index = 0
        typed_index = 0

        while name_index < name_len and typed_index < typed_len:
            if name[name_index] == typed[typed_index]:
                name_index += 1
                typed_index += 1
            else:
                if typed_index == 0:
                    return False
                if typed[typed_index] == typed[typed_index - 1]:
                    typed_index += 1
                else:
                    return False

        if name_index < name_len:
            return False

        if typed_index < typed_len:
            while typed_index < typed_len:
                if typed[typed_index] != name[name_index - 1]:
                    return False
                typed_index += 1
            return True
        else:
            return True

    # 1658. Minimum Operations to Reduce X to Zero
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        n = len(nums)
        if total < x:
            return -1
        if total == x:
            return n

        target = total - x
        current_sum = 0
        max_len = -1
        left = 0

        for right in range(n):
            current_sum += nums[right]

            # If current_sum exceeds target, move left pointer to reduce the window size
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Check if current window sum equals target and update max length
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1


if __name__ == "__main__":
    s = Solution()

    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ac"))
