def faktoriyel(x):
    x=int(x)

    if (x<0):
        raise ValueError("Negatif değer!")
    sonuc=1
    for i in range(1,x+1):
        sonuc*=i

    return sonuc

for i in [5,7,"a",2,-4,"10a"]:
    try:
        x=faktoriyel(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)



def parolaKontrol(parola):
    turkce_char="şçğüöıİ"

    for i in parola:
        if i in turkce_char:
            raise TypeError("Parola'da tr karakter var")
    print("geçerli parola")
parola=input("parola:")

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)
