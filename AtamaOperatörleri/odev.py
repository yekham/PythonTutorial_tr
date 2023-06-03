import random
num2=random.randint(50,99)
while True:
    try:
        num = int(input("Lütfen bir tamsayı girin (0 girerek çıkabilirsiniz): "))
        if (num%1==0):
            break
        if num == 0:
            break
        else:
            continue
        
    except ValueError:
        print("Lütfen tamsayı girin!")

print("Klavyeden girilen 1. sayı {}, rastgele seçilen 2.sayı {}".format(num,num2))
