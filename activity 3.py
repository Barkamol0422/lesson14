def add(a,b):
    return a+b
def sub(a,b):
    return b-a
def mul(a,b):
    return a*b
def div(a,b):
    return b/a
while True:
    print("a. Addition")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")
    c=input("Write your choice(a/b/c/d): ")
    a,b=map(int,input().split())
    if c=="a":
        print(add(a,b))
    elif c=="b":
        print(sub(a,b))
    elif c=="c":
        print(mul(a,b))
    elif c=="d":
        print(div(a,b))
    else:
        break
        print("Incorrect choice")
exit()
    
    
    
    
