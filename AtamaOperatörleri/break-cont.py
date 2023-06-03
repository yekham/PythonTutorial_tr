#continue o anki turu iptal eder
#break döngüden çıkar
name="Yekta Pektaş"
for harf in name:
    if(harf=="Y"):
        break
    print(harf)



i=0
while(i<5):
    if (i==3):
        break
    print(i)
    i+=1
print("döngü bitti")


i=-1
toplam=0
while(i<=100):
    i+=1
    if(i%2==1):
        continue
    toplam+=i
   
print(f"toplam:{toplam}")