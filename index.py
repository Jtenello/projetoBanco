# Cabeçalho Itaú Unibanco
print("=" * 40)
print("       🏦 BEM-VINDO AO ITAÚ UNIBANCO       ")
print("=" * 40)

class ContaBancaria:
    def __init__(self, titular, cpf, saldo=0, limite=500, limite_saques=3):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R$ {valor:.2f}")
            print("\n✅ Depósito realizado com sucesso!")
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n❌ Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite:
            print("\n❌ Operação falhou! O valor do saque excede o limite.")
        elif self.numero_saques >= self.limite_saques:
            print("\n❌ Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            self.numero_saques += 1
            print("\n✅ Saque realizado com sucesso!")
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")

    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"\n💰 Saldo atual: R$ {self.saldo:.2f}")
        print("==========================================")

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("\n❌ Digite um valor positivo.")
        except ValueError:
            print("\n❌ Erro! Digite um valor numérico válido.")

# Criando a conta
print("\n📌 Vamos criar sua conta bancária.\n")
titular = input("Digite seu nome: ")
cpf = input("Digite seu CPF (somente números): ")
conta = ContaBancaria(titular, cpf)

# Menu Principal
menu = """
🔹 [d] Depositar
🔹 [s] Sacar
🔹 [e] Extrato
🔹 [q] Sair

=> """

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = obter_valor("\nInforme o valor do depósito: ")
        conta.depositar(valor)

    elif opcao == "s":
        valor = obter_valor("\nInforme o valor do saque: ")
        conta.sacar(valor)

    elif opcao == "e":
        conta.mostrar_extrato()

    elif opcao == "q":
        print("\n✅ Obrigado por usar o Itaú Unibanco! 👋")
        break

    else:
        print("\n❌ Operação inválida! Escolha uma opção válida.")
