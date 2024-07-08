import textwrap


def menu ():
    menu    =   """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuario
    [5] Nova conta
    [6] Contas
    [0] Sair
    Insira a operacao: """
    return input(menu)

def depositar (saldo, deposito, extrato, /):
    if deposito >0:
            saldo += deposito
            print   (f"Valor depositado = R${deposito:.2f}\n")
            extrato += f"Deposito: R${deposito:.2f}\n"
            return saldo, extrato
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
        
        return saldo, extrato

def imprimir_extrato (saldo,/, *, extrato):
    return print(extrato + f"Saldo: R${saldo:.2f}")

def criar_usuario (usuarios):
    cpf = input("Insira o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print  ("Usuario já existente\n")
        return
    else:
        print   ("_________Novo cadastro_________\n")
        nome = input("Insira o nome do Usuario: ")
        data_nasc = input("Insira a data de nascimento: ")
        endereco = input("Insira o endereço (RUA, Numero - BAIRRO - CIDADE/ESTADO): ")
        usuarios.append({"nome": nome, "data de nascimento": data_nasc,"cpf": cpf, "endereco": endereco})
        print ("Usuario Cadastrado\n")
                
def filtrar_usuario (cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta (agencia, n_conta, usuarios):
    cpf = input("Insira o cpf a ser consultado: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print   ("\nConta Criada")
        return {"agencia": agencia, "n_conta": n_conta, "usuario": usuario}
    else:
        print("\nUsuario não encontrado\n")

def listar_contas (contas):
    for conta in contas:
        linha = f"""\ 
        Agencia :\t {conta['agencia']}
        C/C:\t\t{conta['n_conta']}
        Titular:\t{conta['usuario']['nome']}
    """
    print ("=" * 100)
    print (textwrap.dedent(linha))
    
     
def main ():
    LIMITE_SAQUES = 3
    ANGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = """_________EXTRATO_________\n"""
    n_saques = 0
    usuarios = []
    contas = []
    
    while True:
        controle = menu()
        
        if controle == "1":
            deposito = float(input("Insira o Valor a ser depositado: "))
            
            saldo, extrato = depositar(saldo, deposito, extrato)
        elif controle == "2":
            saque = float(input("Insira o Valor a ser saquado: "))
            
            saldo, extrato = sacar(saldo = saldo, saque = saque, extrato = extrato ,limite = limite, 
                                   n_saques = n_saques,limite_saques = LIMITE_SAQUES )
        elif controle == "3":
            imprimir_extrato(saldo, extrato = extrato)
        elif controle == "4":
            criar_usuario(usuarios)
            
        elif controle == "5":
            n_conta = len(contas)+1
            conta = criar_conta(ANGENCIA, n_conta, usuarios)
            if conta:
                contas.append(conta)
        elif controle == "6":
            listar_contas(contas)
            
        elif controle == "0":
            break
        else:
            print("\n_________OPERACAO INVALIDA_________\n")

main()