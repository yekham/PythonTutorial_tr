sayilar=[1,5,8,9,3,45]
harfler=["a","b","e","s","a","y"]

sonuc=min(sayilar)
#ekleme
sayilar.append(10)#liste sonuna ekler
sayilar.insert(len(sayilar),50) #konuma ekler yana kaydırır
#silme
sayilar.pop()#eleman siler
sayilar.remove(45)
#sıralama
sonuc=sayilar.sort()

print(sonuc)

print(harfler.count("a"))

print(harfler.index("b"))





