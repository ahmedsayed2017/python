def pyram(n):
    for i in range(n):
        print(" "*(n-i), "*"*(i+1)+"*"*i)
    
def pyram2(n, reverse=False):
    s = (2*n-1)
    for i in range(n):
            #print(" "*(i)  ,"*"*(n-i)+"*"*(n-2*i+1))
            spaces = " "*i
            stars = "*"* s
            print(spaces + stars)
            s -= 2


def decorator(f1, f2):
    n = eval(input("Enter number of lines for function1: "))
    b = eval(input("Enter number of lines for function2: "))
    def dec():
        f1(n)
        f2(b)
    return dec

new_shape = decorator(pyram, pyram2)
new_shape()
