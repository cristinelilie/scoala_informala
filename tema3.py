

class Fractie():
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def set_numarator(self,numarator):
        self.numarator = numarator

    def set_numitor(self, numitor):
        self.numitor = numitor

    def __str__(self):
        return f"{self.get_numarator()}/{self.get_numitor()}"

    def cmmdc(self,a,b):
        a=abs(a)
        b=abs(b)
        while a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
        return a

    def __add__(self, other):
        numarator_nou = self.numarator*other.numitor + self.numitor*other.numarator
        numitor_nou = self.numitor*other.numitor
        numitor_nou_simplificat = numitor_nou //self.cmmdc(numitor_nou, numarator_nou)
        numarator_nou_simplificat =numarator_nou // self.cmmdc(numitor_nou,numarator_nou)
        return Fractie(numarator_nou_simplificat, numitor_nou_simplificat)

    def __sub__(self, other):
        numarator_nou = self.numarator * other.numitor - self.numitor * other.numarator
        numitor_nou = self.numitor * other.numitor
        numitor_nou_simplificat = numitor_nou // self.cmmdc(numitor_nou, numarator_nou)
        numarator_nou_simplificat = numarator_nou // self.cmmdc(numitor_nou, numarator_nou)
        return Fractie(numarator_nou_simplificat, numitor_nou_simplificat)

    def inverse(self):
        return Fractie(self.numitor,self.numarator)


f1=Fractie(2,3)
f2=Fractie(4, 2)
print(f1+f2)
print(f1-f2)
print(f1.inverse())