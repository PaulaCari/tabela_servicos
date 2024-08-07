# 10. Perguntando se o usuário deseja editar algum item
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
                        while True:
                            novo_h_q_l = input("Digite o novo valor para H/Q/L (separados por barras): ")
                            try:
                                horas, quantidade, largura = map(float, novo_h_q_l.split("/"))
                                for item in itens_selecionados:
                                    item['H/Q/L'] = novo_h_q_l
                                break
                            except ValueError:
                                print("Por favor, digite valores numéricos válidos separados por barras.")
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