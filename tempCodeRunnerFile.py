mudar_data = input("Deseja mudar a data? (s/n): ")
if mudar_data.lower() == 's':
    data = input("Digite a nova data(DD-MM_AAAA): ")
    while True:
        try:
            data_obj = datetime.datetime.strptime(data, '%d-%m-%Y')
            data_atual = data
            break
        except ValueError:
            print("Data inválida. Digite no formato DD-MM-AAAA.")
            data = input("Digite a nova data (DD-MM-AAAA): ")