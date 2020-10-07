cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    print(n)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
