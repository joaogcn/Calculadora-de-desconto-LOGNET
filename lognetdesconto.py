import os

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcPix():
    descontEntrada = 0.2
    desconto3 = 0.15
    desconto10 = 0.05
    try:
        valorTotal = float(input('Insira o valor total da compra (Sem Descontos): '))
        entrada = float(input('Insira o valor da entrada em dinheiro ou pix: '))
        parcelas = int(input('Insira a quantidade de parcelas: '))
        if parcelas <= 3:
            desconto = desconto3
        elif parcelas > 3:
            desconto = desconto10
        valorAbate = valorTotal-entrada
        reserva1 = valorAbate*desconto
        reserva2 = entrada*descontEntrada
        reserva = reserva1 + reserva2
        valorFinal = valorTotal - reserva
        valorParcelas = (valorFinal - entrada)/parcelas
        clean_terminal()
        print(f'O valor final foi {valorFinal}')
        print(f'O desconto foi de {reserva}')
        print(f'Depois da entrada, as parcelas ficaram {valorParcelas:.2f} reais.\n')
    except:
        print('Erro na inserção dos dados. Não usar virgula, sempre usem ponto.\n')

def calc15():
    try:
        descontEntrada = 0.2
        desconto3 = 0.15
        desconto10 = 0.05
        valorTotal = float(input('Insira o valor total da compra (Sem Descontos): '))
        entrada = float(input('Insira o valor da entrada em cartão até 3x: '))
        parcelas3x = int(input('Insira a quantidade de parcelas em até 3x: '))
        parcelas10x = int(input('Insira a quantidade de parcelas em até 10x: '))
        valorAbate = valorTotal-entrada
        reserva1 = valorAbate*desconto10
        reserva2 = entrada*desconto3
        reserva = reserva1 + reserva2
        valorFinal = valorTotal - reserva
        valorParcelas3x = entrada/parcelas3x
        valorParcelas10x = (valorFinal - entrada)/parcelas10x
        clean_terminal()
        print(f'O valor final foi {valorFinal}')
        print(f'O desconto foi de {reserva}')
        print(f'A entrada ficou {valorParcelas3x:.2f} reais em {parcelas3x} vezes.')
        print(f'O restante ficou {valorParcelas10x:.2f} reais em {parcelas10x} vezes.')
    except:
        print('Erro na inserção dos dados. Não usar virgula, sempre usem ponto.\n')

def descontos():
    try:
        valorTotal = float(input('Insira o valor total da compra (Sem Descontos): '))
        pix = valorTotal*0.8
        valor3x = valorTotal*0.85
        valor10x = valorTotal*0.95
        clean_terminal()
        print(f'Valor no Pix ou Dinheiro: {pix:.2f}')
        print(f'Valor no cartão até 3x: {valor3x:.2f}')
        print(f'Valor no cartão a partir de 4x até 10x: {valor10x:.2f}')
    except:
        print('Erro na inserção dos dados. Não usar virgula, sempre usem ponto.\n')

while True:
    print('---------- MENU ----------')
    print(f'1. Entrada Pix/Dinheiro')
    print(f'2. Entrada Cartão 3x.')
    print(f'3. Valores com descontos.')
    print(f'4. SAIR.')
    escolha = int(input('Digite a escolha: '))
    if escolha == 1:
        calcPix()
    elif escolha == 2:
        calc15()
    elif escolha == 3:
        descontos()
    elif escolha == 4:
        break
    else:
        print('Erro na escolha da opção.')