_list=[1,2,3]
_tuple=(1,2,3)

print(_tuple[1])
print(len(_tuple))
print(_tuple.count(1))
print(_tuple.index(3))

#Tuple değiştirilemezdir 


#List veri yapısını Tuple fonk. ile Tuple'a
#dönüştürdük
dönüşüm=tuple(_list)
print(type(dönüşüm))

