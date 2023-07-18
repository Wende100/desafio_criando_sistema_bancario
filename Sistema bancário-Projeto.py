nome = input("""
             =================== MENU =======================
    """)
print(f"seja bem vindo {nome.upper()} a sua conta!")

saldo = int(input("deposite um valor: "))
saque = 500
extrato = saque 
limite_saque = 3 
valor = 0
 
while True:
       
 opcao = int(input("selecione a opçao \n[1]deposito:\n[2]saque:\n[3]extrato:\n[4]sair: "))
 
 if valor > 0:
  saldo += valor
  saque -= saldo
  
  extrato +=f"deposito: $ {valor:.2f}\n"
 elif saque > saldo:
  print("saldo insuficiente!")
         
 elif opcao == 1:
  print(f"se deposito foi de $ {saldo}")
    
 elif opcao == 2:
  print(f"seu saque foi de $ {saque}")
        
 elif opcao == 3:
     print(f"seu extra e de $ {extrato:.2f}")
        
 elif opcao == 4:
     print("saindo... obrigado por usar nosso serviço")
     break

 else:
     print("opração invalida!!!")
     opcao.clear()
