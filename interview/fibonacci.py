
def fibonacci(n):
    if n == 0:
        return
    numbers = [0,1]
    next = numbers[-1] + numbers

def fib(n):
    numbers = [0,1]
    if n == 1:
        return [0]
    elif n <= 0:
        return []

    for i in range(n-2):
        next_num = numbers[-1] + numbers[-2]
        numbers.append(next_num)
    return numbers 

print(fib(-5))


#if "__name__" == "__main__":
#    print(fibonacci(5))
