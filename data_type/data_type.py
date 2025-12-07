
x: int = 5
y: float = 5.5
z: str = "5.55"
a: list[int] = [1, 2, 3]

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

print(a)
print(type(a))


names: list[str] = ["bob", "Joe", "Sue", "James", "Charly", "Smith"]

long_names: list[str] = [name for name in names if len(name) > 4]

print(f"names: {names}")
print(f"long names: {long_names}")