sayılar=[-1,2,-5,-7,9]
str_sayılar=["1","2","5","7","9"]
isimler=["ali","deniz","mehmet","emel"]
kullanicilar=[
    {"ad":"ali","soyad":"Yılmaz"},
    {"ad":"ahmet","soyad":"Yılmaz"}
]
kareleri=[]

""" for sayi in sayılar:
    kareleri.append(sayi**2)
print(kareleri)

def kareAl(sayi):
    return sayi**2 """
#  MAP(FONKSİYON,LİSTE)  ŞEKLİNDE TANIMLANIR.
# bir fonksiyonu bir dizi üzerinde çalıştırır ve sonuçlarını bir liste olarak döndürür
sonuc=list(map(lambda sayi:sayi**2,sayılar))
sonuc=list(map(int,str_sayılar))
sonuc=list(map(abs,sayılar))
sonuc=list(map(len,isimler))
sonuc=list(map(str.capitalize,isimler))
sonuc=list(map(lambda x:x["ad"],kullanicilar))


print(sonuc)