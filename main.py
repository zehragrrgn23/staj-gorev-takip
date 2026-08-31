print("================================")
print("       STAJ GÖREV TAKİP")
print("================================")

print("1 - Görevleri göster")
print("2 - Yeni görev ekle")
print("3 - Görevi tamamla")
print("4 - Görev sil")
print("5 - Çıkış")

secim = input("Seçiminiz: ")

if secim == "2":
    gorev = input("Yeni görevi girin: ")
    print("Görev eklendi:", gorev)