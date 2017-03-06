def fib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def concat_datas(*args):
    data = args[0]
    for i in range(1,3):
        data = data + '/' + args[i]
    return data

if __name__ == "__main__":
    import sys
    resultado = fib(int(sys.argv[1]))
    print(resultado)