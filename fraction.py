class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den
        # print("BEFORE:",self.num, self.den)
        if den < num:
            self.__validateFraction(num, den)
            
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __validateFraction(self,  num, den):
        res = self.__lcm(num, den)
        print(res)
        self.num = self.num * res
        self.den = self.den * res
        # print("BEFORE:",self.num, self.den)
    
    def __gcd(self, a, b):
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a
    
    def __lcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        gcd = self.__gcd(a, b)
        return (a * b) // gcd
    
    def __simplify_fraction(self, num, den):
        gcd = self.__gcd(num, den)
        simplified_num = num // gcd
        simplified_den = den // gcd
        return simplified_num, simplified_den
    
    def __add__(self, other):
        tempNum = self.num*other.den + self.den*other.num
        tempDen = self.den*other.den
        simplified_num, simplified_den = self.__simplify_fraction(tempNum, tempDen)
        return f"{simplified_num}/{simplified_den}"
    
    def __sub__(self, other):
        tempNum = self.num*other.den - self.den*other.num
        tempDen = self.den*other.den
        simplified_num, simplified_den = self.__simplify_fraction(tempNum, tempDen)
        return f"{simplified_num}/{simplified_den}"
    
    def __mul__(self, other):
        tempNum = self.num*other.num
        tempDen = self.den*other.den
        simplified_num, simplified_den = self.__simplify_fraction(tempNum, tempDen)
        return f"{simplified_num}/{simplified_den}"
    
    def __truediv__(self, other):
        tempNum = self.num*other.den
        tempDen = self.den*other.num
        simplified_num, simplified_den = self.__simplify_fraction(tempNum, tempDen)
        return f"{simplified_num}/{simplified_den}"
    