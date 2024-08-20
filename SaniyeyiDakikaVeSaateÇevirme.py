saniye = int(input("Kaç Saniye?= "))
saat = saniye // 3600
dakika = saniye // 60
saniye = saniye% 60
print(saat,"sa",dakika,"dk",saniye,"sn")