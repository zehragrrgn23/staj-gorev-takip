gorevler = []

while True:
    print()
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
        gorevler.append(gorev)
        print("Görev eklendi:", gorev)

    elif secim == "1":
        print("\n===== GÖREVLER =====")

        if len(gorevler) == 0:
            print("Henüz görev yok.")
        else:
            for i, gorev in enumerate(gorevler, start=1):
                print(f"{i}. {gorev}")

    elif secim == "5":
        print("Program kapatılıyor...")
        break

    else:
        print("Geçersiz seçim.")