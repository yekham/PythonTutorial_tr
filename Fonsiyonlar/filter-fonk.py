#Liste üzerinde filtreleme yapar ve True değer döndürür
yaslar=[5,12,18,24,44]
def yetiskinmi(x):
    if x<18:
        return False
    else:
        return True
for i in filter(yetiskinmi,yaslar):
    print(i)
sonuc=list(filter(yetiskinmi,yaslar))
sonuc=list(filter(lambda x:x>=18,yaslar))

sayilar=[0,1,25,6,8,9]
sonuc=list(filter(lambda x:x%2!=0,sayilar))
isimler=["çınar","yiğit","sena","ada","ali"]
sonuc=list(filter(lambda x:x[0]=='a',isimler))
#map fonks. listeyi dolaşıp gelen her elemana göre filter 
#kullanıp ilk elemanı a olanları filtreledik.
filtered_result=filter(lambda x:x[0]=='a',isimler)
sonuc=list(map(lambda x:x.upper(),filtered_result))

users=[
    {"username":"sadikturan","tweets":["tweet1","tweet2"]},
    {"username":"çınarturan","tweets":[]},
    {"username":"sedaturan","tweets":["tweet1"]}

    ]
sonuc=list(filter(lambda u:len(u["tweets"])>0,users))
#tweeti olan kullanıcıların usernamelerini liste halinde büyük yazdır
filtered=list(filter(lambda u:len(u["tweets"])>0,users))
sonuc=list(map(lambda u:u["username"].upper(),filtered))



print(sonuc)

