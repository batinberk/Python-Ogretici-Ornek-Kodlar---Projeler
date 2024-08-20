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
# # if kullanici_adi == "batinberk" and sifre == "03231235":
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























































