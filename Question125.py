class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = ''
        
        for i in s.lower():
            if i.isalnum():
                s_cleaned += i
                
        s = s_cleaned[::-1]
        
        return True if s == s_cleaned else False