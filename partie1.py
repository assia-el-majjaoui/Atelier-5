
class Vecteur2D:
 def __init__(self,a,b):#  constructeur
    self.x=a
    self.y=b
    print('les deux parametres de vecteurs sont: ')#les parametres de vecteur2D
    print("x=", a)    
    print("y=",b)
v=Vecteur2D(4,8)  
   
class Vecteur2D: 

  def __init__(self): #  constructeur
     self.vx1=1
     self.vy1=3
     self.vx2=6
     self.vy2=8
    
 
  def afficher (self):# la fonction d'affichage de vecteur2D
      
    print('les deux vecteurs sont: ')
    print('les composants de premiere vecteur est : (',self.vx1,',',self.vy1,')')    
    print('les composants de deuxieme vecteur est : (',self.vx2,',',self.vy2,')')    

  def somme (self): # La fonction de la somme de deux vecteurs de class vecteur2D

   print('la somme de ces deux vecteurs est: ')
   self.sommex=self.vx1+self.vx2
   self.sommey=self.vx2+self.vy2
   print('(',self.sommex,',', self.sommey,')')


v=Vecteur2D() 

v.afficher()
v.somme()


class Rectangle: #class rectangle

    def __init__(self):# les composants de ractangle
     
     self.L=5
     self.l=4
     self.nom="rectangle"

    def afficher (self) :# fonction d'affichage
     print('la langeur est :',self.L)
     print('la largeur est :',self.l)
     print('le nom est :',self.nom)
    def surface (self) :# fonction de calculer la surface
     self.sur=self.L * self.L
     print('la surface de rectangle est :',self.sur)
class care(Rectangle): # class care
  
  
    def __init__(self):
     
     self.L=7
     self.l=7
     self.nom="care"
    def surface (self) :
      self.sur=self.L * self.L
      print('la surface de care est :',self.sur)

R=Rectangle()# rappele de class rectangle
R.afficher()
R.surface()
C=care()
C.afficher()
C.surface()
class point:# class point
    def __init__(self ,x=0.0,y=0.0) :
       
        self.ptx=float(x)
        self.pty=float(y)
class segment :# class segment 
    def __init__(self,x1,y1,x2,y2):

        self.org=point(x1,y1)
        self.ex=point(x2,y2)
        print('segment :')
        print (self.org.px,self.org.py,self.ex.px,self.ex.py)

