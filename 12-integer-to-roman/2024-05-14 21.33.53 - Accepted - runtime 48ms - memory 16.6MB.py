class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            roman = ""
        elif num < 4:
            roman = "".join(["I" for i in range(num)])
        elif num < 9:
            if num < 5:
                roman = "IV"
            else:
                roman = "V"
                roman += self.intToRoman(num-5)
        elif num < 40:
            if num < 10:
                roman = "IX"
            else:
                roman = ""
                plc = 10
                for i in range(10, num+1, 10):
                    roman += "X"
                    plc = i
                roman += self.intToRoman(num-plc)
        elif num < 90:
            if num < 50:
                roman = "XL"
                roman +=  self.intToRoman(num-40)
            else:
                roman = "L"
                roman += self.intToRoman(num-50)
        elif num < 400:
            if num < 100:
                roman = "XC"
                roman += self.intToRoman(num-90)
            else:
                roman = ""
                plc = 100
                for i in range(100, num+1, 100):
                    roman += "C"
                    plc = i
                roman += self.intToRoman(num-plc)
        elif num < 900:
            if num < 500:
                roman = "CD"
                roman += self.intToRoman(num-400)
            else:
                roman = "D"
                roman += self.intToRoman(num-500)
        else:
            if num < 1000:
                roman = "CM"
                roman += self.intToRoman(num-900)
            else:
                roman = ""
                plc = 1000
                for i in range(1000, num+1, 1000):
                    roman += "M"
                    plc = i
                roman += self.intToRoman(num-plc)
        return roman


        