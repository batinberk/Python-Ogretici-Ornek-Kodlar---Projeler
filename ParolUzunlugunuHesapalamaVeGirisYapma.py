parola = input("Parola Giriniz= ")
toplam_uzunluk = len(parola)
mesaj = "Parolanız Toplam {} Karakterden Oluşuyor"

if toplam_uzunluk > 12:
    print(mesaj.format(toplam_uzunluk))
    print("Parolanızın Toplam Uzunluğu 12 Karakterden Fazla Olamaz.")
else:
    print("Sisteme Hoşgeldiniz.")