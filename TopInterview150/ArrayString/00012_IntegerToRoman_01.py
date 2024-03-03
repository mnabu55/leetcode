

class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'), 
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'), 
            (4, 'IV'),
            (1, 'I')
        ]

        romans = ''

        for integer, roman in int_to_roman_map:
            quotient, num = divmod(num, integer)
            if quotient >= 1:
                romans += roman * quotient

        return romans

    def intToRoman_other(self, num: int) -> str:
        mapping = {
            1000: "M", 900: "CM",
            500: "D",  400: "CD",
            100: "C",  90: "XC",
            50: "L",   40: "XL",
            10: "X",   9: "IX",
            5: "V",    4: "IV",
            1: "I",
        }

        romans = ""

        for integer in mapping.keys():
            while integer <= num:
                romans += mapping[integer]
                num -= integer

        return romans

solution = Solution()
assert solution.intToRoman(num=3) == "III"
assert solution.intToRoman(num=58) == "LVIII"
assert solution.intToRoman(num=1994) == "MCMXCIV"