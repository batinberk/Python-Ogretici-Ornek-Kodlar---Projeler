a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
delta=b**2-4*a*c
print("Delta:",delta)
if delta>0:
    x1=(-b+(delta**0.5))/(2*a)
    x2=(-b-(delta**0.5))/(2*a)
    print("2 kök vardır.")
    print("x1:",x1,"x2:",x2)
elif delta==0:
    x1=-b/(2*a)
    print("1 kök vardır.\n")
    print("x:",x1)
elif delta<0:
    print("Reel kök yoktur")