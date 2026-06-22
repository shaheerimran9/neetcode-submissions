class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string s -> return True if palindrome or False
        # CASE INSENSITIVE & NO NON-ALPHANUMERIC CHARACTERS!

        l, r = 0, len(s) - 1
        while l < r:
            # Check if characters are alphanumeric first
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            # Compare the characters ignoring case
            if s[l].lower() != s[r].lower():
                return False
            # Same characters -> Increment pointers    
            else:
                l += 1
                r -= 1
        return True
        