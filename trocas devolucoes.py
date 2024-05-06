pc = []
er = []
while True:
    iniciar = int(input("Digite 1 para registrar uma troca/devolução paga pela cliente.\nDigite 2 para registrar uma troca/devolução paga pela loja.\nDigite qualquer outro número para sair."))
    if iniciar == 1:
            cliente_data_motivo1 = {}
            cliente_data_motivo1['cliente'] = input("Digite o nome da cliente: ")
            cliente_data_motivo1['dia'] = int(input("Insira o dia: "))
            cliente_data_motivo1['mes'] = input("Insira o mês: ")
            cliente_data_motivo1['ano'] = int(input("Insira o ano: "))
            cliente_data_motivo1['motivo'] = input("Digite o motivo da troca/devolução: ")
            cliente_data_motivo1['vendedora'] = input("Digite o nome da vendedora: ")
            status = int(input("Digite 1 para status 'resolvido'\nDigite qualquer outro número para status 'pendente'"))
            if status == 1:
                status = 'Resolvido'
            else:
                status = 'Pendente'
            cliente_data_motivo1['status'] = status
            pc.append(cliente_data_motivo1)
            print('Trocas/devoluções cadastradas:')
            for itempc in pc:
                 print(f'Cliente: {itempc['cliente']}, Dia: {itempc['dia']}, Mês: {itempc['mes']}, Ano: {itempc['ano']}, Motivo: {itempc['motivo']}, Vendedora: {itempc['vendedora']}, Status: {itempc['status']}, frete pago pela cliente.')
            for itemer in er:
                print(f'Cliente: {itemer['cliente']}, Dia: {itemer['dia']}, Mês: {itemer['mes']}, Ano: {itemer['ano']}, Motivo: {itemer['motivo']}, Vendedora: {itemer['vendedora']}, Status: {itemer['status']},frete pago pela loja.')
            menu = int(input("Digite 1 para cadastrar outra troca/devolução.\nDigite qualquer outro número para sair."))
            if menu !=1 :
                print("Programa finalizado!")
                break
    elif iniciar == 2:
            cliente_data_motivo2 = {}
            cliente_data_motivo2['cliente'] = input("Digite o nome da cliente: ")
            cliente_data_motivo2['dia'] = int(input("Insira o dia: "))
            cliente_data_motivo2['mes'] = input("Insira o mês: ")
            cliente_data_motivo2['ano'] = int(input("Insira o ano: "))
            cliente_data_motivo2['motivo'] = input("Digite o motivo da troca/devolução: ")
            cliente_data_motivo2['vendedora'] = input("Digite o nome da vendedora: ")
            status = int(input("Digite 1 para status 'resolvido'\nDigite qualquer outro número para status 'pendente'"))
            if status == 1:
                status = 'Resolvido'
            else:
                status = 'Pendente'
            cliente_data_motivo2['status'] = status
            er.append(cliente_data_motivo2)
            print('Trocas/devoluções cadastradas:')
            for itempc in pc:
                print(f'Cliente: {itempc['cliente']}, Dia: {itempc['dia']}, Mês: {itempc['mes']}, Ano: {itempc['ano']}, Motivo: {itempc['motivo']}, Vendedora: {itempc['vendedora']}, Status: {itempc['status']}, frete pago pela cliente.')
            for itemer in er:
                print(f'Cliente: {itemer['cliente']}, Dia: {itemer['dia']}, Mês: {itemer['mes']}, Ano: {itemer['ano']}, Motivo: {itemer['motivo']}, Vendedora: {itemer['vendedora']}, Status: {itemer['status']},frete pago pela loja.')
            menu = int(input("Digite 1 para cadastrar outra troca/devolução.\nDigite qualquer outro número para sair."))
            if menu !=1 :
                print("Programa finalizado!")
                break
    else:
        print("Programa finalizado!")
        break
