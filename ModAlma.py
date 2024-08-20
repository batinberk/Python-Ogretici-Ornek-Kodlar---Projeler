bölünen = int(input("Bir Sayı Giriniz= "))
bölen = int(input("Bir Sayı Daha Giriniz= "))
şablon = "{} sayısı {} sayısına tam".format(bölünen,bölen)

if bölünen % bölen == 0:
    print(şablon, "bölünüyor!")
else:
    print(şablon, "bölünmüyor!")