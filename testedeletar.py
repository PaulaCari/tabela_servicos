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
