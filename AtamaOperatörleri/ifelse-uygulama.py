""" isim=input("isminiz: ")
yas=int(input("yaşınız: "))
egitim=input("eğitim durumu: ")

if(yas>=18):
    if(egitim=="lise" or egitim=="üniversite"):
        print("Ehliyet alabilirsiniz.")
    else:
        print("Ehliyet alamazsınız.")
else:
    print("Ehliyet alamazsınız")
 """

""" yazili1=float(input("1.yazılı: "))
yazili2=float(input("2.yazılı: "))
sozlu=float(input("Sözlü: "))

ortalama=(yazili1+yazili2+sozlu)/3

if(ortalama>=0 and ortalama<=24):
    print(f"{ortalama} 0 harf notu")
elif(ortalama>=25 and ortalama<=44):
    print(f"{ortalama} 1 harf notu")
elif(ortalama>=45 and ortalama<=54):
    print(f"{ortalama} 2 harf notu")
elif(ortalama>=55 and ortalama<=69):
    print(f"{ortalama} 3 harf notu")    
elif(ortalama>=70 and ortalama<=84):
    print(f"{ortalama} 4 harf notu")
elif(ortalama>=85 and ortalama<=100):
    print(f"{ortalama} 5 harf notu")      
else:
    print("Yanlış bilgi girdiniz.") """ 


import datetime
tarih=input("aracınız hangi tarihte trafiğe çıktı(2019/7/11): ")
tarih=tarih.split("/") 
print(tarih)

simdi=datetime.datetime.now()
trafikCıkıs=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark=simdi-trafikCıkıs
gun=fark.days
print(gun)
if(gun<=365):
    print("1.servis bakımı.")
elif(gun>365) and(gun<=365*2):
    print("2.servis bakımı.")
elif(gun>=365*2) and (gun<=365*3):
    print("3.servis bakımı.")
else:
    print("Hatalı bilgi giridiniz.")            








