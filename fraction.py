# This program defines a Fraction class and various associated methods. 
# This is merely instructional and not intended to be executable.

# Through appropriate overrides of the build in standard methods in python,
# we can define a fraction class that behaves like a number.


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self,top,bottom): #constructor method

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common) 

# At this point, one would also want to override methods for divsion, floor div,
# modulo, floor and mod, raise to power, left bit shift, right bit shift, bitwise
# and, bitwise xor, bitwise or, etc

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x*y)