def menu ():
    menu    =   """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Novo usuario
    [0] Sair
    Insira a operacao: """
    return input(menu)

def depositar (saldo, deposito, extrato, /):
    if deposito >0:
            saldo += deposito
            print   (f"Valor depositado = R${deposito:.2f}\n")
            extrato += f"Deposito: R${deposito:.2f}\n"
    else:
        print   ("Valor invalido")

def sacar (*, saldo, saque, extrato, limite, n_saques, limite_saques):
    if saldo <= 0:
            print   ("Saldo insuficiente")
    else:          
        saldo_insuficiente = saque > saldo
        limite_insuficiente = saque > limite
        n_saques_insuficientes = n_saques >= limite_saques
        if saldo_insuficiente:
            print("Saldo insuficiente")
        elif limite_insuficiente:
            print("Limite insuficiente")
        elif n_saques_insuficientes:
            print("Limite de saques exedido")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            n_saques += 1
        else:
            print("Operacao invalida")

def extrato (saldo,/, *, extrato):
    extrato =  """ 
    EXTRATO

    """
    return print(extrato)

def criar_usuario (usario):
    return
def filtrar_usuario (cpf, usuario):
    return


def main ():
    LIMITE_SAQUES = 0
    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0
    usuarios = []
    contas = []
    
    while True:
        controle = menu()
        
        if controle == "1":
            deposito = float(input("Insira o Valor a ser depositado: "))
            
            depositar(saldo, deposito, extrato)
        elif controle == "2":
            saque = float(input("Insira o Valor a ser saquado: "))
            
            sacar(saldo = saldo, saque = saque,limite = limite, n_saques = n_saques,
                  limite_saques = LIMITE_SAQUES )
        elif controle == "3":
            print(extrato)
        elif controle == "4":
            criar_usuario(usuarios)
        
        elif controle == "0":
            break

main()