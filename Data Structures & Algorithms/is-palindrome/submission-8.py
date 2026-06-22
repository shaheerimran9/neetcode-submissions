class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Input -> string s
        #Output -> True if s is a palindrome || False if not a palindrome
        #Note -> Case insensitive and ignore non-alphanumeric characters

        #We can use two pointers at the start and end
        #Compare the two pointers to make sure they are the same character
        #If the character is non-alphanumeric skip over it

        l, r = 0, len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True