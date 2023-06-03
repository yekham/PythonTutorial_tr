#Setler indekslenemez ve sıralanamaz
meyveler={"elma","kiraz","kavun","üzüm"}
sebzeler={"bezelye","soğan"}

sonuc= "elma" in meyveler

meyveler.add("karpuz")

meyveler.update(["vişne","muz","kavun"])

meyveler.remove("karpuz")

meyveler.pop()#her çalıştırmada farklı meyve silinir

#meyveler.clear()

sonuc=meyveler.union(sebzeler)
sonuc=meyveler



#print(sonuc)

