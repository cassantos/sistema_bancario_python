# Formação de python

import os
import random
import textwrap

# Clearing the Screen

def menu():
    main_menu = """ ---- Caixa Eletrônicao ----
    [d ]\tDepositar
    [s ]\tSacar
    [e ]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário 
    [lu]\tLista Usuários
    [q ] Sair
    => """ 
    return input(textwrap.dedent(main_menu))

# Função para saque (keyword only) 
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor >= 15:
        if valor <= limite:
            if numero_saques <= limite_saques:
                if valor <= saldo:
                    saldo -= valor 
                    extrato += f'Saque...:\t\t{valor*(-1):,.2f} \n' 
                    print('Saque realizado com sucesso!')
                else:
                    print('Saldo insuficiente')
            else:
                print('Número de saques diários excedido.')
        else:
            print('Valor do saque excede o limite autorizado.')
    else:
        print('Valor inválido de saque. Operação não realizada. Valor deve ser maior que R$15,00.') 

    espera = input('\nTecle [ENTER] para continuar....')
    return saldo, extrato

# Função Extrato (keyword e positional) 
def exibir_extrato(saldo, /, *, extrato):
    print(12 * '=' + ' EXTRATO ' + 12 * '=')
    print(extrato)
    print(33 * '=')
    print(f'Saldo total:\t\t{saldo:,.2f}')
    espera = input('\nTecle [ENTER] para continuar....')
    return saldo, extrato

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf == usuario[0]:
            print('Usuário encontrado')
        else:
            print('Usuário não encontrado')


# Função de cadastro de novos usuários
def criar_usuario(usuarios):
    ''' Armazenar usuário numa lista com:
    - nome
    - data de nascimento
    - cpf
    - endereço (string com o formato: logradouro, nro - bairro - cidade/siga estado) 
    '''
    cpf = input('Digite o CPF do usuário (somente números): ')
    if filtrar_usuario(cpf, usuarios) == None:
        usuario = input('Digite o nome do novo usuário: ')
        data_nascimento = input('Digite a data de nascimento no formato "mm-dd-aaaa": ')
        endereco = input('Digite o endereço: ')
        usuarios.append([usuario, cpf, data_nascimento, endereco])
        print('Usuario cadastrado com sucesso!')
    else:
        print('Usuário já cadastrado!')
    
    Espera = input('\nTecle [ENTER] para continuar....')
    
    return usuarios

def lista_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

    espera = input('\nTecle [ENTER] para continuar....')

def criar_conta(agencia, numero_conta, usuarios, contas):
    '''
    Armazenar a conta numa lista com:
    - número da conta (é um sequencial, iniciando em 1)
    - número da agência é uma contante com valor '0001'
    Outras regras: 
    - Um usuário pode ter mais de uma conta
    - Uma conta pode pertencer somente a um usuário
    '''
    numero_conta = numero_conta + 1
    usuario = len(usuarios)

    if usuario >= 1:
        contas.append([agencia, numero_conta, usuarios[len(usuarios)-1][1]])
        print(f'Conta {numero_conta} criada para o usuário {usuarios[len(usuarios)-1][0]} na agência {agencia}')
    else:
        print('Nenhum usuário selecionado.')

    espera = input('\nTecle [ENTER] para continuar....')
    return numero_conta

    
def listar_contas(contas):
    for conta in contas:
        print(conta)
    espera = input('\nTecle [ENTER] para continuar....')

# Função de depósito (positional only) 
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato +=  f"Deposito:\t\t{valor:,.2f}\n"
        print('Depósito efetuado com sucesso!')
    else:
        print('Valor de depósito inválido.')
        
    espera = input('\nTecle [ENTER] para continuar....')
    return saldo, extrato



def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_conta = 0
    usuarios = []
    contas = []
    
    while True:
        os.system('clear')
        opcao = menu()

        # **** DEPÓSITO ****
        if opcao == 'd' or opcao == 'D':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        # **** SAQUE ****
        elif opcao == 's' or opcao == 'S':
            valor = float(input('Informe o valor do saque (Valor mínimo R$15) : '))

            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES,
            )
            numero_saques += 1
            
        elif opcao == 'e' or opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu' or opcao == 'NU':
            criar_usuario(usuarios)

        elif opcao == 'lu' or opcao == 'LU':
            lista_usuarios(usuarios)

        elif opcao == 'nc' or opcao == 'NC':
            numero_conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == 'lc' or opcao == 'LC':
            listar_contas(contas)

        elif opcao == 'q' or opcao == 'Q':
            os.system('clear')
            break

main()