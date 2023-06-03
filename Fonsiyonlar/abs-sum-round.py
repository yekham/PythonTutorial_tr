sayilar=[34,2,4,67,89,12]

sonuc=sum(sayilar)

urunler=[
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000},
    {"title":"iphone 11","price":0},    
]

# toplamfiyat=sum([urun["price"] for urun in urunler])
# sonuc=toplamfiyat/len(urunler)

toplamfiyat=sum([urun["price"] for urun in urunler])
urunAdeti=len([urun for urun in urunler if urun["price"]>0])
sonuc=toplamfiyat/urunAdeti

sonuc=round(10.5)
sonuc=round(1.4242424,2)
sonuc=round(1.4262424,4)


print(sonuc)