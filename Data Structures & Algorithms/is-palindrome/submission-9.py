class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Check if characters are alphanumeric
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            # Check if both characters are the same
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
