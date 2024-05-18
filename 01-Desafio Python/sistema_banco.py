#Sistema bancario simples com as funcionalidades de sacar, depositar e Extrato

nome_banco = "Banco Manu Digital"
saldo = 0                                                          # saldo inicial será 0 até que seja feito um deposito
limite = 500                                                       # valor máximo de saque permitido
numero_saque = 3                                                   # número máximo de saques permitidos
acao_saque = 0                                                     # contador de saques realizados
extrato = ""   
quantidade_deposito = 0                                            #contador de depositos realizados
total_deposito = 0                                                 #valor total de depositos

menu_de_transacao = f"""
====================Escolha uma opção=======================
[1] - Sacar 
[2] - Depositar 
[3] - Extrato
[4] - Sair
============================================================  
"""


while True:
    print("") 
    print(nome_banco.center(65))                                   #apresenta o nome do banco centralizado
    opcao = int(input(menu_de_transacao))

    if opcao == 1:         
       saque = float(input("Digite o valor que deseja sacar:"))

    # Verificação das condições para saque  
       saldo_maximo = saque > saldo 
       limite_maximo = saque > limite
       limite_saques = acao_saque >= numero_saque
       
       if saldo_maximo:
          print("\nFalha na transação! Saldo insuficiente") 

       elif limite_maximo:
        print("\nFalha na transação!O valor de saque excede o limite diário.")
        
       elif limite_saques:
        print("\nFalha na transação! você atingiu o limite de saques diário.")
        
       elif saque > 0:
        saldo -= saque
        acao_saque += 1
        extrato += f"Saque: R$ {saque:.2f}\n"
        print(f"\n O seu saque no valor de R$ {saque:.2f} foi realizado com sucesso.")   

       else:
          print("\n O valor de saque não pode ser menor ou igual a 0")  
    
    elif opcao == 2:
       valor_deposito = float(input("\nDigite o valor que deseja depositar: "))

       # Verificação das condições para deposito  
       if valor_deposito > 0:
            quantidade_deposito += 1
            saldo += valor_deposito
            total_deposito += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"\nO seu deposito no valor de R$ {valor_deposito:.2f} foi realizado com sucesso.")
       else:
             print("\nFalha no seu deposito, revise o valor informado.")
         

    elif opcao == 3:
         print("====================Extrato Simplificado======================= ")
         print("Não foram identificadas movimentações em sua conta." if not extrato else extrato)          
         mensagem_final=(f"Quantidade total de saque: {acao_saque} \nTotal de depositos: {quantidade_deposito} \nValor total depositado: R${total_deposito:.2f}")   
         mensagem_sem_espaco=mensagem_final.strip()      
         print(f"{mensagem_sem_espaco}")
         print("================================================================")
         print(f"\nSaldo total: R$ {saldo:.2f}")
    
    # Opcional: sair do loop após a escolha do cliente
    elif opcao == 4:
       print("\nObrigado(a) por usar os nossos serviços.")   
       break        
          
