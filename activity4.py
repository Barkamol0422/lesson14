def sq(a):
    return 4*a
def rc(d,e):
    return 2*(d+e)
b=input("a. perimeter of square , b. perimeter of rectangle: ")
if b=="a":
    a=int(input("Write the side of square: "))
    print(sq(a))
else:
    d,e=map(int,input("Write two sides of rectangle: ").split())
    print(rc(d,e))
