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

        yeni_gorev = {
            "ad": gorev,
            "tamamlandi": False
        }

        gorevler.append(yeni_gorev)
        print("Görev eklendi:", gorev)

    elif secim == "1":
        print("\n===== GÖREVLER =====")

        if len(gorevler) == 0:
            print("Henüz görev yok.")
        else:
            for i, gorev in enumerate(gorevler, start=1):
                if gorev["tamamlandi"]:
                    durum = "✓"
                else:
                    durum = " "

                print(f"{i}. [{durum}] {gorev['ad']}")

    elif secim == "3":
        if len(gorevler) == 0:
            print("Henüz görev yok.")
        else:
            print("\n===== GÖREVLER =====")

            for i, gorev in enumerate(gorevler, start=1):
                if gorev["tamamlandi"]:
                    durum = "✓"
                else:
                    durum = " "

                print(f"{i}. [{durum}] {gorev['ad']}")

            secim_gorev = int(input("Tamamlamak istediğiniz görev numarası: "))

            if 1 <= secim_gorev <= len(gorevler):
                gorevler[secim_gorev - 1]["tamamlandi"] = True
                print("Görev tamamlandı!")
            else:
                print("Geçersiz görev numarası.")

    elif secim == "4":
        if len(gorevler) == 0:
            print("Henüz görev yok.")
        else:
            print("\n===== GÖREVLER =====")

            for i, gorev in enumerate(gorevler, start=1):
                if gorev["tamamlandi"]:
                    durum = "✓"
                else:
                    durum = " "

                print(f"{i}. [{durum}] {gorev['ad']}")

            secim_gorev = int(input("Silmek istediğiniz görev numarası: "))

            if 1 <= secim_gorev <= len(gorevler):
                silinen_gorev = gorevler.pop(secim_gorev - 1)
                print("Görev silindi:", silinen_gorev["ad"])
            else:
                print("Geçersiz görev numarası.")


    elif secim == "5":
        print("Program kapatılıyor...")
        break

    else:
        print("Geçersiz seçim.")