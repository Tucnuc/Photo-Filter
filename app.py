from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageOps
import os
import time

loc = ["start"]

while True:
  if "start" in loc:
    print("Vítejte v našem editoru obrázků.")
    time.sleep(1)
    print("Můžete využít už vytvořené filtry naším zkušeným týmem.")
    time.sleep(1)
    print("Nebo si zkusit vytvořit svůj vlastní!")
    time.sleep(1)
    print("Nezapomeňtě nahrát obrázek/y do stejné složky jako naši aplikaci a můžeme začít.")
    time.sleep(1)
    loc.clear()
    loc.append("photo_equip")
    print("")

  if "photo_equip" in loc:
    nazev_obrazku = input("Jméno vybraného obrázku: ")
    print("")

    obrazek = Image.open(nazev_obrazku)

    max_vyska = 500
    if obrazek.size[1] > max_vyska:
        ratio = max_vyska / obrazek.size[1]
        new_sirka = int(obrazek.size[0] * ratio)
        obrazek.thumbnail((new_sirka, max_vyska))

    display(obrazek)
    time.sleep(1)
    print("")
    loc.clear()
    loc.append("filter_options")

  if "filter_options" in loc:
    while True:
      choice1 = input("Chcete použít předpřipravený filtr nebo vytvořit vlastní? [1 - předpřipravený, 2 - vlastní]: ")
      time.sleep(0.5)
      print("")
      if choice1 == "1":
        loc.clear()
        loc.append("premade")
        break
      elif choice1 == "2":
        loc.clear()
        loc.append("custom")
        break
      else:
        print("Špatná odpověď.")

  if "premade" in loc:
    def seznam(item):
      print("  " + item)
      time.sleep(0.2)

    print("Seznam filtrů:")
    time.sleep(0.5)
    seznam("1. Černobílý Filtr")
    seznam("2. Sepia Filtr")
    seznam("3. Negativní Filtr")
    seznam("4. Ztmavení Barev")   
    seznam("5. Větší Saturace")
    seznam("6. Zvíraznění Obrysů")
    seznam("7. Rozostření")
    seznam("8. Kontrastní Úprava")
    time.sleep(1)
    print("")
    while True:
      filter_number = input("Číslo filtru: ")
      print("")
      if filter_number == "1":
        sirka, vyska = obrazek.size
        x = 0
        while x < sirka:
            y = 0
            while y < vyska:
                r, g, b = obrazek.getpixel((x,y))
                prumer = int((r+g+b)/3)
                obrazek.putpixel((x,y), (prumer, prumer, prumer))
                y += 1
            x += 1
        display(obrazek)
        break

      elif filter_number == "2":
        sirka, vyska = obrazek.size
        x = 0
        while x < sirka:
            y = 0
            while y < vyska:
                r, g, b = obrazek.getpixel((x,y))
                prumer = int((r+g+b)/3)
                obrazek.putpixel((x,y), (int(0.393 * r + 0.769 * g + 0.189 * b), int(0.349 * r + 0.686 * g + 0.168 * b), int(0.272 * r + 0.534 * g + 0.131 * b)))
                y += 1
            x += 1
        display(obrazek)
        break

      elif filter_number == "3":
        sirka, vyska = obrazek.size
        x = 0
        while x < sirka:
            y = 0
            while y < vyska:
                r, g, b = obrazek.getpixel((x,y))
                prumer = int((r+g+b)/3)
                obrazek.putpixel((x,y), (255 - r, 255 - g, 255 - b))
                y += 1
            x += 1
        display(obrazek)
        break

      elif filter_number == "4":
        sirka, vyska = obrazek.size
        for x in range(sirka):
            for y in range(vyska):
                r, g, b = obrazek.getpixel((x, y))
                new_r = int((r ** 2) / 255)
                new_g = int((g ** 2) / 255)
                new_b = int((b ** 2) / 255)
                obrazek.putpixel((x, y), (min(new_r, 255), min(new_g, 255), min(new_b, 255)))
        display(obrazek)
        break

      elif filter_number == "5":
        enhanced_image = ImageEnhance.Color(obrazek).enhance(1.5)
        obrazek = enhanced_image
        display(obrazek)
        break

      elif filter_number == "6":
        contour_image = obrazek.filter(ImageFilter.CONTOUR)
        obrazek = contour_image
        display(obrazek)
        break

      elif filter_number == "7":
        noisy_image = obrazek.filter(ImageFilter.GaussianBlur(radius=2))
        obrazek = noisy_image
        display(obrazek)
        break

      elif filter_number == "8":
        equalized_image = ImageOps.equalize(obrazek)
        obrazek = equalized_image
        display(obrazek)
        break

      else:
        print("Špatná odpověď.")

    print("")
    loc.clear()
    loc.append("post_uprava")

  if "custom" in loc:
    print("Vlastní filtr funguje na principu přičítání číselných hodnot k RGB pixelů obrázku.")
    time.sleep(0.5)
    print("Změny můžou být minimální nebo obrovské.")
    time.sleep(0.5)
    print("Záleží na velikosti číselných hodnot.")
    time.sleep(0.5)
    print("")
    R = int(input("Hodnota pro přičtění k R: "))
    time.sleep(0.2)
    G = int(input("Hodnota pro přičtění k G: "))
    time.sleep(0.2)
    B = int(input("Hodnota pro přičtění k B: "))
    time.sleep(0.2)
    print("")

    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r + R, g + G, b + B))
            y += 1
        x += 1
    display(obrazek)
    print("")
    loc.clear()
    loc.append("post_uprava")

  if "post_uprava" in loc:
    while True:
      ulozeni = input("Chcete si obrázek uložit? [1 - ano, 2 - ne]: ")
      print("")
      time.sleep(0.5)
      if ulozeni == "1":
        nazev_ulozeneho_obrazku = input("Název uloženého obrázku (i s koncovkou): ")

        # cesta = os.path.join(os.path.dirname(__file__), nazev_ulozeneho_obrazku)
        # obrazek.save(cesta)

        cesta = os.path.join(os.getcwd(), nazev_ulozeneho_obrazku)
        obrazek.save(cesta)
        time.sleep(1)
        print("")
        print("Uloženo!")
        time.sleep(0.5)
        print("")
        loc.clear()
        loc.append("end_ask")
        break
      elif ulozeni == "2":
        loc.clear()
        loc.append("end_ask")
        break
      else:
        print("Špatná odpověď.")

  if "end_ask" in loc:
    while True:
      end_ask = input("Chcete ukončit program? [1 - ano, 2 - ne]: ")
      print("")
      time.sleep(0.5)
      if end_ask == "1":
        loc.clear()
        loc.append("end")
        break
      elif end_ask == "2":
        loc.clear()
        loc.append("post_uprava2")
        break
      else:
          print("Špatná odpověď.")

  if "post_uprava2" in loc:
    while True:
      continue_changes = input("Chcete pokračovat v úpravách s tímto obrázkem? [1 - ano, 2 - ne]: ")
      print("")
      time.sleep(0.5)
      if continue_changes == "1":
        loc.clear()
        loc.append("filter_options")
        break
      elif continue_changes == "2":
        loc.clear()
        loc.append("photo_equip")
        break
      else:
        print("Špatná odpověď.")

  if "end" in loc:
    break
