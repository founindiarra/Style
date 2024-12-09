"""class Nombrep:
    def __init__(self,):
        pass

    @staticmethod

    def myStaticMethod():
        for nombre in range (1,101) :
            print(nombre)

Nombrep.myStaticMethod()
"""


"""class deuxnombre:
    def __init__(self,chaine1,chaine2):
        self.chaine1 = chaine1
        self.chaine2 = chaine2


    def myclass(self):
        if self.chaine1 == self.chaine2 :
            print("juste")
        else :
            print("erreur")

s1 = input("entrer chaine1")
s2 = input("entrer chaine2")

afficher = deuxnombre(s1,s2)
afficher.myclass()"""



class Etudiant:
    def __init__(self,nom,note1,note2):
        self.nom = nom
        self.note1 = note1
        self.note2 = note2

    def calculmoyenne(self):
        self.moyenne = (self.note1 + self.note2) / 2
        print("je suis", self.nom, "j'ai", self.moyenne, "de moyenne")

n = input("entrer votre nom")
n1 = int(input("entrer note1"))
n2 = int(input("entrer note2"))

afficher = Etudiant(n,n1,n2)
afficher.calculmoyenne()




            





