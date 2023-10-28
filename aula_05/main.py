
class Automovel:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def getLinha(self):
        linha = f"{self.marca} {self.modelo} {self.ano}"
        return linha

class Onibus(Automovel):
    def __init__(self, marca, modelo, ano, assentos):
        super().__init__(marca, modelo, ano)
        self.assentos = assentos
    
    @property
    def assentos(self):
        return self.__assentos 
    
    @assentos.setter
    def assentos(self, p_assentos: int):
        self.__assentos = p_assentos
        
    def getLinha(self):
        linha = super().getLinha() + f' {self.assentos}'
        return linha

# auto = Automovel('ford', 'b', 2019)   

onibus = Onibus('ford', 'b', 2019, 90)

onibus.assentos = 20

print(onibus.getLinha())
