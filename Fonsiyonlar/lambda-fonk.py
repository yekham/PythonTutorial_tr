def multiply(a):
    return a**2
print(multiply(4))

sonuc=(lambda a: a**2)(4)

multiply=lambda a:a**2
sonuc=multiply(5)

toplama =lambda a,b,c:a+b+c
sonuc=toplama(1,4,7)

terscevir=lambda s:s[::-1]
sonuc=terscevir("Yekta")

#fonksiyon geriye fonksiyon döndürüyor(fonk-->lambda)
def myFunc(n):
    return lambda a:a*n
multiply2=myFunc(2)
sonuc=multiply2(20)




print(sonuc)

