
class etudiant:
    def __init__(self): # constructeur  
       
        self.nom1="ASSIA"
        self.prenom1="mej"
        self.age1=20
        self.cne1="KB1234"
        self.note1=18
        self.nom2="Douae"
        self.prenom2="Has"
        self.age2=23
        self.cne2="kb567"
        self.note2=15
        list=[self.nom1,self.prenom1,self.age1,self.cne1,self.note1,self.nom2,self.prenom2,self.age2,self.cne2,self.note2]
        print(list)
        print('ordrer la liste selon age') #  la liste ordonner selon l'age
        if(list[2]>list[7]):
            list=[self.nom1,self.prenom1,self.age1,self.cne1,self.note1,self.nom2,self.prenom2,self.age2,self.cne2,self.note2]
            print(list)
        else:
            list=[self.nom2,self.prenom2,self.age2,self.cne2,self.note2,self.nom1,self.prenom1,self.age1,self.cne1,self.note1]
            print(list)
            print('ordrer la liste selon moyenne')# la liste ordonner selon moyenne
        if(list[4]>list[9]):
            list=[self.nom1,self.prenom1,self.age1,self.cne1,self.note1,self.nom2,self.prenom2,self.age2,self.cne2,self.note2]
            print(list)
        else:
            list=[self.nom2,self.prenom2,self.age2,self.cne2,self.note2,self.nom1,self.prenom1,self.age1,self.cne1,self.note1]
            print(list)

e=etudiant() # rappelle de constructeur



