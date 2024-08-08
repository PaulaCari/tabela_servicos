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

def calcular_valor_111(quantidade):
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
    return f"R$ {valor:.2f}"

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
        return f"R$ {calcular_valor_111(quantidade):.2f}"
    
    elif cod == '311':
        return f"R$ {calcular_valor_311(quantidade):.2f}"
    
    elif cod == '304':
        return f"R$ {calcular_valor_304(largura, comprimento):.2f}"
    
    elif cod == '312':
        return f"R$ {calcular_valor_312(quantidade):.2f}"

      
    elif cod == '402':
        return calcular_valor_402(largura, comprimento)  # Retorna a string já formatada
        #return f"R$ {calcular_valor_402(largura, comprimento):.2f}"  
    
    else:
        return 0
    
   
    

#5 Criando a lista para armazenar os dados da tabela
tabela_servicos = []
total_valor = 0
item_atual = 1
data_atual = None # Inicializa a data atual como None

#6 Loop para receber os dados do usuario e adicionar a tabela
while True:
    #item = input("Digite o item: ")

    # Se não há uma data atual definida, solicita uma nova
    if data_atual is None:
        data = input("Digite a data (DD-MM-AAAA): ")
        while True:
            try:
                data_obj = datetime.datetime.strptime(data, '%d-%m-%Y')
                data_atual = data  # Define a data atual
                break
            except ValueError:
                print("Data inválida. Digite no formato DD-MM-AAAA.")
                data = input("Digite a data (DD-MM-AAAA): ")
    else:
        # Caso contrário, usa a data atual
        data = data_atual
            

   
    while True:
        cod = input("Digite o código do serviço: ")
        
        #verificar sim o cod e valido
        if cod in codigos_servicos:
            break  # Sai do loop se o código for válido
        else:
            print("Codigo de serviço invalido. Por favor tente novamente.")

    descricao = obter_descricao(cod)

    while True:
        referencia = input("Ref. do cliente:")
        if referencia:
            break
        else:
            print('A referencia do cliente deve ser prenchida. Por favor tente novamente.')

    # Ajustando a entrada para os códigos específicos
    if cod == '103':
        while True:  # Loop para validar a quantidade de modelagens
            try:
                quantidade = int(input("Qtd de modelagens: "))
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod, quantidade=quantidade)

    elif cod == '106':
        while True:
            try:
                minutos = float(input("H/Q/L-Tiempo em minutos: "))
                break
            except ValueError:
                print("Por favor digite o tempo em minutos")
        h_q_l = f"{minutos}/0/0"
        comprimento = 0
        valor = calcular_valor(cod, minutos=minutos)

    elif cod == '109':
        while True:
            try:
                modificacoes = int(input("Qtd de modificações: "))
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        h_q_l = f"0/{modificacoes}/0"
        comprimento = 0
        valor = calcular_valor(cod, modificacoes=modificacoes)

    elif cod =='205':
        while True:
            try:
                tamanhos = int(input("Qtd de tamanhos: "))
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        h_q_l = f"0/{tamanhos}/0"
        comprimento = 0
        valor = calcular_valor(cod, tamanhos=tamanhos)

    elif cod =='111':
        while True:
            try:
                quantidade = int(input("Qtd Conversão de Arquivos: "))
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod,quantidade=quantidade)

    elif cod == '311':
        while True:  
            try:
                quantidade = int(input("Qtd Reabrir Encaixe: "))
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod, quantidade=quantidade)

    elif cod == '304':
        while True:  # Loop para validar a largura
            try:
                largura = float(input("H/Q/L - Largura Util: "))
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Por favor, digite um número válido.")
        while True:  # Loop para validar o comprimento
            try:
                comprimento = float(input("Comprimento: "))
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Por favor, digite um número válido.")
        h_q_l = f"0/0/{largura}"
        valor = calcular_valor(cod, largura=largura, comprimento=comprimento)

    elif cod == '312':
        while True:  # Loop para validar a quantidade de miniriscos
            try:
                quantidade = int(input("Qtd de Miniriscos: "))
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        h_q_l = f"0/{quantidade}/0"
        comprimento = 0
        valor = calcular_valor(cod, quantidade=quantidade)

    elif cod == '402':
        while True:  # Loop para validar a largura
            try:
                largura = float(input("H/Q/L - Largura: "))
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Por favor, digite um número válido.")
        while True:  # Loop para validar o comprimento
            try:
                comprimento = float(input("Comprimento: "))
                break  # Sai do loop se a entrada for válida
            except ValueError:
                print("Por favor, digite um número válido.")
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
    total_valor += float(valor.strip("R$  "))
    #total_valor += float(valor.replace("R$ ", "").replace(".", "")) # Atualizando o total_valor a cada novo serviço 
    item_atual += 1  # Incrementando o item_atual para o próximo serviço

    #8. Perguntando se o usuário deseja adicionar mais um serviço
    while True:  # Loop para validar a resposta do usuário
        continuar = input("Deseja adicionar mais um serviço? (s/n): ")
        if continuar.lower() in ('s', 'n'):
            break
        else:
            print("Por favor, digite 's'  ou 'n' para não.")

    if continuar.lower() != 's':
        break

# 9. Perguntando se o usuário deseja mudar a data
    while True:  # Loop para validar a resposta do usuário
        mudar_data = input("Deseja mudar a data? (s/n): ")
        if mudar_data.lower() in ('s', 'n'):
            break
        else:
            print("Por favor, digite 's'  ou 'n' para não.")

    if mudar_data.lower() == 's':
        data = input("Digite a nova data (DD-MM-AAAA): ")
        while True:
            try:
                data_obj = datetime.datetime.strptime(data, '%d-%m-%Y')
                data_atual = data
                break
            except ValueError:
                print("Data inválida. Digite no formato DD-MM-AAAA.")
                data = input("Digite a nova data (DD-MM-AAAA): ")
    

#10. Imprimindo tabela 
tabela_servicos.append({'item': '', 'data': '', 'cod': '', 'descricao': '', 'referencia': '', 'H/Q/L': 
                        '', 'comprimento': 'TOTAL', 'valor': f"R$ {total_valor:.2f}"})
#valor total na ultima linha
tabela_servicos[-1]['valor'] = f"R$ {total_valor:.2f}"

print("-" * 100)
print("TABELA DE SERVIÇOS")
print("-" * 100)
#print(tabulate(tabela_servicos, headers="keys", tablefmt="grid",  showindex="always", justify='right'))
print(tabulate(tabela_servicos, headers="keys", tablefmt="grid",  showindex="always", colalign=("center",)*8))  
print("-" * 100)

# 11. Perguntando se o usuário deseja editar algum item
while True:
    editar = input("Deseja editar algum item da tabela? (s/n): ")
    if editar.lower() in ('s', 'n'):
        break
    else:
        print("Por favor, digite 's'  ou 'n' para não.")

if editar.lower() == 's':
    # Lista para armazenar os números dos itens
    itens_a_editar = []
    while True:
        try:
            item_a_editar = int(input("Digite o número do item que deseja editar (ou 0 para finalizar): "))
            if item_a_editar == 0:
                break
            itens_a_editar.append(item_a_editar)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    # Iterando pelos itens a serem editados
    itens_selecionados = []  # Lista para armazenar os itens selecionados
    for item_numero in itens_a_editar:
        # Encontrando o item na lista
        item_selecionado = next((item for item in tabela_servicos if item['item'] == item_numero), None)

        if item_selecionado:
            # Adicionando o item selecionado à lista
            itens_selecionados.append(item_selecionado)

            # Exibindo os dados do item selecionado a tab de cada item selecionado fica redudante
            #print("\nDados do item selecionado:")
            #print(tabulate([item_selecionado], headers="keys", tablefmt="grid"))

        else:
            print(f"Item {item_numero} não encontrado.")

    # Imprimindo os itens selecionados após o loop
    if itens_selecionados:
        print("\nItens selecionados:")
        print(tabulate(itens_selecionados, headers="keys", tablefmt="grid"))

    # Mostrando as opções de edição (fora do loop)
    if itens_selecionados:
        print("\nOpções de edição:")
        print("1. Data")
        print("2. Código do serviço")
        print("3. Descrição")
        print("4. Referência do cliente")
        print("5. H/Q/L")
        print("6. Comprimento")
        print("7. Valor")
        print("0. Terminar edição dos itens")  # Opção para sair do loop
        print()
        while True:
            try:
                opcao_edicao = int(input("Digite o número da opção que deseja editar: "))
                if opcao_edicao == 0:
                    break  # Sai do loop se o usuário digitar 0
                elif 1 <= opcao_edicao <= 7:

                    # Editar o campo selecionado
                    if opcao_edicao == 1:  # Data
                        while True:
                            nova_data = input("Digite a nova data (DD-MM-AAAA): ")
                            try:
                                datetime.datetime.strptime(nova_data, "%d-%m-%Y")  # Tenta converter a data para verificar se o formato está correto
                                for item in itens_selecionados:
                                    item['data'] = nova_data  # Atualiza a data no item
                                break  # Sai do loop se a data for válida
                            except ValueError:
                                print("Data inválida. Por favor, digite no formato DD-MM-AAAA.")

                    elif opcao_edicao == 2:  # Código do serviço
                        while True:
                            novo_cod = input("Digite o novo código do serviço: ")
                            if novo_cod in codigos_servicos:
                                for item in itens_selecionados:
                                    item['cod'] = novo_cod
                                    item['descricao'] = codigos_servicos[novo_cod]  # Atualiza a descrição também
                                break
                            else:
                                print("Código de serviço inválido. Por favor, tente novamente.")

                    elif opcao_edicao == 3:  # Descrição
                        nova_descricao = input("Digite a nova descrição: ")
                        for item in itens_selecionados:
                            item['descricao'] = nova_descricao

                    elif opcao_edicao == 4:  # Referência do cliente
                        nova_referencia = input("Digite a nova referência do cliente: ")
                        for item in itens_selecionados:
                            item['referencia'] = nova_referencia
                            

                    elif opcao_edicao == 5:  # H/Q/L
                        # Verifica se o código do serviço é 205
                        if any(item['cod'] == '205' for item in itens_selecionados):
                            while True:
                                try:
                                    novos_tamanhos = int(input("Qtd de tamanhos: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '205':
                                            item['H/Q/L'] = f"0/{novos_tamanhos}/0"  # Atualiza H/Q/L com novos tamanhos
                                    break
                                except ValueError:
                                    print("Por favor, digite um número inteiro válido.")

                        elif any(item['cod'] == '103' for item in itens_selecionados):
                            while True:
                                try:
                                    novas_modelagens = int(input("Qtd de modelagens: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '103':
                                            item['H/Q/L'] = f"0/{novas_modelagens}/0"  # Atualiza H/Q/L com novos tamanhos
                                            item['valor'] = f"R$ {calcular_valor_103(novas_modelagens):.2f}"  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite um número inteiro válido.")

                        elif any(item['cod'] == '106' for item in itens_selecionados):
                            while True:
                                try:
                                    novos_minutos = float(input("H/Q/L-Tiempo em minutos: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '106':
                                            item['H/Q/L'] = f"{novos_minutos}/0/0"  # Atualiza H/Q/L com novos tamanhos
                                            item['valor'] = f"R$ {calcular_valor_106(novos_minutos):.2f}"  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite um número inteiro válido.")

                        elif any(item['cod'] == '109' for item in itens_selecionados):
                            while True:
                                try:
                                    novas_modificacoes = int(input("Qtd de modificações: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '109':
                                            item['H/Q/L'] = f"0/{novas_modificacoes}/0"  # Atualiza H/Q/L com novos tamanhos
                                            item['valor'] = f"R$ {calcular_valor_109(novas_modificacoes):.2f}"  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite um número inteiro válido.")

                        elif any(item['cod'] == '111' for item in itens_selecionados):
                            while True:
                                try:
                                    novas_conversoes = int(input("Qtd Conversão de Arquivos: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '111':
                                            item['H/Q/L'] = f"0/{novas_conversoes}/0"  # Atualiza H/Q/L com novos tamanhos
                                            item['valor'] = f"R$ {calcular_valor_111(novas_conversoes):.2f}"  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite um número inteiro válido.")

                        elif any(item['cod'] == '311' for item in itens_selecionados):
                            while True:
                                try:
                                    novas_reaberturas = int(input("Qtd Reabrir Encaixe: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '311':
                                            item['H/Q/L'] = f"0/{novas_reaberturas}/0"  # Atualiza H/Q/L com novos tamanhos
                                            item['valor'] = f"R$ {calcular_valor_311(novas_reaberturas):.2f}"  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite um número inteiro válido.")

                        elif any(item['cod'] == '312' for item in itens_selecionados):
                            while True:
                                try:
                                    novos_miniriscos = int(input("Qtd de Miniriscos: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '312':
                                            item['H/Q/L'] = f"0/{novos_miniriscos}/0"  # Atualiza H/Q/L com novos tamanhos
                                            item['valor'] = f"R$ {calcular_valor_312(novos_miniriscos):.2f}"  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite um número inteiro válido.")

                        
                            
                        elif any(item['cod'] == '304' for item in itens_selecionados):
                            while True:
                                try:
                                    nova_largura = float(input("H/Q/L - Largura Util: "))
                                    novo_comprimento = float(input("Comprimento: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '304':
                                            item['H/Q/L'] = f"0/0/{nova_largura}"
                                            item['comprimento'] = novo_comprimento  # Atualiza o comprimento também
                                            # Utiliza a função calcular_valor_304 para calcular o valor correto
                                            # Extrai a largura atual do campo H/Q/L
                                            largura_atual = float(item['H/Q/L'].split('/')[-1])
                                            # Utiliza a função calcular_valor_304 para calcular o valor correto
                                            item['valor'] = f"R$ {calcular_valor_304(largura_atual, novo_comprimento):.2f}"  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite valores numéricos válidos.") 


                        elif any(item['cod'] == '402' for item in itens_selecionados):
                            while True:
                                try:
                                    nova_largura = float(input("H/Q/L - Largura: "))
                                    novo_comprimento = float(input("Comprimento: "))
                                    for item in itens_selecionados:
                                        if item['cod'] == '402':
                                            item['H/Q/L'] = f"0/0/{nova_largura}"
                                            item['comprimento'] = novo_comprimento  # Atualiza o comprimento também
                                            # Utiliza a função calcular_valor_402 para calcular o valor correto com os novos valores
                                            item['valor'] = calcular_valor_402(nova_largura, novo_comprimento)  # Recalcula o valor
                                    break
                                except ValueError:
                                    print("Por favor, digite valores numéricos válidos.")

                                    

                    elif opcao_edicao == 6:  # Comprimento
                        while True:
                            try:
                                novo_comprimento = float(input("Digite o novo comprimento: "))
                                if novo_comprimento >= 0:
                                    for item in itens_selecionados:
                                        item['comprimento'] = novo_comprimento
                                    break
                                else:
                                    print("O comprimento deve ser um valor positivo.")
                            except ValueError:
                                print("Por favor, digite um valor numérico válido.")

                    elif opcao_edicao == 7:  # Valor
                        while True:
                            novo_valor = input("Digite o novo valor: ")
                            try:
                                novo_valor = float(novo_valor.replace("R$ ", "").replace(",", "."))  # Remove "R$ " e "," para converter para float
                                for item in itens_selecionados:
                                    item['valor'] = f"R$ {novo_valor:.2f}"
                                break
                            except ValueError:
                                print("Por favor, digite um valor numérico válido.")


                    # Atualiza o valor total (após editar o valor do serviço)
                    total_valor = sum(float(item['valor'].replace("R$ ", "").replace(",", ".")) for item in tabela_servicos if item['comprimento'] != 'TOTAL')
                    tabela_servicos[-1]['valor'] = f"R$ {total_valor:.2f}"  # Atualiza o valor total na última linha da tabela

                    # Perguntar se o usuário deseja editar outro campo
                    while True:
                        editar_outro_campo = input("Deseja editar outro campo? (s/n): ")
                        if editar_outro_campo.lower() in ('s', 'n'):
                            break
                        else:
                            print("Por favor, digite 's'  ou 'n' para não.")
                    if editar_outro_campo.lower() != 's':
                        break # Sai do loop de edição de campos
                    
                    
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    # Imprime a tabela com os itens editados (após o loop de edição)
    print("\nTabela de Serviços (Atualizada):")
    print(tabulate(tabela_servicos, headers="keys", tablefmt="grid",  showindex="always", colalign=("center",)*8))