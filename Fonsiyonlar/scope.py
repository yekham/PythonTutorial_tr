#global scope
x="global x"

def function():
    #local scope
    x="local x"
    print(x)
function()
print(x)
#########################################
#global
name="Çınar"

def changeName(new_name):
    #local
    name=new_name
    print(name)
changeName("Ada")
print(name)
print("#########################################")

name="global string"
def greeting():
    #name="Çınar"
    
    def hello():
       # name="ada"
        print("hello "+name)
    hello()
greeting()
#########################################
#GLOBAL KEYWORD
#Global keyword'ü fonksiyon içinde tanımlanan değişkenin global olmasını sağlar
#böylelikle fonksiyon dışındaki atadığımız değeri fonksiyon kullanımından sonra değiştirebiliriz.
x=50
def test():
    global x 
    print(f"x: {x}")
    x=100
    print(f"changed x to: {x}")   
test()     
print(x)   
