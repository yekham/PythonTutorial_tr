""" sayi=int(input("sayi giriniz: "))

if sayi>50 and sayi<100:
    print(f"{sayi} sayısı 50-100 arasında.")
else:
    print(f"{sayi} sayısı 50-100 arasında değil.")  """ 


""" sayi=int(input("sayi giriniz: "))

if sayi%2!=0 and sayi>0:
    print(f"{sayi} sayısı pozitif tek sayıdır.")
else:
    print(f"{sayi} sayısı pozitif tek değil.")   """  



""" ad=input("adınızı giriniz: ")
kilo=float(input("kilonuzu giriniz: "))
boy=float(input("boyunuzu giriniz: "))

indeks=kilo/(boy**2)

if indeks<=18.4 and indeks>=0:
    print(f"{indeks} zayıfsınız.")
elif indeks>=18.5 and indeks<=24.9:
    print(f"{indeks} normalsiniz.")
elif indeks>=25.0 and indeks<=29.9:
    print(f"{indeks} fazla kilolusunuz.")
elif indeks>=30.0 and indeks<=34.9:
    print(f"{indeks} şişmansınız.")
else:
    print("Lütfen sayı giriniz.")   """  


""" x=y=[1,2,3]
z=[1,2,3]

print(x==y)
print(x==z)
print(x is y)#aynı adrese sahipler True
print(x is z)#farklı adres false """

x=[1,2,3]
y=[2,4]

del x[2]
y[1]=1
y.reverse()

print(x==y)#elemanlar aynı
print(x is y)#aynı adreste değiiler farklı objeler

print(x is not y)

x=["apple","banana"]
print("banana"in x)
name="Çınar"
print("a"in name)






