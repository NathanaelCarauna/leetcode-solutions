class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxlen = max(len(a), len(b))
        a=a.zfill(maxlen)
        b=b.zfill(maxlen)
        result = ''
        carry = 0

        for i in range(maxlen-1,-1,-1):
            r = carry
            r += 1 if a[i] == '1' else 0
            r += 1 if b[i] == '1' else 0
            result = ('1' if r %2 == 1 else '0') + result
            carry = 0 if r<2 else 1
        if carry != 0 : result = '1' + result
        return result.zfill(maxlen)
