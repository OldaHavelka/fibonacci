def fib(number1, number2, iterations):
    if number2<number1:
        temp=number2
        number2=number1
        number1=temp
    for i in range(iterations):
        number = number1 + number2
        number1 = number2
        number2 = number
    return number1

def fibo(number1, number2, iterations):
    if number2<number1:
        temp=number2
        number2=number1
        number1=temp
    if iterations<=0:
        return number1
    else:
        return fib(number1+number2, number2, iterations-1)

for i in range(10):
    print(fib(0,2,i))

for i in range(10):
    print(fibo(0,2,i))