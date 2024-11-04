# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print("x=", x)
print("y=", y)
print("z=", z)

thistuple = ("apple", "banana", "cherry")
i = 0
while (i < len(thistuple)):
  print(thistuple[i])
  i = i + 1
