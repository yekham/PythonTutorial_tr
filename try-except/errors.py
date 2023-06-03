""" try:
    x=int(input("x:"))
    y=int(input("y:"))
    print(x+y)
except:
    print("Hata oluştu!!") """

                              #SyntaxError=>yazım yanlışı
#ksjdfkjs;;
#def yazdir(():
#print("merhab"a)

                            #NameError=>tanımlanmamış bir değişken kullanımı
#print(ad)

                            #TypeError=>Hatalı parametre kullanımı
#len(5)
#4+"a"

                            #IndexError=>yanlış index numarası
#liste=["merhaba"]
#liste[1]

                            #ValueError=>hatalı tip kullanımı
#int("10z")

                            #KeyError=>key hatası 
#d={}
#d["ad"]

                            #AttributeError=>Olmayan bir özelliğe ulaşmak istediğimizde
#"merhaba".upper()
#"merhaba".append()
while True:
    try:
        x=int(input("x:"))
        y=int(input("y:"))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:#Hatayı logladık
        print("hata oluştu")
        print(e)
    except Exception as e :
        print("Bilinmeyen bir hata oluştu")
        print(e)
    else:
        break
    finally:#hata olsun olmasın her türlü çalışır
        print("finally bloğu çalıştı")