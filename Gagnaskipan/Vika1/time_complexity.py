import time

def addition(num1, num2):
    return num1 + num2

def logarithmic_example(n):
    a = 0
    while n >= 1:
        n = n // 2
        a += 1
    return a

def print_list(lis):
    for elem in lis:
        print(elem)

def double_loop(n):
    a = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a += 1
    print(a)

def ntimeslogn(n):
    a = 0
    for i in range(n):
        a += logarithmic_example(n)
    print(a)

#ntimeslogn(10000)

def power(num1, num2):
    total = num1
    for i in range(num2):
        total *= num1
    total2 = num1 ** num2
    print(total, total2)

lis = []
start_time = time.time()
for i in range(100):
    lis.append(i)
double_loop(lis)
end_time = time.time()
elapsed = end_time - start_time
print(elapsed)