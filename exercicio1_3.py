class Conta_Corrente:
    def __init__(self, num, saldo, owner):
        self.num = num
        self.saldo = saldo
        self.owner = owner

conta1 = Conta_Corrente(1234, 500000, "Álvaro")
conta2 = Conta_Corrente(4321, 400, "Roberto")

print(f"A conta de {conta1.owner} tem o numero {conta1.num} com o saldo de {conta1.saldo} R$")

print(f"A conta de {conta2.owner} tem o numero {conta2.num} com o saldo de {conta2.saldo} R$")