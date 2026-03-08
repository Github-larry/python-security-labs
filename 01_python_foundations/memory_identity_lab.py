a = 50 
b = a

print("a id:", id(a))
print("b id:", id(b))

b = 100

print("After modification")

print("a id:", id(a))
print("b id:", id(b))