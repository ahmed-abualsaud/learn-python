# you can write import math as mt
# also you can write from math import factorial as fact then use fact() directly
# or you can write from math import factorial and then use factorial() directly
# or you can write from math import * and then use factorial() directly

import math

# import math as mt
# from math import *
# from math import factorial
# from math import factorial as fact
# from math import factorial, sin, cos

f=math.factorial(10)
e=math.exp(10)
e2=math.exp2(10)
n=math.log(10)
n3=math.log(10, 3)
n10=math.log10(10)
sr=math.sqrt(10)
d=math.degrees(10)
r=math.radians(10)
rs=math.sin(math.radians(10))
rc=math.cos(math.radians(10))
asi=math.asin(rs)
aco=math.acos(rc)
cosi=math.copysign(10, -1)
flo=math.floor(9.5)
cei=math.ceil(9.5)
ef=math.erf(1)
gm=math.gamma(3)

print("\n")

print("Factorial of", 10, "is:", f)
print("Natural Exponential of", 10, "is:", e)
print("Exponential of", 10, "with base 2 is:", e2)
print("Natural Logarithm of", 10, "is:", n)
print("Logarithm of", 10, "with base 3 is:", n3)
print("Logarithm of", 10, "with base 10 is:", n10)
print("Square Root of", 10, "is:", sr)
print("Degrees of", 10, "radians is:", d)
print("Radians of", 10, "degrees is:", r)
print("Sine of", 10, "degrees is:", rs)
print("Cosine of", 10, "degrees is:", rc)
print("Arcsine of", rs, "degrees is:", asi)
print("Arccosine of", rc, "degrees is:", aco)
print("Value of pi is:", math.pi)
print("Value of tau is:", math.tau)
print("Value of e is:", math.e)
print("Value of infinity is:", math.inf)
print("Copysign of 10 with sign of -1 is:", cosi)
print("Floor of 9.5 is:", flo)
print("Ceiling of 9.5 is:", cei)
print("Error function of 1 is:", ef)
print("Gamma function of 3 is:", gm)
