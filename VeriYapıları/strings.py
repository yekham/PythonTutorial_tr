""" ad="Yekta"#karakter dizisidir
karakter="a"#string
yas="22"
msj="Benim adım "+ad+" ve yaşım "+yas
karakterSayisi=len(msj)
print(msj[karakterSayisi-1])
print(msj[0:5])
print(msj[0:20:2])#adım sayısı
print(msj[::-1])#sağdan sola 1 er str alır ters yazar
 """


ad="Yekta"
soyad="Pektaş"
yas=22
"""
print("My name is {n} {s}.I'm {y} years old.".format(n=ad,s=soyad,y=yas))
#süslü yerine formatlanmış ad yazılır. """

number=200/700
print("the result is {n:1.2} ".format(n=number))

print(f"my name is {ad} {soyad} and I'm {yas} years old.")
#fstring daha kullanışlı




