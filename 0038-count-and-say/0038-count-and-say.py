class Solution:
    def countAndSay(self, n: int) -> str:
        def describe(s):
            result = ""
            i = 0
            while i < len(s):
                char = s[i]
                count = 0
                while i < len(s) and s[i] == char:
                    count += 1
                    i += 1
                result += str(count) + char
            return result
        
        result = "1"
        for _ in range(n-1):
            result = describe(result)
        return result
