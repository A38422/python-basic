class Roman:
    def __init__(self, number):
        self.number = number
    def convert(self):
        num = [
            1, 4, 5, 9, 
            10, 40, 50, 90, 
            100, 400, 500, 900, 
            1000
            ]
        roman_num = [
            'I', 'IV', 'V', 'IX',
            'X', 'XL', 'L', 'XC',
            'C', 'CD', 'D', 'CM',
            'M'
            ]
        roman = ''
        i = 12
        while i >= 0:
            temp = int(self.number / num[i])
            self.number %= num[i]
            while temp > 0:
                roman += roman_num[i]
                temp -= 1
            i -= 1  
        return roman

rm = Roman(10)
print(rm.convert())
