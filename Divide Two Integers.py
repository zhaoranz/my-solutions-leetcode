class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_v, max_v = -2 ** 31, 2**31-1
        sign = 1
        if dividend < 0: sign, dividend = -sign, -dividend
        if divisor < 0: sign, divisor = -sign, -divisor
        ans = 0
        while dividend >= divisor:
            cur = divisor
            mult = 1
            while cur+cur < dividend:
                cur += cur
                mult += mult
            dividend -= cur
            ans += mult
        ans = ans if sign > 0 else -ans
        
        if ans < min_v:
            return min_v
        elif min_v <= ans <= max_v:
            return ans
        else:
            return max_v
        
