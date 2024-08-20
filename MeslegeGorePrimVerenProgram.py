meslek = input("Mesleğinizi Yazınız: ")
maas = int(input("Maaşınızı Yazınız: "))
if meslek == "Doktor":
    prim = maas*0.04
if meslek == "Polis":
    prim = maas*0.06
if meslek == "Marangoz":
    prim = maas*0.07
else:
    prim = maas*0.09
print("Prim: ",prim)