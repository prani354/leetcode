class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str += ch

        print(new_str.lower())
        new_str = new_str.lower()

        return new_str == new_str[::-1]
