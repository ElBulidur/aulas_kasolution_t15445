
# ABSTRACAO, OBJETO, ATRIBUTOS, METHODOS

#classe (Abstracao)
class Carro:
    def __init__(self, cor, modelo, fabricante):
        self.cor = cor
        self.modelo = modelo
        self.fabricante = fabricante
        
    def imprimir_tudo(self):
        print(f"Carro: {self.modelo}, fabricante: {self.fabricante}, Cor: {self.cor}")
        
    def retorn_string_tudo(self):
        return f"Carro: {self.modelo}, fabricante: {self.fabricante}, Cor: {self.cor}"

# Objeto
carro_red = Carro("Red", 'Mustang', 'Ford')
carro_blue = Carro("Blue", 'Prius', 'Toyota')
carro_gree = Carro("Green", 'Golf', 'Volkswagen')

# Atributo

# print(Carro)
# print(carro_red)
print(carro_red.cor)
print(carro_red.modelo)
print(carro_red.fabricante)
print("=====")
carro_red.imprimir_tudo()
print("=====")

print(carro_red.retorn_string_tudo())