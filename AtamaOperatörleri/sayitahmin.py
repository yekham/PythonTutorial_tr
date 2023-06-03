import random

randomsayi=random.randint(1,10)
hak=int(input("hak sayısını giriniz: "))
sayac=0
while(hak>0):
    hak-=1
    sayac+=1
    tahminsayi=int(input("sayı tahmin ediniz:"))
    if(tahminsayi==randomsayi):
        print("Tebrikler {}. defada sayıyı bildiniz.".format(sayac))
        break
    elif(tahminsayi<randomsayi):
        print("Yukarı.")
    else:
        print("aşşağı")
    if (hak==0):
        print("Hakkınız bitti tekrar deneyin. Sayı:{}".format(randomsayi))
        break