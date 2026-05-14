class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        if s == " ":
            return True

        for ch in s:
            if ch.isalnum():
                new_str += ch.lower() 

        string = ""
        
        for i in range(len(new_str)-1,-1,-1):
            string += new_str[i]

        if new_str == string:
            return True

        return False
        