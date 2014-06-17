def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.numer = top
         self.denom = bottom

     def __str__(self):
         return str(self.numer)+"/"+str(self.denom)

     def show(self):
         print(self.numer,"/",self.denom)

     def __add__(self,otherfraction):
         newnum = self.numer*otherfraction.denom + \
                      self.denom*otherfraction.numer
         newden = self.denom * otherfraction.denom
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.numer * other.denom
         secondnum = other.numer * self.denom

         return firstnum == secondnum
     def __sub__(self, otherfrac):
     	 subnum = self.numer*otherfrac.denom - \
     	 		self.denom*otherfrac.numer
     	 subden = otherfrac.denom*self.denom
     	 commonsub = gcd(subnum, subden)
     	 return Fraction(subnum//commonsub, subden//commonsub)		



x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x - y)