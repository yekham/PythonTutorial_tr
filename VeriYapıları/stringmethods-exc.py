website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
#sonuc=" Hello World ".strip()

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
#sonuc='www.sadikturan.com'.strip("w.com")

# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
#sonuc=kursAdi.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
#sonuc=website.count("a")

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
#sonuc=website.startswith("www")
#sonuc=website.endswith("com")


# 6- 'website' içinde '.com' ifadesi var mı?

#sonuc = website.index('.com')

# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
#sonuc=kursAdi.isalpha()
#sonuc=kursAdi.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
#sonuc="Contents".center(50,"*")

# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
#sonuc=kursAdi.replace(" ","-")

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
#sonuc="Hello World"
#sonuc=sonuc.replace("World","There") 

# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
sonuc=kursAdi.split(" ")

print(sonuc)