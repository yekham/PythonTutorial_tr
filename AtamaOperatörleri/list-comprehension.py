""" #uzun yöntem
liste=[10,4,7,9,70]
sayilar=[]
for i in liste:
    i*=2
    sayilar.append(i)
print(sayilar)

#Bu yöntem liste oluşturmak için kısa yol sunar
sayilar=[i for i in liste]

sayilar=[i**2 for i in range(1,11,2)]
print(sayilar)

isim="Ahmet"
isimler=["Ahmet","Mehmet","Cengiz","Sadık"]

sonuc=[i.upper() for i in isimler]
sonuc=[str(i) for i in liste]
print(sonuc) """


sayilar=[1,5,8,9,15,44]

sonuc=[i for i in sayilar if i%2==0] 
sonuc=[i if i%2==0 else "tek sayı" for i in sayilar]

fiyatlar=[1000,3000,5000,0,4000]
sonuc=[fiyat*1.18 for fiyat in fiyatlar if fiyat>0]
sonuc=[fiyat*1.18 if fiyat>0 else "vergi hesaplanamadı" for fiyat in fiyatlar]
#iç içe döngü
sonuc=[(x,y)for x in range(3) for y in range(3)]
print(sonuc)