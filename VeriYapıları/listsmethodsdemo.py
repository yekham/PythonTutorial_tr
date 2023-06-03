isimler=["Ada","Yiğit","Hasan","Beril"]
yaslar=[1998,2000,1998,1987]

isimler.append("Cenk")

isimler.insert(0,"Sena")

#isimler.remove("Yiğit")

print(isimler.index("Yiğit"))

#BEril var mı
print(isimler.__contains__("Beril"))
sonuc= "Beril" in isimler
print(sonuc)

isimler.reverse()
yaslar.reverse()

isimler.sort()
yaslar.sort()


print(isimler)
print(yaslar)

str="Iphone X,Iphone XR"
sonuc=str.split(",")
print(sonuc[0])


#Kullanıcıdan aldığım 3 markka bilgisini listede sakla
markalar=[]


marka=input("Marka: ")
markalar.append(marka)

marka=input("Marka: ")
markalar.append(marka)

marka=input("Marka: ")
markalar.append(marka)

print(markalar)

