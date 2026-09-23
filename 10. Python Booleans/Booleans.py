# Boolean Values
# Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables
# Example 1
print(bool("Hello"))
print(bool(15))

# Example 2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True
# Example 
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# Some Values are False
# Example 1
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Example 2
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
# Example 1
def myFunction() :
  return True

print(myFunction())

# Example 2
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Example 3
x = 200
print(isinstance(x, int))