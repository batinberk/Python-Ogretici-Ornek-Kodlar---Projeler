tr_harfler = "ŞşÇçĞğÖöÜüİı"
parola = input("Parola Giriniz= ")
for karakter in parola:
    if karakter in tr_harfler:
        print("Parolada Türkçe Karakter Olamaz.")