class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        start, max_length = 0, 1
        
        for i in range(len(s)):
            odd = self.expandAroundCenter(s, i, i)
            even = self.expandAroundCenter(s, i, i + 1)
            current_length = max(odd, even)
            
            if current_length > max_length:
                max_length = current_length
                start = i - (current_length - 1) // 2
        
        return s[start:start + max_length]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

