""" sayilar=[1,5,15,35,57,72,75,10]

for x in sayilar:
    print(x)


for x in sayilar:
    if(x%5==0):
        print(x)

toplam=0
for x in sayilar:
     toplam=toplam+x
print(toplam)


for x in sayilar:
    if(x%2==0):
        x**=2
        print(x)

        

urunler=["iphone 8","iphone X","iphone XR","samsung S10"]

for x in urunler:
    print(x[1])    


#liste içinde iphone geçen kaç ürün var        
count=0
for urun in urunler:
    index=urun.find("iphone")
    if(index>-1):
        count+=1
print(count) """

urunler = [
    {'name':'iphone 8','price':'4000'},
    {'name':'iphone 8 Plus','price':'5000'},
    {'name':'iphone X','price':'6000'},
    {'name':'iphone XR','price':'7000'},
    {'name':'iphone 11','price':'8000'},
    {'name':'samsung s10','price':'6000'},
 ]
toplam=0
for x in urunler:
    toplam=int(x["price"])+toplam
print(toplam)


sayi=1
for x in urunler:
    if(int(x['price'])>=6000):
        print(f"{sayi}. ürün:"+x['name']+" fiyatı="+x['price'])
        sayi+=1


kelime=input("aramak istediğiniz ürün:")

for urun in urunler:
    if(urun['name'].find(kelime.lower())>-1):
        print(urun['name'])

    