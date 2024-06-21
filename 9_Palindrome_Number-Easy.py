class Solution:
    def isPalindrome(self, x):
        """x: int
        -> bool"""
        #62ms and 16.49MB
        """
        x=str(x)
        index=len(x)//2
        for i in range (index):
            if x[i] == x[-i-1]:
                continue
            else:
                return False
        return True"""
        #48ms and 16.45MB
        if x<0:
            return False
        test=0
        y=x
        while y:
            test=test*10+y%10
            y//=10
        return x==test
        