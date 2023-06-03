liste=["1","2","5a","10b","abc","10","50"]

""" for i in liste:
    try:
        sonuc=int(i)
        print(sonuc)
    except ValueError:
        continue """





""" while True:
    sayi=input("sayı: ")
    if (sayi=="q"):
        break
    try:
        sonuc=float(sayi)
        print(f"girilen sayı: {sonuc}")
        break
    except ValueError:
        print("geçersiz sayi")
        continue """



urun={"urunAdi":"samsung s10"}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(urun,"fiyat"))
print(get(urun,"urunAdi"))



