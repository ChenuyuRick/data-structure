class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        ans = ''
        if n == 0 :
            return ans
        else :
            mini = min(strs, key = len)
            for i in range(len(mini)):
                curr = mini[i]
                if any(strs[j][i] != curr for j in range(n)):
                    break
                ans += curr
            
            return ans
