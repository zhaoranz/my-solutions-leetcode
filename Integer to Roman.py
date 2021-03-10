class Solution:
    def intToRoman(self, num: int) -> str:
        roman_digit=[("M",1000), ("CM",900),("D",500),("CD", 400),("C",100),("XC",90),("L",50),
                    ("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)]
   

        romans =[]

        for roman, digit in roman_digit:
            if num ==0:
                break
            count, num = divmod(num, digit)
            romans.append(roman * count)
        return "".join(romans)
