def power(base, exp):
    if exp == 0:
        return 1
    return base*power(base, exp-1)

#print(power(2,4))

def mul(a,b):
    if b ==0:
        return 0
    return a + mul(a,b-1)

print(mul(4,5))

def factorial(n):
    if n == 0:
        return 0
    factorial(n-1)

def natural(n):
    if n == 0:
        return 0
    natural(n-1)
    print(n, end=' ')

natural(5)

def sum_of_digits(x):
    if x < 10:
        return x
    right_digit = x % 10
    other_digits = x // 10
    return right_digit + sum_of_digits(other_digits)

#print(sum_of_digits(254))

def fib(n): #Mikil tímaflækja
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#print(fib(50))

def fibo(n, i=1,b=0): #Miklu minni tíma flækja
    if n == 0:
        return i
    c = i + b
    return fibo(n-1, b, c)

def a(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return a(m-1, 1)
    return a(m-1, a(m,n-1))

#print(a(1,1))