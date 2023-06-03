def selamlama():
    for i in range(1,5):   
        print("merhaba")
selamlama()

#----------------------------------------------------------------------------------


def topla():
    a=10
    b=10
    print(a+b)
topla()

#----------------------------------------------------------------------------------


def yıl():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yıl()-2000
sonuc=yasHesapla()
print(sonuc)

#----------------------------------------------------------------------------------



def saat():
    import datetime
    return datetime.datetime.now().hour
def selamla(isim):
    if (saat()<12):
        return "Günaydın "+isim
    else:
        return "Merhaba "+isim
sonuc=selamla("Yekta")
print(sonuc)

#----------------------------------------------------------------------------------



def toplam(a,b):
    return a+b
sonuc=toplam(12,20)
print(sonuc)

#----------------------------------------------------------------------------------



def yasHesapla(dogumyli):
    return 2023-dogumyli
sonuc=yasHesapla(2000)
print(sonuc)
#----------------------------------------------------------------------------------



def emeklilik(dogumyili,isim):
    yas=yasHesapla(dogumyili)
    emeklilik=65-yas
    if emeklilik>0:
        print(f"{isim},emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print(f"{isim},zaten {abs(emeklilik)} yıl önce emekli oldunuz")
emeklilik(2000,"Yekta")
emeklilik(1950,"Ali")


#----------------------------------------------------------------------------------

#DEFAULT PARAMETERS

def selamlama(isim="Kullanıcı",mesaj="iyi günler"):
    print(f"{mesaj} {isim}")
selamlama("Ali","Günaydın")
selamlama("Ali")
selamlama()

def usAlma(taban=3,us=2):
    return taban**us
sonuc=usAlma(2,3)
sonuc=usAlma(2)

#fonksiyonu tanımlarken tanımlanan değerler parametre(parameters)
#fonksiyonu çağırırken verdiğimiz değerlere argüman denir.(arguments)


def toplam(a,b):
    return a+b

def cıkarma(a,b):
    return a-b

def islem(a,b,fn=toplam):
    return fn(a,b)#fonksiyonun referansını verdik

sonuc=islem(b=1,a=3,fn=toplam)#default şeklinde argümanı gönderdik

print(sonuc)

#----------------------------------------------------------------------------------
                                            #Değişken sayıda parametre gönderme
#*args
#dönen değer tuple veri yapısıdır
liste=[10,20,30,40]
def toplama(sayilar):
    sonuc=0
    for i in sayilar:
        sonuc+=i
    return sonuc

def toplamak(*args):
    print(type(args))
    print(args)
    sonuc=0
    for i in args:
        sonuc+=i
    return sonuc
print(toplamak(10,20,39,50,60))


#**kwargs
#dönen değer dictionary veri yapısıdır.


def displayUser(**kwargs):
    for key,value in kwargs.items() :
        print(f"{key}: {value}")
    print("\n")
    
displayUser(username="sadık turan")
displayUser(username="yekta hamit",email="yektahamit@gmail.com")

def myfunction(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)#tuple
    print(kwargs)#dictionary

myfunction(10,20,30,40,50,60,key1="value1",key2="value2")

