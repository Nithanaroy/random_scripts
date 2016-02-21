import re


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        m = re.match(r'[^0-9.+e-]', s)
        if m is None:
            if s.find('e') > 0:
                # Only one 'e'
                if s.count('e') > 1:
                    return False

                mantissa, exponent = s.split('e')
                return self.may_have_decimal(mantissa) and self.valid_without_decimal(exponent, True)
            else:
                return self.may_have_decimal(s)
        return False

    def may_have_decimal(self, n):
        if len(n) > 0 and (n[0] == '-' or n[0] == '+'):
            n = n[1:]

        if n.count('.') == 0:
            return self.valid_without_decimal(n)
        else:
            # Only one decimal point when present
            if n.count('.') > 1:
                return False
            else:
                whole, fraction = n.split('.')
                if len(whole) is 0:
                    return self.valid_without_decimal(fraction, True)
                elif len(fraction) is 0:
                    return self.valid_without_decimal(whole)
                return self.valid_without_decimal(whole) and self.valid_without_decimal(fraction, True)

    def valid_without_decimal(self, n, positive_only=False):
        if len(n) == 0:
            return False

        if positive_only:
            return self.valid_positive_number(n)
        else:
            if n[0] == '-' or n[0] == '+':
                return self.valid_positive_number(n[1:])
            else:
                return self.valid_positive_number(n)

    @staticmethod
    def valid_positive_number(n):
        if len(n) > 0:
            if n[0] == '+':
                return re.search(r'[^0-9]', n[1:]) is None
            else:
                return re.search(r'[^0-9]', n) is None


if __name__ == '__main__':
    s = Solution()

    print s.isNumber("+++")  # Should be false, of course!
    print s.isNumber(" 005047e+6")  # Should be true
    print s.isNumber('+.0')  # Should be true
    print s.isNumber('-1.21e1')
    print s.isNumber('-.1')  # Should be true
    print s.isNumber('-3.')  # Should be true
    print s.isNumber('-.')  # Should be False
    print s.isNumber('1 23')
    print s.isNumber('1 a')
    print s.isNumber('1.5')
    print s.isNumber('1.5a')
    print s.isNumber('1e5a')
    print s.isNumber('1e5')
