opelObj={
    "marka":"Opel",
    "model":"Corsa",
    "yil":2020
}

sonuc=opelObj.get("marka")

""" for x in opelObj:
    print(x)

for x in opelObj:
    print(opelObj[x]) """

#value'ya erişim
for x in opelObj.values():
    print(x)

#key-value erişilebilir
for x,y in opelObj.items():
    print(x,y)

sonuc="marka" in opelObj

sonuc=len(opelObj)

#yeni eleman ekleme
opelObj["renk"]="kırmızı"

#eleman silme
opelObj.pop("renk")

print(opelObj)



print(sonuc)
#obj=opelObj#kopyalama işlemi referans olarak yapıldı
# ikiside aynı adresi tutar 

obj=opelObj.copy()#kopyalama işlemi yapıldı 
#belleğin ayrı yerlerinde farklı bir kopyası çıkar
obj["marka"]="Mazda"

opelObj.update({
    "marka":"bmw",
    "renk":"kırmızı"
})
print(obj)
print(opelObj)


