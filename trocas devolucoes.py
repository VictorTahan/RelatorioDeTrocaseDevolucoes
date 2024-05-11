from tkinter import *
pc = []
er = []
def registrar_troca_devolucao_paga_cliente():
    cliente_data_motivo1 = {}
    cliente_data_motivo1['cliente'] = cliente_entry.get()
    cliente_data_motivo1['dia'] = int(dia_entry.get())
    cliente_data_motivo1['mes'] = mes_entry.get()
    cliente_data_motivo1['ano'] = int(ano_entry.get())
    cliente_data_motivo1['motivo'] = motivo_entry.get()
    cliente_data_motivo1['vendedora'] = vendedora_entry.get()
    cliente_data_motivo1['status'] = status_var.get()
    pc.append(cliente_data_motivo1)
    update_display()

def registrar_troca_devolucao_paga_loja():
    cliente_data_motivo2 = {}
    cliente_data_motivo2['cliente'] = cliente_entry.get()
    cliente_data_motivo2['dia'] = int(dia_entry.get())
    cliente_data_motivo2['mes'] = mes_entry.get()
    cliente_data_motivo2['ano'] = int(ano_entry.get())
    cliente_data_motivo2['motivo'] = motivo_entry.get()
    cliente_data_motivo2['vendedora'] = vendedora_entry.get()
    cliente_data_motivo2['status'] = status_var.get()
    er.append(cliente_data_motivo2)
    update_display()

def update_display():
    display_text.delete('1.0',END)
    for itempc in pc:
        display_text.insert(END, f"-Cliente: {itempc['cliente']}\n-Dia: {itempc['dia']}\n-Mês: {itempc['mes']}\n-Ano: {itempc['ano']}\n-Motivo: {itempc['motivo']}\n-Vendedora: {itempc['vendedora']}\n-Status: {'Resolvido' if itempc['status'] == 1 else 'Pendente'}\n-frete pago pela cliente.\n")
    for itemer in er:
        display_text.insert(END, f"-Cliente: {itemer['cliente']}\n-Dia: {itemer['dia']}\n-Mês: {itemer['mes']}\n-Ano: {itemer['ano']}\n-Motivo: {itemer['motivo']}\n-Vendedora: {itemer['vendedora']}\n-Status: {'Resolvido' if itemer['status'] == 1 else 'Pendente'}\nfrete pago pela loja.\n")
    
janela = Tk()
janela.title("Cadastro de trocas/devoluções")
#Labels e entradas:
Label(janela, text="Cliente: ").grid(row=0,column=0)
cliente_entry = Entry(janela)
cliente_entry.grid(row=0, column=1)

Label(janela, text="Dia: ").grid(row=1,column=0)
dia_entry = Entry(janela)
dia_entry.grid(row=1,column=1)

Label(janela, text="Mês: ").grid(row=2,column=0)
mes_entry = Entry(janela)
mes_entry.grid(row=2,column=1)

Label(janela, text="Ano: ").grid(row=3,column=0)
ano_entry = Entry(janela)
ano_entry.grid(row=3,column=1)

Label(janela, text="Motivo:").grid(row=4, column=0)
motivo_entry = Entry(janela)
motivo_entry.grid(row=4, column=1)

Label(janela, text="Vendedora:").grid(row=5, column=0)
vendedora_entry = Entry(janela)
vendedora_entry.grid(row=5, column=1)

Label(janela, text="Status:").grid(row=6, column=0)
status_var = IntVar()
Radiobutton(janela, text="Resolvido", variable=status_var, value=1).grid(row=6, column=1)
Radiobutton(janela, text="Pendente", variable=status_var, value=0).grid(row=6, column=2)

#Botões:
Button(janela, text="Registrar Troca/Devolução Paga Cliente", command=registrar_troca_devolucao_paga_cliente).grid(row=7, column=0)
Button(janela, text="Registrar Troca/Devolução Paga Loja", command=registrar_troca_devolucao_paga_loja).grid(row=7, column=1)

#Display de trocas/devoluções
display_text = Text(janela, height=10, width=60)
display_text.grid(row=8, columnspan=3)

janela.mainloop()