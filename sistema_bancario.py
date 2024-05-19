# Formação de python

import os
import random

# Clearing the Screen

menu = """ ---- Caixa Eletrônicao ----
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """ 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0
extrato_data  = []
extrato_valor = []
dia = 1
mes = 5 
ano = 2024
saque_dia = 0
conta_saques_dia = 0

def dia_movimento():
    """
    Gera uma data aleatória e sequencial para simular o movimento bancário no tempo.
    """
    global dia, mes, ano 
    novo_dia = random.randint(1, 31)
    if dia > novo_dia:
        dia = novo_dia # avança um mês
        if mes == 12: # Se mês atual é dezembro, próximo mês é mês 1, janeiro
            mes = 1
            ano += 1
        else:
            mes += 1

    return(str(ano) + '-' + str(mes) + '-' +str(dia))

# Simula um dia para teste
diaUltimoSaque = dia_movimento()

while True:
    os.system('clear')
    opcao = input(menu)

    # **** DEPÓSITO ****
    if opcao == 'd' or opcao == 'D':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor 
            extrato_valor.append(valor)
            extrato_data.append(dia_movimento())
            print('Depósito efetuado com sucesso!')
            espera = input('\nTecle [ENTER] para continuar....')
        else:
            print('Valor de depósito inválido.')
            espera = input('\nTecle [ENTER] para continuar....')

    # **** SAQUE ****
    elif opcao == 's' or opcao == 'S':
        valor = 0
        while valor < 15:
            valor = float(input('Informe o valor do saque (Valor mínimo R$15) : '))

        hoje = dia_movimento()
        
        # Não permite saque acima do limite diário
        if saque_dia + valor <= limite:
            # Controle número de saques por dia
            if diaUltimoSaque == hoje:
                conta_saques_dia += 1
            else:
                conta_saques_dia = 1
                diaUltimoSaque = hoje
                saque_dia = 0

            # Não permite que sejam feitos mais saques que o permitido
            if conta_saques_dia <= LIMITE_SAQUES:
                if valor > 0:
                    if valor <= saldo:
                        extrato_valor.append(valor * (-1))
                        extrato_data.append(hoje)
                        saldo -= valor
                        saque_dia += valor

                        diaUltimoSaque = hoje
                    else:
                        print('Saldo insuficiente. Operação não realizada. ')
                else:
                    print('Valor inválido de saque. Operação não realizada. ') 
            else:
                print(f'O número máximo ({LIMITE_SAQUES}) de saques por dia foi excedido ')
        else:
            print('Este valor excede o limite de saque do dia')

        espera = input('\nTecle [ENTER] para continuar....')
            
    elif opcao == 'e' or opcao == 'E':
        print('\n================= EXTRATO =================')
        for index, v in enumerate(extrato_valor):
            deposito = True if extrato_valor[index] > 0  else False
            if deposito:
                print(f'Data: {extrato_data[index]} "Depósito: " R$  {extrato_valor[index]:,.2f}')
            else:
                print(f'Data: {extrato_data[index]} "Saque...: " R$ {extrato_valor[index]:,.2f}')

        print('\n==========================================')
        print(f'Saldo total: R$ {saldo:,.2f}') 
        print('==========================================')
        espera = input('\nTecle [ENTER] para continuar....')

    elif opcao == 'q' or opcao == 'Q':
        os.system('clear')
        break

