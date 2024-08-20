maas = int(input("Maaşınızı Yazınız: "))
if maas < 15000:
    prim=maas*0.06
else:
    prim=maas*0.04
    print("Prim: ",prim)