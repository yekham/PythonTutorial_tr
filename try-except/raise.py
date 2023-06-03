""" x=10
if x>5:
    raise ValueError("X 5'ten büyük olamaz") """
#raise ile hata objesi fırlatması yapılır obje içine mesaj da yazılabilir.
def colorize(text,color):
    colors=("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdır.")
    if type(color) is not str:
        raise TypeError("renk str tipinde olmalıdır.")
    if color not in colors:
        raise ValueError("geçersiz bir renk ismi")

    print(f"{text} {color} renk olarak yazdırıldı")
try:
    colorize("merhaba","red")
    colorize("selam","purple")
    colorize("selam","yellow")
except Exception as ex:
    print(ex)



