import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub('[^a-zA-Z0-9]','',s) #注意里面有中括号[^a-zA-Z0-9]和上尖符号^
        s=s.lower()
        return s==s[::-1] #注意是两个==