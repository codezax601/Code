class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        d = {} 
        res = 0
        start = 0
        for i in range(n):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1 
            else:
                res = max(res, i-start+1)
            d[s[i]] = i
            
        return res
