#key-value
#34-->İstanbul

plakalar={"kocaeli":41,"istanbul":34}
""" print(plakalar["kocaeli"])
print(plakalar["istanbul"])
 """
plakalar["rize"]=53
plakalar["izmir"]=36
plakalar["izmir"]=35#value güncellenir 

#print(plakalar)

ogrenciler={
            100: {
             "ad":"Çınar",
             "soyad":"Turan",
             "yas":4,
             "notlar":[70,80,70]
            },
            101: {
             "ad":"Yekta",
             "soyad":"Pektaş",
             "yas":22
            }
            }
sonuc=ogrenciler[101]
sonuc=ogrenciler[100]["notlar"][0]

print(sonuc)



urunler={
     '100': {'ad': 'IphoneX', 'fiyat': '200$'}, 
     '101': {'ad': 'IphoneXR', 'fiyat': '220$'}, 
     '102': {'ad': 'IphoneXRS', 'fiyat': '250$'}
        }

""" urunid=input("ID giriniz: ")
urunad=input("Ürün adını giriniz: ")
urunfiyat=input("Ürün fiyatını giriniz: ")

urunler[urunid]={
    "ad":urunad,
    "fiyat":urunfiyat

} #kul. aldığımız id değeri key diğerleri ise yeni bir dictionary oldu

urunid=input("ID giriniz: ")
urunad=input("Ürün adını giriniz: ")
urunfiyat=input("Ürün fiyatını giriniz: ")

urunler[urunid]={
    "ad":urunad,
    "fiyat":urunfiyat
}

urunid=input("ID giriniz: ")
urunad=input("Ürün adını giriniz: ")
urunfiyat=input("Ürün fiyatını giriniz: ")

urunler[urunid]={
    "ad":urunad,
    "fiyat":urunfiyat

} """

id=input("aramak istediğiniz ürün id: ")
urun=urunler[id]
print(f'id:{id} ürün adı {urun["ad"]} ürün fiyatı:{urun["fiyat"]}')