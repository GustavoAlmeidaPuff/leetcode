class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_alphanum = "".join(char for char in s if char.isalnum())
        
        s_inverted = s_alphanum[::-1]

        return s_inverted.lower() == s_alphanum.lower()