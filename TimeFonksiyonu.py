import time

baslangicZamani = time.perf_counter()
ad=input("İsminizi Giriniz: ")
zaman = time.perf_counter() - baslangicZamani
print("isminizi tam", zaman, "saniyede girdiniz")