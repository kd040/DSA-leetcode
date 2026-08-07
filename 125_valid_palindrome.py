class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

def main():
    solution = Solution()
    test_cases = [
        "A man, a plan, a canal: Panama",]
    for s in test_cases:
        print(f"'{s}' is a palindrome: {solution.isPalindrome(s)}")
if __name__ == "__main__":
    main()