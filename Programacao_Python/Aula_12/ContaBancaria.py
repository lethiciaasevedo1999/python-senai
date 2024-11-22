class contaBancaria:
    def __init__(self,saldoInicial ):
        self.saldo = saldoInicial
        
    def depositar(self,valor):
        self.saldo = self.saldo + valor
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente.")
            
    def exibirSaldo(self):
        print(f"Saldo atual: {self.saldo}")


valorInicial = float(input("Deposite o valor inicial da conta: "))        
contaFisica = contaBancaria(valorInicial)        
deposito = float(input("Digite o valor do depósito: "))
contaFisica.depositar(deposito)
contaFisica.exibirSaldo()
saque = float(input("Digite o valor do saque: "))
contaFisica.sacar(saque)
contaFisica.exibirSaldo()

      
        
        