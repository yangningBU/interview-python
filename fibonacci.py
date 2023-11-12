test_out = [1,1,2,3,5,8,13,21,34,55]

def fib(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fibs = [] 
for i in range(10):
    fibs.append(fib(i+1))

print(fibs == test_out)