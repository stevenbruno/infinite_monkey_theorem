# This program defines a Fraction class and various associated methods. 
# this is merely instructional and not intended to be executable


class Fraction:

    def __init__(self,top,bottom): #constructor method

	    self.num = top
	    self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
