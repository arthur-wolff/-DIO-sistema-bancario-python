saldo   =   0
limite  =   500
extrato =   """ 
EXTRATO

"""
n_saques    =   0
LIMETE_SAQUES = 3


menu    =   """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
Insira a operacao: """

while True:
    
    controle = input(menu)
    
    if controle == "1":
        deposito = float(input("Digite o valor a ser depositado: "))
    
        if deposito >0:
            saldo += deposito
            print   (f"Valor depositado = R${deposito:.2f}\n")
            extrato += f"Deposito: R${deposito:.2f}\n"
        else:
            print   ("Valor invalido")
            
    if controle == "2":
        if saldo <= 0:
            print   ("Saldo insuficiente")
        else:
            saque = float(input("Digite o valor a ser sacado: "))
            
            saldo_insuficiente = saque > saldo
            limite_insuficiente = saque > limite
            n_saques_insuficientes = n_saques >= LIMETE_SAQUES
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
                
    if controle == "3":
        print   (extrato + f"Saldo: {saldo:.2f}")
    if controle == "0":
        break
    
        
                
                
            
            
            
        

    
    

    
        
    