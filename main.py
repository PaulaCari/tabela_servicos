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
    return (minutos * (80/60),2)

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
        return round((comprimento * 27.5) / 500, 2) #valor >500
    
def calcular_valor_312(quantidade):
    return quantidade * 6

def calcular_valor_402(largura, comprimento):
    valor_fixo = 0.00044  #mt quadrado

    if largura <= 0 or comprimento <= 0:
        raise ValueError("largura e comprimento deven er valores Positivos.")
    
    valor = largura * comprimento * valor_fixo
    return f"R${valor:.2f}"


#3 Função Obter a descrição de serviço
def obter_descrição(codigo):
    return codigos_servicos.get(codigo, "Codigo Invalido")


#4 função calcula o valor do serviço com base no codigo
def calcular_valor (cod, quantidade=None, horas=None, minutos=None, modificacoes=None, tamanhos=None, largura=None, comprimento=None):

    if cod == '103':
        return f"R$ {calcular_valor_103(quantidade):.2f}"
    
    elif cod == '106':
        return f"R$ {calcular_valor_106(minutos): .2f}"
    
    elif cod == '109':
        return f"R$ { calcular_valor_109(modificacoes): .2f}"
    
    elif cod == '205':
        return f"R$ {calcular_valor_205(tamanhos): .2f}"
    
    elif cod == '111':
        return f"R$ {calcular_valos_111(quantidade): .2f}"
    
    elif cod == '311':
        return f"R$ { calcular_valor_311(quantidade): .2f}"
    
    elif cod == '304':
        return f"R$ { calcular_valor_304(largura, comprimento): .2f}"
    
    elif cod == '312':
        return f"R$ {calcular_valor_312(quantidade): .2f}"
        
    elif cod == '402':
        return f"R${calcular_valor_402(largura, comprimento): .2f}"
    
    else:
        return 0
    

#5 Criando a lista par armazenar os dados da tabela

    






