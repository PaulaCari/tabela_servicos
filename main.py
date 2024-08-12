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

print()

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

    
    print()

    #8. Perguntando se o usuário deseja adicionar mais um serviço
    while True:  # Loop para validar a resposta do usuário
        continuar = input("Deseja adicionar mais um serviço? (s/n): ")
        if continuar.lower() in ('s', 'n'):
            break
        else:
            print("Por favor, digite 's'  ou 'n' para não.")

    if continuar.lower() != 's':
        break
   
        
    print()

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
    
    
    print()
    
#10. Imprimindo tabela 
tabela_servicos.append({'item': '', 'data': '', 'cod': '', 'descricao': '', 'referencia': '', 'H/Q/L': 
                        '', 'comprimento': 'TOTAL', 'valor': f"R$ {total_valor:.2f}"})
#valor total na ultima linha
tabela_servicos[-1]['valor'] = f"R$ {total_valor:.2f}"
print()
print("-" * 100)
print("TABELA DE SERVIÇOS")
print("-" * 100)
#print(tabulate(tabela_servicos, headers="keys", tablefmt="grid",  showindex="always", justify='right'))
print(tabulate(tabela_servicos, headers="keys", tablefmt="grid",  showindex="always", colalign=("center",)*8))  
print("-" * 100)

print()




# 11. Perguntando se o usuário deseja editar algum item
while True:
    editar = input("Deseja editar algum item da tabela? (s/n): ")
    if editar.lower() in ('s', 'n'):
        break
    else:
        print("Por favor, digite 's'  ou 'n' para não.")

if editar.lower() == 's':
    
    print()
    

    # Loop principal para editar itens
    while True:
        # Lista para armazenar os números dos itens
        itens_a_editar = []
        while True:
            # Lista auxiliar para armazenar os itens selecionados temporariamente
            itens_selecionados_temp = []
            while True:
                try:
                    item_a_editar = int(input("Quais são os números dos item que deseja editar? (ou 0 para finalizar): "))
                    if item_a_editar == 0:
                        break
                    # Validação da entrada do usuário
                    while True:
                        if 1 <= item_a_editar <= len(tabela_servicos) - 1:  # Verifica se o item está dentro do intervalo válido
                            itens_selecionados_temp.append(item_a_editar)
                            break
                        else:
                            print("Número de item inválido. Por favor, digite um número válido.")
                            item_a_editar = int(input("Quais são os números dos item que deseja editar? (ou 0 para finalizar): "))
                except ValueError:
                    print("Por favor, digite um número inteiro válido.")

            # Perguntar ao usuário se ele deseja confirmar a seleção
            if itens_selecionados_temp:
                print("\nItens selecionados:")
                #print(tabulate([{'item': i} for i in itens_selecionados_temp], headers=["item"], tablefmt="grid"))
                while True:
                    confirmacao = input("Confirma a seleção? (s/n): ")
                    if confirmacao.lower() in ('s', 'n'):
                        break
                    else:
                        print("Por favor, digite 's' ou 'n'.")
                if confirmacao.lower() == 's':
                    # Copiar os itens selecionados para a lista final
                    itens_a_editar = itens_selecionados_temp.copy()
                    break  # Sai do loop principal
                else:
                    # Limpar a lista auxiliar
                    itens_selecionados_temp.clear()

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

        
        print()

        # Pede para o usuário selecionar o item a ser editado
        while True:
            try:
                item_a_editar = int(input("Qual item deseja editar primeiro?: "))
                # Verifica se o item está na lista de itens selecionados:
                if 1 <= item_a_editar <= len(itens_selecionados):  # Validação corrigida: de 1 até o tamanho da lista
                    break
                else:
                    print("Número de item inválido. Por favor, digite um número válido da tabela.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

        # Seleciona o item a ser editado
        item_selecionado = itens_selecionados[item_a_editar - 1]  # Usa o índice correto (lembrando que a numeração da tabela começa em 1)

        print()
        
      
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
                    opcao_edicao = int(input("Selecione um Numero na Opção de edição: "))
                    if opcao_edicao == 0:
                        break  # Sai do loop se o usuário digitar 0
                    elif 1 <= opcao_edicao <= 7:

                        # Editar o campo selecionado
                        if opcao_edicao == 1:  # Data
                            while True:
                                nova_data = input(f"Digite a nova data (DD-MM-AAAA) (item {item_selecionado['item']}): ")
                                try:
                                    datetime.datetime.strptime(nova_data, "%d-%m-%Y")  # Tenta converter a data para verificar se o formato está correto
                                    item_selecionado['data'] = nova_data  # Atualiza a data no item
                                    break  # Sai do loop se a data for válida
                                except ValueError:
                                    print("Data inválida. Por favor, digite no formato DD-MM-AAAA.")

                        elif opcao_edicao == 2:  # Código do serviço
                            while True:
                                novo_cod = input(f"Digite o novo código do serviço (item {item_selecionado['item']}): ")
                                if novo_cod in codigos_servicos:
                                    item_selecionado['cod'] = novo_cod
                                    item_selecionado['descricao'] = codigos_servicos[novo_cod]  # Atualiza a descrição também
                                    item_selecionado['valor'] = f"R$ {calcular_valor(novo_cod):.2f}"  # Calcula e atualiza o valor
                                    break
                                else:
                                    print("Código de serviço inválido. Por favor, tente novamente.")

                        elif opcao_edicao == 3:  # Descrição
                            nova_descricao = input(f"Digite a nova descrição (item {item_selecionado['item']}): ")
                            item_selecionado['descricao'] = nova_descricao

                        elif opcao_edicao == 4:  # Referência do cliente
                            nova_referencia = input(f"Digite a nova referência do cliente (item {item_selecionado['item']}): ")
                            item_selecionado['referencia'] = nova_referencia

                        elif opcao_edicao == 5:  # H/Q/L
                                
                                if item_selecionado['cod'] == '103':
                                    while True:
                                        try:
                                            novas_modelagens = int(input(f"Qtd de modelagens (Item {item_selecionado['item']}): "))
                                            item_selecionado['H/Q/L'] = f"0/{novas_modelagens}/0"  # Atualiza H/Q/L com novos tamanhos
                                            item_selecionado['valor'] = f"R$ {calcular_valor_103(novas_modelagens):.2f}"  # Recalcula o valor
                                            break
                                        except ValueError:
                                            print("Por favor, digite um número inteiro válido.")


                                elif item_selecionado['cod'] == '106':
                                    while True:
                                        try:
                                            novos_minutos = float(input(f"H/Q/L-Tiempo em minutos (Item {item_selecionado['item']}): "))
                                            item_selecionado['H/Q/L'] = f"{novos_minutos}/0/0"  # Atualiza H/Q/L com novos tamanhos
                                            item_selecionado['valor'] = f"R$ {calcular_valor_106(novos_minutos):.2f}"  # Recalcula o valor
                                            break
                                        except ValueError:
                                            print("Por favor, digite um número inteiro válido.")

                       

                        total_valor = sum(float(item['valor'].replace("R$ ", "").replace(",", ".")) for item in tabela_servicos if item['comprimento'] != 'TOTAL')
                        tabela_servicos[-1]['valor'] = f"R$ {total_valor:.2f}"  # Atualiza o valor total na última linha da tabela

                
                        
                  

                        

                        print()
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

                print()

        # Imprime a tabela com os itens editados (após o loop de edição)
        print("\nTabela de Serviços (Atualizada):")
        print(tabulate(tabela_servicos, headers="keys", tablefmt="grid",  showindex="always", colalign=("center",)*8))

        print()

        # Pergunta se o usuário deseja editar outro item
        while True:
            editar_outro_item = input("Deseja editar outro item? (s/n): ")
            if editar_outro_item.lower() in ('s', 'n'):
                break
            else:
                print("Por favor, digite 's' ou 'n'.")

        if editar_outro_item.lower() != 's':
            break  # Sai do loop principal se o usuário responder "n"
