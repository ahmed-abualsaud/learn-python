name="Ahmed Mohamed"
age=20
male=True
income=5000.50

print("\n")

print("Name:", name)
print("Age:", age)
print("Male:", male)
print("Income:", income)

print("\n")

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of male:", type(male))
print("Type of income:", type(income))

print("\n")
print("=====================================================")
print("\n")

# number of variables must match the number of values when unpacking a list or tuple
a,b,c,d,e=1,"2",3.1,True,1+1j

print(a,b,c,d,e)

print("\n")

print("a:", a, "Type:", type(a))
print("b:", b, "Type:", type(b))
print("c:", c, "Type:", type(c))
print("d:", d, "Type:", type(d))
print("e:", e, "Type:", type(e))

print("\n")
print("=====================================================")
print("\n")

f=str(1)            # convert int to str
g=str(3.14)         # convert float to str
h=float(5)          # convert int to float
i=int(3.14)         # convert float to int
j=complex(1)        # convert int to complex
k=bool(1)           # convert int to bool
l=bool(0)           # convert int to bool
m=float("3.14")     # convert str to float
n=complex(2,3)      # convert int to complex
o=complex("1+2j")   # convert str to complex
p=bin(10)           # convert int to binary
q=bool('0')         # convert str to bool, any non-empty string is True

print("f:", f, "Type:", type(f))
print("g:", g, "Type:", type(g))
print("h:", h, "Type:", type(h))
print("i:", i, "Type:", type(i))
print("j:", j, "Type:", type(j))
print("k:", k, "Type:", type(k))
print("l:", l, "Type:", type(l))
print("m:", m, "Type:", type(m))
print("n:", n, "Type:", type(n))
print("o:", o, "Type:", type(o))
print("p:", p, "Type:", type(p))
print("q:", q, "Type:", type(q))

print("real part of o:", o.real, "Type:", type(o.real))
print("imaginary part of o:", o.imag, "Type:", type(o.imag))