import json


def gorevleri_yukle():
    try:
        with open("gorevler.json", "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return []


def gorevleri_kaydet(gorevler):
    with open("gorevler.json", "w", encoding="utf-8") as dosya:
        json.dump(gorevler, dosya, ensure_ascii=False, indent=4)


gorevler = gorevleri_yukle()


while True:
    print()
    print("================================")
    print("       STAJ GÖREV TAKİP SİSTEMİ")
    print("================================")

    print("1 - Görevleri göster")
    print("2 - Yeni görev ekle")
    print("3 - Görevi tamamla")
    print("4 - Görev sil")
    print("5 - Çıkış")
    print("6 - Görev ara")

    secim = input("Seçiminiz: ")

    if secim == "1":
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

    elif secim == "2":
        gorev = input("Yeni görevi girin: ")

        yeni_gorev = {
            "ad": gorev,
            "tamamlandi": False
        }

        gorevler.append(yeni_gorev)
        gorevleri_kaydet(gorevler)

        print("Görev eklendi:", gorev)

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

            secim_gorev = int(
                input("Tamamlamak istediğiniz görev numarası: ")
            )

            if 1 <= secim_gorev <= len(gorevler):
                gorevler[secim_gorev - 1]["tamamlandi"] = True
                gorevleri_kaydet(gorevler)

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

            secim_gorev = int(
                input("Silmek istediğiniz görev numarası: ")
            )

            if 1 <= secim_gorev <= len(gorevler):
                silinen_gorev = gorevler.pop(secim_gorev - 1)
                gorevleri_kaydet(gorevler)

                print("Görev silindi:", silinen_gorev["ad"])
            else:
                print("Geçersiz görev numarası.")

    elif secim == "5":
        print("Program kapatılıyor...")
        break

    elif secim == "6":
        aranan = input("Aramak istediğiniz görev: ")
        bulundu = False

        for gorev in gorevler:
            if aranan.lower() in gorev["ad"].lower():
                print(gorev["ad"])
                bulundu = True

        if not bulundu:
            print("Arama sonucu bulunamadı.")

    else:
        print("Geçersiz seçim.")