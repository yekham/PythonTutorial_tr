""" for x in range(1,11):
    print("************************")
    for k in range(1,11):
        print("{}x{}={}".format(x,k,x*k)) """


asalmi=True
sayi=int(input("lütfen sayı giriniz: "))

if (sayi==1):
    asalmi=False
for i in range(2,sayi):
    if(sayi%i==0):
        asalmi=False
        break
if asalmi:
    print("sayı asaldır.")
else:
    print("sayı asal değil.")


