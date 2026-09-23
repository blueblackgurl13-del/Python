# Assignment Operators
# Example 1
x = 5

print(x)

# Example 2
x = 5

x += 3

print(x)

# Example 3
x = 5

x -= 3

print(x)

# Example 4
x = 5

x *= 3

print(x)

# Example 5
x = 5

x /= 3

print(x)

# Example 6
x = 5

x%=3

print(x)

# Example 7
x = 5

x//=3

print(x)

# Example 8
x = 5

x **= 3

print(x)

# Example 9
x = 5

x &= 3

print(x)

# Example 10
x = 5

x |= 3

print(x)

# Example 11
x = 5

x ^= 3

print(x)

# Example 12
x = 5

x >>= 3

print(x)

# Example 13
x = 5

x <<= 3

print(x)

# Example 14
print(x := 3)

# The Walrus Operator
# Example
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")