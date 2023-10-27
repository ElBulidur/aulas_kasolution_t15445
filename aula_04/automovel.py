class Automovel:
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, p_marca: str):
        if len(p_marca) == 0:
            raise ValueError('A marca foi fornecida incorretamente')
        self.__marca = p_marca
    
    
class Automovel2:
    def __init__(self):
        self.marca = 'julio'


auto1 = Automovel() # obj, 

auto2 = Automovel2() # obj, atrib

auto1.marca = 'ford'  # obj, atr

print(auto1.marca)

