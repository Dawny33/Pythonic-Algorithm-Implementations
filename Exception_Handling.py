import math

num = int(input("Pl enter"))


try:
     print(math.sqrt(num))
except:
     print("Bad value")
     print("Using absolute value")
     print(int(abs(num)))

##if num<0:
##	raise RuntimeError("No negatives")
##else:
##	print(math.sqrt(num))