# Identity Operators
# Example 1
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

print(x is y)

print(x == y)

# Example 2
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

print(x is not y)

print(x != y)

# Examples
# Example 1
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# Example 2
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# Difference Between is and ==
# Example
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)