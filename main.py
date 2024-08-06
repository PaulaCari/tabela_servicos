import csv
import datetime
from tabulate import tabulate

#1 Definiendo dicionario codigos de serviços

codigos_servicos = {
    '103': 'Modelagem Básica',
    '106': 'Modelagem (Hora)',
    '109': 'Modificação de modelagem',
    '205': 'Graduação',
    '111': 'Conversão de Arquivo',
    '311': 'Reabrir Encaixe',
    '304': 'Encaixe',
    '312': 'Minirisco',
    '402': 'Plotagem de Risco'  
}


#2 função Calculando valor de cada serviço

def  calcular_valor_103(quantidade):
    return quantidade * 25

def calcular_valor_106(minutos):
    return round(minutos * (80/60),2)

def calcular_valor_109(modificacoes):
    return 6 +(modificacoes -1) * 3

def calcular_valor_205(tamanhos) :
    return tamanhos * 25

def calcular_valos_111(quantidade):
    return quantidade * 15

def calcular_valor_311(quantidade):
    return quantidade * 6

def calcular_valor_304(largura, comprimento):
    if comprimento <= 500:
        return 27.50 #valor fixo <500
    
    else:
        return round((comprimento * 27.5) / 500, 2) #valor comprimento >500
    
def calcular_valor_312(quantidade):
    return quantidade * 6

def calcular_valor_402(largura, comprimento):
    valor_fixo = 0.00044  #mt quadrado

    if largura <= 0 or comprimento <= 0:
        raise ValueError("largura e comprimento deven ser valores Positivos.")
    
    valor = largura * comprimento * valor_fixo
    return f"R${valor:.2f}"


#3 Função Obter a descrição de serviço
def obter_descricao(codigo):
    return codigos_servicos.get(codigo, "Codigo Invalido")


#4 função calcula o valor do serviço com base no codigo
def calcular_valor (cod, quantidade=None, horas=None, minutos=None, modificacoes=None, tamanhos=None, largura=None, comprimento=None):

    if cod == '103':
        return f"R$ {calcular_valor_103(quantidade):.2f}"
    
    elif cod == '106':
        return f"R$ {calcular_valor_106(minutos):.2f}"
    
    elif cod == '109':
        return f"R$ { calcular_valor_109(modificacoes):.2f}"
    
    elif cod == '205':
        return f"R$ {calcular_valor_205(tamanhos):.2f}"
    
    elif cod == '111':
        return f"R$ {calcular_valos_111(quantidade):.2f}"
    
    elif cod == '311':
        return f"R$ {calcular_valor_311(quantidade):.2f}"
    
    elif cod == '304':
        return f"R$ {calcular_valor_304(largura, comprimento):.2f}"
    
    elif cod == '312':
        return f"R$ {calcular_valor_312(quantidade):.2f}"
        
    elif cod == '402':
        return calcular_valor_402(largura, comprimento)  # Retorna a string já formatada
    else:
        return 0
    

#5 Criando a lista para armazenar os dados da tabela
tabela_servicos = []
total_valor = 0
item_atual = 1
data_atual = None


#6 Loop para receber os dados do usuario e adicionar a tabela
while True:
    item = input("Digite o Item: ")

    data = input("Data (DD-MM-AAAA): ")

    cod = input("Digite o código do serviço: ")
    descricao = obter_descricao(cod)

    referencia = input("Ref. do cliente:")
    #Entrada para os dados especificos

    # Ajustando a entrada para os códigos específicos
    if cod == '103':
        quantidade = int(input("Qtd de modelagens: "))
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod, quantidade=quantidade)

    elif cod == '106':
        minutos = float(input("H/Q/L-Tiempo em minutos: "))
        h_q_l = f"{minutos}/0/0"
        comprimento = 0
        valor = calcular_valor(cod, minutos=minutos)

    elif cod == '109':
        modificacoes = int(input("Qtd de modificações: "))
        h_q_l = f"0/{modificacoes}/0"
        comprimento = 0
        valor = calcular_valor(cod, modificacoes=modificacoes)

    elif cod =='205':
        tamanhos = int(input("Qtd de tamanhos: "))
        h_q_l = f"0/{tamanhos}/0"
        comprimento = 0
        valor = calcular_valor(cod, tamanhos=tamanhos)

    elif cod =='111':
        quantidade = int(input("Qtd Conversão de Arquivos: "))
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod,quantidade=quantidade)

    elif cod == '311':
        quantidade = int(input("Qtd Reabrir Encaixe: "))
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod, quantidade=quantidade)

    elif cod == '304':
        largura = float(input("H/Q/L - Largura Util: "))
        comprimento = float(input("Comprimento: "))
        h_q_l = f"0/0/{largura}"
        valor = calcular_valor(cod, largura=largura, comprimento=comprimento)

    elif cod == '312':
        quantidade = int(input("Qtd de Miniriscos: "))
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod, quantidade=quantidade)

    elif cod == '402':
        largura = float(input("H/Q/L - Largura: "))
        comprimento = float(input("Comprimento: "))
        h_q_l = f"0/0/{largura}"
        valor = calcular_valor(cod, largura=largura, comprimento=comprimento)

    else:
        h_q_l = input("Digite H/Q/L (Separados por barras): ")
        horas,quantidade,largura = map(float, h_q_l.split("/"))
        comprimento = float(input("Digite o comprimento: "))
        valor = calcular_valor(cod, horas=horas, largura=largura, comprimento=comprimento)

    #7 Adicionando os dados do serviço a tabela
    novo_servico = {
        'item': item_atual,
        'data': data,
        'cod': cod,
        'descricao': descricao,
        'referencia': referencia,
        'H/Q/L': h_q_l,
        'comprimento': comprimento,
        'valor': valor
    }

    tabela_servicos.append(novo_servico)
    # CORRIGIDO: Remove a vírgula (,) do valor antes de converter para float
    total_valor += float(valor.strip("R$ "))
    #total_valor += float(valor.replace("R$ ", "").replace(".", "")) # Atualizando o total_valor a cada novo serviço 
    item_atual += 1  # Incrementando o item_atual para o próximo serviço


    #8. Perguntando se o usuário deseja adicionar mais um serviço
    continuar = input("Deseja adicionar mais um serviço? (s/n): ")
    if continuar.lower() != 's':
        break

#9. Imprimindo tabela 
tabela_servicos.append({'item': '', 'data': '', 'cod': '', 'descricao': '', 'referencia': '', 'H/Q/L': '', 'comprimento': 'TOTAL', 'valor': f"R$ {total_valor:.2f}"})
#valor total na ultima linha
tabela_servicos[-1]['valor'] = f"R$ {total_valor:.2f}"


print("-" * 100)
print("Tabela de Serviços")
print("-" * 100)
print(tabulate(tabela_servicos, headers="keys", tablefmt="grid",  showindex="always"))
print("-" * 100)
