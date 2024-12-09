d = {

    "nom" : "diarra",
    "prenom" : "foune",
    "age" : 20

}

p = {

    "" : "koumasssi",
    "filiere" : "informatique",
    "ville" : "abidjan"

}
d.update(p)
print(d)



a = {
    "mali" : "bamako",
    "cote d'ivoire" : "abidjan",
    "burkina" : "ouagadougou"
}
for i in a :
    print("la capitale de", a.keys(), "est", a.values() )

 