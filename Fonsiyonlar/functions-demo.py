""" #alan çevre hesabı
def alan(kısa,uzun):
    return kısa*uzun
def cevre(kısa,uzun):
    return (2*kısa)+(2*uzun)

sonuc=alan(5,4)
sonuc=cevre(5,4)
print(sonuc) """



""" #kelime tekrar
def kelimetekrar(kelime,tekrar):
    while tekrar>0:
        tekrar-=1
        print(kelime)

kelime=input("girmek istediğiniz kelime nedir:")
tekrar=int(input("kaç kere tekrarlamak istersiniz:"))

sonuc1=kelimetekrar(kelime,tekrar)
print(sonuc1) """



""" #asal sayı bulma
def asalBulma(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if (sayi>1):
            for i in range(2,sayi):
                if (sayi%i==0):
                    break
            else:
                print(sayi) 


say1=int(input("1.sayı: "))
say2=int(input("2.sayı: "))

asalBulma(say1,say2) """



""" #Tam bölen bulma
def tambolen(sayi):
    listtam=[]    
    for i in range(1,sayi+1):
        if sayi%i==0:
            listtam.append(i)
    return listtam 


print(tambolen(20)) """


""" #yazı-tura
def yazıTura():
    import random
    sayi=random.randint(1,11)
    if sayi>5:
        return "Tura"
    else:
        return "Yazı"
print(yazıTura()) """


