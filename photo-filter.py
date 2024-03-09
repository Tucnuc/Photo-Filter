from PIL import Image
obrazek = Image.open("kitten.jpg")
sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        obrazek.putpixel((x,y), (r, r, r))  # Doplňujte zde
        y += 1
    x += 1
display(obrazek)


# Před udělané filtry:

# r+g+b-250 , r+g+b-250, r+g+b-250 - Černo bílá
# r, r, r - Šedá
# r+250, g, b+150 - Růžová
# r+g+b -182, r+g+b -154, r+g+b -141 - Světle modrá