class Calc:
    def somar(self, a, b):
        print(f"A soma e: {a+b}")
        
    def subatracao(self, a, b):
        print(f"A subtracao e: {a-b}")
        
    def multiplicar(self, a, b):
        print(f"A multiplicacao e: {a*b}")
        
    def dividir(self, a, b):
        print(f"A divisao e: {a/b}")
        
    def executar_caculadora(self):
        print("====== calculador do julio ==========")
        print("Bem vindo a minha calculadora, escolha uma das opcoes abaixo:")
        print("")


        print("A = SOMA")
        print("B = SUBTRACAO")
        print("C = MULTIPLICACAO")
        print("D = DIVISAO")
        
        a = int(input("Numero 01: "))
        b = int(input("Numero 02: "))

        opcao = input("Escolha a opcao desejada: ").lower()
        print("")

        if opcao == 'a':
            escolha = 'Soma'
            resultado = self.somar(a, b)
        elif opcao =='b':
            escolha = 'Subtracao'
            resultado = self.subatracao(a, b)
        elif opcao == 'c':
            escolha = 'Multiplicacao'
            resultado = self.multiplicar(a, b)
        elif opcao == 'd':
            escolha = 'Divisao'
            resultado = self.dividir(a, b)
        else:
            print("Escolha errada!!!")
            print("saindo...")
        
# calculadora = Calc()

# calculadora.executar_caculadora()