from VeiculoEletrico import VeiculoEletrico
veiculo = VeiculoEletrico()
    
while True:
        print("\nMenu:")
        print("1. Cadastrar Veículo")
        print("2. Consultar Veículos")
        print("3. Iniciar Carregamento")
        print("4. Finalizar Carregamento")
        print("5. Consultar Status")
        print("6. Deletar Veículo")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            tempo_carregamento = float(input("Tempo de Carregamento (horas): "))
            veiculo.cadastrarVeiculo(placa, modelo, tempo_carregamento)
        
        elif opcao == '2':
            veiculo.consultarVeiculos()
        
        elif opcao == '3':
            try:
                id = int(input("ID do veículo: "))
                veiculo.iniciarCarregamento(id)
            except ValueError:
                print("ID deve ser um número.")
        
        elif opcao == '4':
            try:
                id = int(input("ID do veículo: "))
                custo = float(input("Custo por hora: "))
                veiculo.finalizarCarregamento(id, custo)
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
        
        elif opcao == '5':
            try:
                id = int(input("ID do veículo: "))
                veiculo.consultarStatus(id)
            except ValueError:
                print("ID deve ser um número.")
        
        elif opcao == '6':
            try:
                id = int(input("ID do veículo: "))
                veiculo.deletarVeiculo(id)
            except ValueError:
                print("ID deve ser um número.")
        
        elif opcao == '7':
            veiculo.close()
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
