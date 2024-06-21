class Solution:
    def romanToInt(self, s):
        """s: str,
        -> int"""
        #37ms and 16.58MB
        value=0
        roman={'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        for letter, pos_letter in zip(s,s[1:]):
            if roman[letter]<roman[pos_letter]:
                value-=roman[letter]
            else:
                value+=roman[letter]                 
        return value + roman[s[-1]]
