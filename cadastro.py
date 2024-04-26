# importar as biliotecas 
# Criar interface Gráfica:
# - Descrição do material 
# - Unidade >> tipo de unidade 
# - Quantidade que vem dentro da unidade 
# Inteligencia da interface gráfica 
  # - Função 
#1) Ler meu Excel para códigos existentes 
#2) qual índice do novo código 
#3) Adicionar os novos códigos ao dataframe Excel
#$) Atualizar o excel  
import tkinter as tk
from tkinter import ttk 
import datetime as dt # quando foi criado 
import pandas as pd 

materiais = pd.read_excel('materiais.xlsx', engine='openpyxl')    # ler o excel
# precisa colocar o engine pra pegar os arquivos xlsx
lista_tipo = ["Galão", "Caixa", "Saco", "Unidade"]
lista_codigos = []

janela = tk.Tk() # Criar uma janela dentro de uma variavel janela 

# Criação da função button

def inserir_codigo():
    #descricao = entry_descricao.get()
    #tipo = comobox_selecionar_tipo.get()
    #quant = entry_quantidade.get()
    # registrar data de criação do código 
    #data_criacao = dt.datetime.now() # dt importada da biblioteca datetime, now pegar exatamente a data e hora registrada
    #data_criacao = data_criacao.strftime("%d/%m/$y %H:%M")
    #codigo = materiais.shape[0]+len(lista_codigos)+1 
    #codigo_str = "COD-{}".format(codigo) # .format pra colocar o valor de uma variavel dentro do codigo
    #lista_codigos.append((codigo_str,descricao,tipo,quant,data_criacao)) # que ele adicione na lista código esse código que acabou de criar 
    # append = tupla estrutura que n permite edição individualmente 
    descricao = entry_descricao.get()
    tipo = comobox_selecionar_tipo.get()
    quant = entry_quantidade.get()
    data_criacao = dt.datetime.now().strftime("%d/%m/%y %H:%M")
    codigo = materiais.shape[0] + len(lista_codigos) + 1 
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))


# Titulo da janela 

janela.title('Ferramenta de cadastro de materias') # nome da janela 

# Descrição / rotulo / espaço vazio 

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4) # pocisionamento da descrição / pdx distanciamento do eixo x 
# sticky='norte,sul,leste,oeste'
# entry espaço para botar o nome desse código
 
entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky= 'nswe' , columnspan=4)

label_tipo_unidade= tk.Label(text="tipo da unidade do Material")
label_tipo_unidade.grid(row=3, column=0,padx=10, pady=10, sticky='nswe', columnspan=2)
# combo box ou lista suspença do excel clicar e escolher os conjutos de materiais 

comobox_selecionar_tipo = ttk.Combobox(values=lista_tipo) # criar a lista que será lida
comobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan= 2)

label_quantidade = tk.Label(text="Quantidade na unidade de material ")
label_quantidade.grid(row=4, column=0,padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Label(text="Quantidade na unidade de material ")
label_quantidade.grid(row=4, column=0,padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky= 'nswe' , columnspan=2)

# botão para validar os dados cadastrados Ex "enviar ou cadastrar "

botao_criar_codigo = tk.Button(text="Criar código", command=inserir_codigo)
#
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

# Função para manuziar o código botão 



janela.mainloop() # deixar existente sempre que fazer alguma coisa 

# Criar um dataframe para receber essa lista de código 
#novo_material = pd.DataFrame(lista_codigos, columns=['Código','Descrição','Tipo','Quantidade','Data Criação'])
#materiais = materiais.append(novo_material, ignore_index=True)# pra ele entrar um em baixo do outro entrando de forma sequencial 
#materiais.to_excel('materiais.xlsx', index=False) #Atualizar o excel # =False pra n criar uma coluna do lado esquerdo dos ídices
novo_material = pd.DataFrame(lista_codigos, columns=['Código','Descrição','Tipo','Quantidade','Data Criação'])
materiais = pd.concat([materiais, novo_material], ignore_index=True)
materiais.to_excel('materiais.xlsx', index=False)

#print(lista_codigos)