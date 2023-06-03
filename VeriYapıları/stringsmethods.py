msg="Python Kursumuza Hoş Geldiniz.Ben Yekta Hamit Pektaş."

#sonuc=msg.upper()#hepsi büyük
#sonuc=msg.lower()#hepsi küçük
#sonuc=msg.title()#ilk harfler büyük
#sonuc=msg.capitalize()#ilk büyük sonra küçük
#sonuc=msg.islower()#is ile başlayanlar soru sorar T,F
#sonuc="abc".islower()#is ile başlayanlar soru sorar T,F
#sonuc=msg.split()#boşluklara göre dizi oluşturur.
#sonuc="-".join(sonuc)#eleman birleştirir.
#sonuc=msg.split(".")#noktalara göre dizi oluşturur.
#sonuc=msg.index("Hoş")#str içinde arama
#sonuc=msg.startswith("P")#P ile mi başlıyo T,F
#sonuc=msg.endswith(".")#. ile mi bitiyo T,F
#sonuc=msg.replace("Yekta","Osman")#yer değiştirme
sonuc=msg.lower().replace(" ","-").replace("ş","P")#yer değiştirme


print(sonuc)