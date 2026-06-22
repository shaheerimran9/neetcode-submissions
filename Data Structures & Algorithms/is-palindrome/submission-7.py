class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Input -> string s
        # Output -> Return true if s is palindrome || False if not palindrome
        # Palindrome -> string that is same reversed and case insensitive
            # Ignore non-alphanumeric characters

        # Use two pointers start and end
        # While the pointers haven't met
        # If either character is not alphanumeric skip it
        # If its alphanumeric compare the characters
            # If not the same character return False
            # Else move start and end pointers
        # Return True at the end

        l, r = 0, len(s)-1
        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True