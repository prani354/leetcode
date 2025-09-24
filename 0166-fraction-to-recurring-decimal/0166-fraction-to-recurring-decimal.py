class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        negative = (numerator < 0) ^  (denominator < 0)
        numerator , denominator = abs(numerator),abs(denominator)

        int_part = numerator // denominator
        res = "-" if negative else ""
        res += str(int_part) + '.'

        rem = numerator % denominator
        rems = {}
        dec_part = []

        while rem != 0:
            if rem in rems:
                repeat_idx = rems[rem]
                dec_part.insert(repeat_idx,'(')
                dec_part.append(')')
                break

            rems[rem] = len(dec_part)
            rem *= 10
            digit = rem // denominator
            dec_part.append(str(digit))
            rem %= denominator

        return res + "".join(dec_part)
       