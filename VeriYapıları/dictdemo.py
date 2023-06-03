players={}
sayac=0
while sayac<2:
    id=input("oyuncu id: ")
    name=input("oyuncu adı: ")
    nationality=input("ülke: ")
    yearOfBirth=input("doğum yılı: ")
    current_team=input("takım: ")
    history=input("oynadığı yerler: ")
    players.update({
    id:{
        "name":name,
        "yearOfBirth":yearOfBirth,
        "nationality":nationality,
        "yearOfBirth":yearOfBirth,
        "current_team":current_team,
        "history":history.split(",")#split ederek liste oluşturduk

    }
                        })
    sayac=sayac+1

print(players)