telefonlar=["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]

sonuc=len(telefonlar)

sonuc=telefonlar[0:-1]

#telefonlar[0]="Samsung S9"
sonuc=telefonlar

""" if "Samsung S6" in telefonlar:
    print("Samsung S6 listenin elemanıdır") """

sonuc=telefonlar[-3]

sonuc=telefonlar[:2]


""" telefonlar[-2:]=["Samsung S9","Samsung S10"]
sonuc=telefonlar
#Listenin son 2 elemanını değiştirdik """


sonuc=telefonlar +["Iphone X","Iphone XR"]


#del telefonlar[-1]
sonuc=telefonlar


sonuc=telefonlar[::-1] #adım sayısı normalde soldan sağa biz sağdan sola yaptık 



'''for x in telefonlar:#x im,n içine elemanlar kopyalanır
    print(x)'''


#print(sonuc)


ogrenciA=["Yiğit","Bilgi",2010,[70,60,70]]
ogrenciB=["Sena","Turan",1999,[80,80,70]]
ogrenciC=["Ahmet","Turan",1998,[80,70,90]]

ogrenciler=[ogrenciA,ogrenciB,ogrenciC]

#print(ogrenciler)



for ogrenci in ogrenciler:
    ad=ogrenci[0]
    soyad=ogrenci[1]
    yaş=2021-ogrenci[2]
    ortalama=round((ogrenci[3][0]+ogrenci[3][1]+ogrenci[3][2]) / 3)
    print(f"{ad} {soyad} {yaş} {ortalama}") 
 
















