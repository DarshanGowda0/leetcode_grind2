class Solution:
    def isValid(self, s: str) -> bool:
        mDict = {')': '(', ']':'[', '}':'{' }
        ans = []
        for c in s:
            if ans and (c in mDict and ans[-1] == mDict[c]):
                ans.pop()
            else:
                ans += c,
                
        # print(ans)
        return not ans
