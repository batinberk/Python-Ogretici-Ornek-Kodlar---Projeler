# # saniye = int(input("Kaç Saniye?"))#
# # dakika = saniye/60#
# # print(saniye,"Saniye",int(dakika),"Dakika Yapar")
#
# # r = int(input("Yarıçapı Giriniz="))
# # pi=3.14
# # alan = pi * (r **2)
# # print("Dairenin Alanı= ",alan)
#
#
# # saniye = int(input("Kaç Saniye?= "))
# # saat = saniye // 3600
# # saniye = saniye% 3600
# # dakika = saniye // 60
# # saniye = saniye% 60
# # print(saat,"sa",dakika,"dk",saniye,"sn")
#
#
# #parola = input("Parola Giriniz= ")
# #if not parola:
#  #   print("Parola Boş Bırakılamaz")
# #else:
#    # print("İşlem Tamam")
#
#
# #yas = int(input("Yaşınız Kaç = "))
# #if yas < 14:
#   #  print("Merhaba Çocuk")
# #if 13 < yas < 19:
#   #  print("Merhaba Liseli")
# #if 18 < yas < 24:
#   #  print("Merhaba Ünili")
#
#
# #sayi = int(input("Sayı Giriniz: "))
# #if sayi % 2 == 0:
#   #  print("Sayı Çift Sayıdır.")
# #else:
#   #  print("Sayı Tek Sayıdır.")
#
#
# # kullanici = input("Kullanıcı Adı Giriniz= ")
# # if kullanici:
# #     print("Teşekkürler")
# # else:
# #     print("Kullanıcı Adı Boş Bırakılamaz.")
#
#
#
# # kullanici_adi = input("Kullanıcı Adı Giriniz= ")
# # sifre = input("Parolanız= ")
# # if kullanici_adi == "batinberk" and sifre == "12345":
# #     print("Parola Doğru Giriş Başarılı.")
# # else:
# #     print("Kullanıcı Adı Veya Parola Hatalı. Lütfen Tekrar Deneyiniz! ")
#
#
# # parola = input("Parola Giriniz= ")
# # toplam_uzunluk = len(parola)
# # mesaj = "Parolanız Toplam {} Karakterden Oluşuyor"
# #
# # if toplam_uzunluk > 12:
# #     print(mesaj.format(toplam_uzunluk))
# #     print("Parolanızın Toplam Uzunluğu 12 Karakterden Fazla Olamaz.")
# # else:
# #     print("Sisteme Hoşgeldiniz.")
#
#
# # bölünen = int(input("Bir Sayı Giriniz= "))
# # bölen = int(input("Bir Sayı Daha Giriniz= "))
# # şablon = "{} sayısı {} sayısına tam".format(bölünen,bölen)
# # if bölünen % bölen == 0:
# #     print(şablon, "bölünüyor!")
# # else:
# #     print(şablon, "bölünmüyor!")
#
# # for n in range(21,0,-3):
# #     print(n, end=" ")
#
#
# # top = 0
# # for n in range(1,100):
# #     top+=n
# # print(top)
#
# # a = "kodlama"
# # for harf in a:
# #     print(harf, end=(" "))
#
# tr_harfler = "ŞşÇçĞğÖöÜüİı"
# parola = input("Parola Giriniz= ")
# for karakter in parola:
#  if karakter in tr_harfler:
#         print("Parolada Türkçe Karakter Bulunamaz.")
#
#
# # a = 0
# # while a < 16:
# #     a += 1
# #     if a % 2 == 0:
# #         print(a, end=(" "))
#
#
# n = 1
# karar = int(input("Sayılar Kaça Kadar Sıralansın= "))
# while n < karar:
#     print(n)
#     n += 1


# say = 0
# metin = input("Lütfen Metin Giriniz= ")
# for n in metin:
#     if n == " ":
#         break
#         say+=say+1
# print("İlk Kelime", say, "Karakterine Sahiptir."),



#Demet oluşturma:
# demet = (1,2,3,4,5,6,7,8,9)
# print(demet)
#
# #Tek elemanlı bir demet tanımlama:
# demet = (1,)
# print(demet)
#
# #0. indekse ulaşma:
# demet = (1,2,3,4,5,6,7,8,9)
# print(demet[0])
#
# #Elemanların indexini yani kaçıncı sırada olduğunu bulma:
# demet = (1,2,3,”python”,”kodlama”,”Ali”)
# print(demet.index("python"))
#
# #Elemanların demette kaç defa geçtiğini bulma:
# demet = (1,23,34,34,2,1,4,5,1,1,34)
# print(demet.count(34))
#
# #Demetler değiştirilemez:
# demet = ("Elma","Armut","Muz")
# demet[0] = "Kiraz"
#
# #Demetler değiştirilemez:
# demet = ("Elma","Armut","Muz")
# demet.remove = "Kiraz" #Kiraz değerini silmeye çalıştık hata aldık

# import math
# dir(math)



                                          #KAREKÖK FONKSİYONU

# import math
# sayi = float(input("Sayi Giriniz: "))
# kok = math.sqrt(sayi)
# print(sayi, "Sayısının Karekökü", "=", kok)

                                          #İç İçe Karekök Fonksiyonu

# import math
# y = math.sqrt(math.sqrt(256))
# print(y)
                                       #FONKSİYON TANIMLAMAK VE ÇAĞIRMAK

# isim = "Ali"
# soyisim = "Yılmaz"
# d_yeri = "İzmir"
# yas = "28"
# print("isim : ", isim)
# print("soyisim : ", soyisim)
# print("doğum yeri : ", d_yeri)
# print("yaş : ", yas)


# def kayit_olustur(isim, soyisim, d_yeri, yas):
#     print("isim : ", isim)
#     print("soyisim : ", soyisim)
#     print("doğum yeri : ", d_yeri)
#     print("yaş : ", yas)
#
# kayit_olustur("Berk","Duman","İzmir","20")
# kayit_olustur("Batın","Kurşun","İzmir","20")


                    #ÖRNEK KARE BULMA FONKSİYON
# def kare_bul(i):
#  print(i**2)
# kare_bul(2)

                    #ÖRNEK SAYINLARIN 10 KATINI ALAN FONKSİYON

# def on_kat(n):
#     return (n*10)
# x = on_kat(3)
# print(x)

                  #ÖRNEK KARENİN ALANINI HESAPLAYAN FONKSİYON
# def kare(n):
#     print(n*n)
# kare(3)

                  #Ör: 1’den 10’a kadar yazdıran fonksiyon

# def say():
#     for n in range(1,11):
#         print(n, end=" ")
# say()

                    # time fonksiyonları: Zamanla ilgili işlemlerin yer aldığı modüldür. Bu modüle ait clock ve
                                        # sleep fonksiyonları bulunur.
# clock(): Programın başladığı andan itibaren geçen süreyi saniye olarak hesaplar.

# import time
#
# baslangicZamani = time.perf_counter()
# ad=input("İsminizi Giriniz: ")
# zaman = time.perf_counter() - baslangicZamani
# print("isminizi tam", zaman, "saniyede girdiniz")


# sleep(): Programın çalışması sırasında belirtilen süre kadar durmasını sağlar.


# import time
# time.sleep(5)
# ad = input("İsminizi Giriniz: ")


                            #Ör: Belli aralıklarda rastgele bir tamsayı üretme

# import random
# for i in range(1):
#     print(random.randrange(1,100), end= " ")

# import random
# for i in range(4):
#     print(random.randrange(1,10), end= " ")


                           #Ör: Sayısal loto Programı:
# import random
# for i in range(6):
#     print(random.randrange(1,50), end= " ")


                    # sample() fonksiyonu: random modülü içinde herhangi bir dizi içinden istediğimiz sayıda
                    # rastgele numune almamızı sağlar.

# import random
# liste = ["ahmet","elif","mehmet","sevgi","sevim","Selin","zeynep"]
# print(random.sample(liste,2))


# x = 25
# y = 12
# toplam = x+y
# print("İşlem Sonucu", toplam)


# sayi1 = int(input("Sayı giriniz: "))
# sayi2 = int(input("Bir Sayı Daha Giriniz: "))
# toplam = sayi1+sayi2
# print(toplam)

# sayi1 = int(input("1.Sayı: "))
# sayi2 = int(input("2.sayı: "))
# sayi3 = int(input("3.sayi: "))
# toplam = sayi1+sayi2+sayi3
# ort = toplam/3
# print("Aritmetik Ortalama",ort)


# vize = int(input("Vize Sonucunuz: "))
# final = int(input("Final Sonucunuz: "))
# ortalama = vize*0.40 + final*0.60
# print("Ortalamanız", ortalama)


# boy = float(input("Boyunuzu Giriniz: "))
# kg = int(input("Kilonuzu Giriniz: "))
# vucud_indeks = kg/(boy**2)
# print("Vücud Kitle Endeksiniz: ",vucud_indeks)

# isim = input("İsminiz: ")
# soyisim = input("Soyisminiz: ")
# veri = isim+" "+soyisim
# print(veri)


# ilce = input("İlçe Giriniz: ")
# il = input("İl Giriniz: ")
# veri = ilce+"/"+il
# print(veri)

# celsius = int(input("Celcius Değerini Giriniz: "))
# f = celsius*1.8 + 32
# print(f)
#
# a = int(input("1.sayı: "))
# b = int(input("2.sayı: "))
# c = int(input("3.sayı: "))
# z = (b**2 / (a-c)) + (c**2+b / (a*b))
# print("Sonuç", z)
#
#
# ogr_not = int(input("Notunuzu Giriniz: "))
# if ogr_not < 60:
#     print("Kaldı.")
#  else:
#     print("Geçti.")
#
# sayi = int(input("Sayı Giriniz: "))
# if sayi < 0:
#     sonuc = 0-sayi
# else:
#     sonuc = sayi
# print(sayi,"Sayısının Mutlak Değeri",sonuc)



# maas = int(input("Maaşınızı Yazınız: "))
# if maas < 15000:
#     prim=maas*0.06
# else:
#     prim=maas*0.04
# print("Prim: ",prim)


# maas = int(input("Maaşınızı Yazınız: "))
# if maas != 10000:
#     prim=maas*0.16
# else:
#     prim=maas**0.14
# print("Prim: ", prim)
#
#
# medeni_hal = input("Medeni Halinizi Giriniz: ")
# if medeni_hal=="evli":
#     print("Aile Yardımı Alabilirsiniz.")
# else:
#     print("Aile Yardımı Almak İçin Evli Olmalısınız. ")


# meslek = input("Mesleğinizi Yazınız: ")
# maas = int(input("Maaşınızı Yazınız: "))
# if meslek == "Doktor":
#     prim = maas*0.04
# if meslek == "Polis":
#     prim = maas*0.06
# if meslek == "Marangoz":
#     prim = maas*0.07
# else:
#     prim = maas*0.09
# print("Prim: ",prim)

# bolum = input("Bölümünüzü Giriniz: ")
# ogr_not = int(input("Notunuzu Giriniz: "))
# if bolum == "Kimya":
#     sonuc = ogr_not+20
#
# elif bolum == "Seramik":
#     sonuc = ogr_not+10
#
# elif bolum == "Bilgisayar":
#     sonuc = ogr_not+1
# else:
#     sonuc = ogr_not+7
#
#
# print("Ötelenmiş Not: " , sonuc)

# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
# delta=b**2-4*a*c
# print("Delta:",delta)
# if delta>0:
#  x1=(-b+(delta**0.5))/(2*a)
#  x2=(-b-(delta**0.5))/(2*a)
#  print("2 kök vardır.")
#  print("x1:",x1,"x2:",x2)
# elif delta==0:
#  x1=-b/(2*a)
#  print("1 kök vardır.\n")
#  print("x:",x1)
# elif delta<0:
#  print("Reel kök yoktur")


# kadi = input("Kullanıcı Adı Giriniz: ")
# parola = (input("Parola Giriniz: "))
#
# if kadi=="admin" and parola=="123":
#     print("Giriş Başarılı")
# else:
#     print("Giriş Başarısız")





































































































