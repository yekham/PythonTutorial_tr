markalar=["opel","bmw","mercedes"]

#enumerate


index=0
for x in markalar:
    print(f"{index+1}-{markalar[index]}")
    index+=1

#enumerate fonksiyon her ögenin index numarasıyla dönmesini sağlar.

obj1=enumerate(markalar)

print(list(obj1))

for (indexno,value) in enumerate(markalar,10):
    print(f"{indexno}-{value}")
#zip


""" #farklı tuple yada listeleri birleştirmeye.
#for döngüsü de elemanları ayrıştırmak için kullanıllır.
liste1=[1,2,3,4,5]
liste2=["a","b","c","d","e","f"]
liste3=[100,200,300,400,500]
print(list(zip(liste1,liste2,liste3)))

for item in zip(liste1,liste2):
    print(item)

for a,b,c in zip(liste1,liste2,liste3):
    print(a,b,c) """