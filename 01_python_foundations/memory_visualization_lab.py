x = [10, 20, 30]
y = x.copy()

print("Before change")
print("x:", x)
print("y:", y)

y.append(40)

print("\AFter change")
print("x:", x)
print("y:", y)

print("\nMemory locations")
print("x id:", id(x))
print("y id:", id(y))
