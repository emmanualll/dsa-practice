class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.strip()

        if not s:
            return 0

        i = 0
        sign = 1
        result = 0


        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > INT_MAX % 10
            ):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result