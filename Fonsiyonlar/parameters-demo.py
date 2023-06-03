#Büyük sayı bulma
def buyukbulma(sayi1,sayi2):
    if(sayi1>sayi2):
        return f"Büyük sayı:{sayi1}"
    else:
        return f"Büyük sayı:{sayi2}"
    
sonuc=buyukbulma(10,20)



#string karakter sayısı bulma
def karakterSayisinibul(string):
    return{letter: string.count(letter) for letter in string}
sonuc=karakterSayisinibul("flutter")


#Liste güncelleme
def list_operation(liste,command,position,value=None):
    if (command=="add") and (position=="end"):
        liste.append(value)
        return liste
    elif (command=="add")and(position=="beginning"):
        liste.insert(0,value)
        return liste
    elif (command=="remove")and(position=="end"):
        return liste.pop()
    elif (command=="remove")and(position=="beginning"):
        liste.pop(0)
        return liste

sonuc=list_operation([1,2,3],"add","beginning",4)
sonuc=list_operation([1,2,3],"remove","beginning")



def contains_blue(*args):
    if "blue" in args:
        return True
    else :
        return False
sonuc=contains_blue("red","blue","yellow")


print(sonuc)
        