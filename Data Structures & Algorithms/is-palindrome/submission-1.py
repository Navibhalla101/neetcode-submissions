class Solution:
    def isPalindrome(self, s: str) -> bool:

       ## newStr = "".join(c.lower() for c in s if c.isalnum())


        newStr = ""
        for c in s: 
            if c.isalnum():
                newStr += c.lower()
        

        reverseStr = newStr[::-1]

        if newStr == reverseStr:
            return True 
        else:
            return False


'''
.isalnum(): True for letters and digits, False for spaces and punctuation
    can read it as is all l and num? 
.lower() — lowercases, and returns a new string 
"".join(list_of_strings)
'''