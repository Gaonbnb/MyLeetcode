具体讲解可以看代码随想录，大概就是从后往前的找匹配的问题 substr()
```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        m = len(haystack)
        n = len(needle)
        # 构建next
        
        next_ = [0] * n
        j = -1
        next_[0] = j
        for i in range(1, n):
            while j >= 0 and needle[i] != needle[j+1]:
                j = next_[j]
            if needle[i] == needle[j+1]:
                j += 1
            next_[i] = j
        
        # 利用next进行匹配

        j = -1
        for i in range(0, m):
            while j >= 0 and haystack[i] != needle[j+1]:
                j = next_[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == n - 1:
                return i - n + 1
        return -1
```
