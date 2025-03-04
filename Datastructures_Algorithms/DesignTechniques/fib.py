def fib2(n):
    fib_num = 1
    previous_2 = 0
    for i in range(n):
            previous_1 = fib_num
            fib_num = previous_1 +previous_2
            previous_2= previous_1



    return fib_num

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    fib_table = [0]*(n+1)

    fib_table[0]= 1
    fib_table[1]= 1
    for i in range(2,n + 1):
        fib_table[i] = fib_table[i-1]+fib_table[i-2]

    fib_num = 1
    previous_2 = 0
    for i in range(n):
            previous_1 = fib_num
            fib_num = previous_1 +previous_2
            previous_2= previous_1



    return fib_table[n]

print(fib(0))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))