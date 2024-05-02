class Passaro:
    def Voar(self):
        print("Voando")

class Pardal(Passaro):
    def Voar(self):
        super().Voar()
    
class Avestruz(Passaro):
    def Voar(self):
        print("Avestruz não pode voar")

class Aviao(Passaro):
    def Voar(self):
        print("Avião está decolando")

def plano_de_voo(obj):
    obj.Voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(p3)