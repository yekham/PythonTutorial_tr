sayilar=[1,53,45,67,97,5,7]
sonuc=sorted(sayilar,reverse=True)
sonuc=sorted((1,53,45,67,97,5,7))


users=[
    {"username":"sadikturan","tweets":["tweet1","tweet2"],"email":"info@gmail.com"},
    {"username":"çınarturan","tweets":[]},
    {"username":"sedaturan","tweets":["tweet1"],"name":"","phone":"123123123"}

    ]
sonuc=sorted(users,key=len,reverse=True)
sonuc=sorted(users,key=lambda u:u["username"])
sonuc=sorted(users,key=lambda u:len(u["tweets"]))

kurslar=[
    {"title":"python kursu","students":25000},
    {"title":"web geliştirme kursu","students":35000},
    {"title":"javascript kursu","students":5000}
]
kurs=sorted(kurslar,key=lambda kurs:kurs["students"],reverse=True)
#en popüler kursların adları:
#
sonuc=list(map(lambda kurs:kurs["title"],kurs))


print(sonuc)