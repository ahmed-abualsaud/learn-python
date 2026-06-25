a=10
b=3
c=15

# mathematical operations
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=a**b
i=a//b
j=abs(a-b)
k=divmod(a,b)
l=pow(a,b)


# comparison operations
m=a==b
n=a!=b
o=a>b
p=a<b
q=a>=b
r=a<=b
s=b<a<c
t=b>a>c
u=b>a<c
v=b<a>c

print("\n")

print("Mathematical Operations:")
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
print("Division:", f)
print("Modulus:", g)
print("Exponentiation:", h)
print("Floor Division:", i)
print("Absolute Value:", j)
print("Divmod:", k)
print("Power:", l)

print("\n")
print("======================================================")
print("\n")


print("Comparison Operations:")
print("Equal:", m)
print("Not Equal:", n)
print("Greater Than:", o)
print("Less Than:", p)
print("Greater Than or Equal To:", q)
print("Less Than or Equal To:", r)
print("Chained Comparison (b<a<c):", s)
print("Chained Comparison (b>a>c):", t)
print("Chained Comparison (b>a<c):", u)
print("Chained Comparison (b<a>c):", v)

print("\n")
print("======================================================")
print("\n")

equation=(a+b*c-d/e+f**g-h//i)
parenthesis_equation=((a+b)*(c-d)/(e+f)**g-h//i)

print("Complex Equation a+b*c-d/e+f**g-h//i:", equation)
print("Parenthesis Equation (a+b)*(c-d)/(e+f)**g-h//i:", parenthesis_equation)