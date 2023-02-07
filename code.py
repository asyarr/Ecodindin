
# BIBLIOTECAS
# Download tkinter, pymong, screts, requestes, pandas, numpy, pillow.
from doctest import master
import json
from textwrap import indent
import time
from turtle import bgcolor, color
from tkinter import Scrollbar, font, ttk
import requests
import secrets
import tkinter as tk
from gc import collect
import pymongo
from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
from gettext import find
from tokenize import String
from gc import collect
import pandas
import re
import numpy
import datetime
import pprint
import os
from tkinter import *
from PIL import ImageTk, Image
import PIL.Image
import PIL.ImageTk
from tkinter.messagebox import showinfo
from cgitb import text
import urllib.request
from PIL import Image


# Indicando para onde os dados devem ir:

cluster = pymongo.MongoClient("mongodb+srv://raysa_grippa:1BXi1NRZERxvMQyw@cluster0.jj5qy.mongodb.net/hackaton?retryWrites=true&w=majority")

db = cluster.get_database('EcoDinDin')

collection = db.get_collection('participantes')


def cadastro():
    aba_cadastro = tk.Toplevel()
    aba_cadastro.geometry("450x450")
    aba_cadastro.configure(bg='lightgray')
    aba_cadastro.title('Cadastro')

    # Configurando formato da jenela

    aba_cadastro.resizable(False, False)

    window_height = 500
    window_width = 600

    screen_width = aba_cadastro.winfo_screenwidth()
    screen_height = aba_cadastro.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    aba_cadastro.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


    # mudando icone da aba 

    urllib.request.urlretrieve(
      'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
       "icon.png")

    icon = PhotoImage(file = 'icon.png')
    aba_cadastro.iconphoto(False, icon)

    # Logo 

    logo = tk.Label(aba_cadastro, text="Eco DinDin", bg='#005F40', fg='white', font='BahnschriftLightCondensed 18 bold',  justify = 'left', width= 42, height= 2)
    logo.place(relx=0, rely=0)

    # Imagem

    urllib.request.urlretrieve(
        'https://lh3.googleusercontent.com/pw/AL9nZEU1Ov1y6IvmXDWxPL2vXPWNjeahjiHVR6pvybkGm0XKi2ZL3gb2MSzGmrzRBf0q0nISdoehHnyJC_oxJQa6JuOUxljpxGt-ezt-dLTG959srYlwey5w1FsMb2Om1tSSXahxx8Ykoqd6PkKXHOQ4YR5O=w224-h302-no?authuser=2',
        "interrogação.png")
    imagem3 = "interrogação.png"
    frame = Frame(aba_cadastro, width=300, height=200)
    frame.pack()
    frame.place(anchor='center', relx=0.75, rely=0.5)
    image = PIL.Image.open(f'{imagem3}')
    resize_image = image.resize((202,280))
    img = PIL.ImageTk.PhotoImage(resize_image)
    label = Label(frame, image = img, bg='lightgray')
    label.photo = img
    label.pack()


    # Iniciando o formulário:

    mensagem = tk.Label(aba_cadastro, text = "Quem esta se cadastrando?", justify= 'center', bg='lightgray', font='BahnschriftLight 12')
    mensagem.place_configure(relx=0.15, rely=0.2)

    
    def cadastro1():
        aba_cadastro1 = tk.Toplevel()
        aba_cadastro1.geometry("450x450")
        aba_cadastro1.configure(bg='lightgray')
        aba_cadastro1.title('Cadastro')

        # Configurando formato da jenela

        aba_cadastro1.resizable(False, False)

        window_height = 500
        window_width = 600

        screen_width = aba_cadastro1.winfo_screenwidth()
        screen_height = aba_cadastro1.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        aba_cadastro1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # mudando icone da aba 

        urllib.request.urlretrieve(
          'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
           "icon.png")

        icon = PhotoImage(file = 'icon.png')
        aba_cadastro1.iconphoto(False, icon)

        # Logo

        logo = tk.Label(aba_cadastro1, text="Eco DinDin", bg='#005F40', fg='white', font='BahnschriftLightCondensed 18 bold',  justify = 'left', width= 42, height= 2)
        logo.place(relx=0, rely=0)

        # Informações de cadastro:

        mensagem1 = tk.Label(aba_cadastro1, text = "Informe seus dados:", bg='lightgray', justify= 'center',  font='BahnschriftLight 12')
        mensagem1.place_configure(relx= 0.1, rely= 0.15)

        nome = tk.Label(aba_cadastro1, text = "Nome: ", bg='lightgray',  font='BahnschriftLight 10')
        nome.place_configure(relx= 0.35, rely= 0.23)

        campo_nome = tk.Entry(aba_cadastro1)
        campo_nome.place_configure(relx= 0.45, rely= 0.23)

        sobrenome = tk.Label(aba_cadastro1, text = "Sobrenome: ", bg='lightgray',  font='BahnschriftLight 10')
        sobrenome.place_configure(relx= 0.3, rely= 0.33) 

        campo_sobrenome = tk.Entry(aba_cadastro1)
        campo_sobrenome.place_configure(relx= 0.45, rely= 0.33) 

        idade = tk.Label(aba_cadastro1, text = "Idade: ", bg='lightgray',  font='BahnschriftLight 10')
        idade.place_configure(relx= 0.35, rely= 0.43) 

        campo_idade = tk.Entry(aba_cadastro1)
        campo_idade.place_configure(relx= 0.45, rely= 0.43) 

        CPF = tk.Label(aba_cadastro1, text = "CPF: ", bg='lightgray',  font='BahnschriftLight 10')
        CPF.place_configure(relx= 0.35, rely= 0.53) 

        campo_CPF = tk.Entry(aba_cadastro1)
        campo_CPF.place_configure(relx= 0.45, rely= 0.53) 
        campo_CPF.size()

        CEP = tk.Label(aba_cadastro1, text = "CEP: ", bg='lightgray',  font='BahnschriftLight 10')
        CEP.place_configure(relx= 0.35, rely= 0.63) 

        campo_CEP = tk.Entry(aba_cadastro1)
        campo_CEP.place_configure(relx= 0.45, rely= 0.63) 

        senha = tk.Label(aba_cadastro1, text = "Nova senha: ", bg='lightgray',  font='BahnschriftLight 10')
        senha.place_configure(relx= 0.3, rely= 0.73) 

        campo_senha = tk.Entry(aba_cadastro1, show="*")
        campo_senha.place_configure(relx= 0.45, rely= 0.73) 

        def validacao():
            cpf = campo_CPF.get()
            cpf_errado = tk.Label(aba_cadastro1, text="O CPF deve conter 11 dígitos.", bg='lightgray',  font='BahnschriftLight 10')

            if len(cpf) != 11:
                cpf_errado.place_configure(relx= 0.35, rely= 0.58)

            else:

                # Vrificando se o CPF já esta cadastrado:

                cpf_existe = collection.find_one({'CPF': str(cpf)})

                if cpf_existe:
                    cpf_existente = tk.Label(aba_cadastro1, text="CPF cadastrado", bg='lightgray',  font='BahnschriftLight 10')
                    cpf_existente.place_configure(relx= 0.7, rely= 0.53)

                else:
                    cep = campo_CEP.get()

                    cep_errado = tk.Label(aba_cadastro1, text="O CEP deve conter 8 dígitos.", bg='lightgray',  font='BahnschriftLight 10')

                    if len(cep) != 8:
                        cep_errado.place_configure(relx= 0.35, rely= 0.68)

                    # Validando o CEP

                    else:
                        resposta = requests.get(f'https://viacep.com.br/ws/{int(cep)}/json/')

                        if resposta.status_code == 200:
                            dado = resposta.json()

                            if "erro" in dado:
                                erro = tk.Label(aba_cadastro1, text="CEP inválido", bg='lightgray',  font='BahnschriftLight 10')
                                erro.place_configure(relx= 0.7, rely= 0.63)

                            else:
                                rua = dado['logradouro']
                                print(rua)
                                bairro = dado['bairro']
                                print(bairro)
                                cidade = dado['localidade']
                                print(cidade)
                                estado = dado['uf']
                                print(estado)

                                if len(campo_senha.get()) <= 7:

                                    erro2 = tk.Label(aba_cadastro1, text="A senha deve conter no min. 8 dígitos", bg='lightgray',  font='BahnschriftLight 10')
                                    erro2.place_configure(relx= 0.3, rely= 0.78)

                                else:
                                    def confima_clica():

                                        print('Cadastro efetuado')

                                        cadastro_concluido = tk.Label(janela, text="Cadastro efetudo, faça o login para acessar seu perfil.", bg='lightgray',  font='BahnschriftLight 10')
                                        cadastro_concluido.place(relx= 0.1, rely= 0.9)

                                        # Captando os dados do contribuidor:

                                        contribuidor = {}
                                        contribuidor['Nome'] = str(campo_nome.get())
                                        contribuidor['Sobrenome'] = str(campo_sobrenome.get())
                                        contribuidor['Idade'] = str(campo_idade.get())
                                        contribuidor['CPF'] = str(campo_CPF.get())
                                        contribuidor['CEP'] = str(campo_CEP.get())
                                        contribuidor['Cidade'] = cidade
                                        contribuidor['Estado'] = estado
                                        contribuidor['Senha'] = str(campo_senha.get())
                                        contribuidor['Classe'] = 'Usuário'
                                        contribuidor['Pontos'] = 0

                                        # Inserir dado na collection:

                                        collection.insert_one(contribuidor)

                                        aba_cadastro.destroy()
                                        aba_cadastro1.destroy()

                                    bt = tk.Button(aba_cadastro1, text="Cadastrar", command=confima_clica, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2, font='BahnschriftLight 10')
                                    bt.place_configure(relx= 0.43, rely= 0.85)


        bt_validacao = tk.Button(aba_cadastro1, text="Validar", command=validacao, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 8, height= 1, font='BahnschriftLight 10')
        bt_validacao.place_configure(relx= 0.7, rely= 0.72) 

    bt_cadastro_usuario = tk.Button(aba_cadastro, text="Usuário", command=cadastro1, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2, font='BahnschriftLight 10')
    bt_cadastro_usuario.place_configure(relx= 0.25, rely= 0.35) 

    def cadastro2():
        aba_cadastro2 = tk.Toplevel()
        aba_cadastro2.geometry("450x450")
        aba_cadastro2.configure(bg='lightgray')
        aba_cadastro2.title('Cadastro')

        # Configurando formato da jenela

        aba_cadastro2.resizable(False, False)

        window_height = 500
        window_width = 600

        screen_width = aba_cadastro2.winfo_screenwidth()
        screen_height = aba_cadastro2.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        aba_cadastro2.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # mudando icone da aba 

        urllib.request.urlretrieve(
          'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
           "icon.png")

        icon = PhotoImage(file = 'icon.png')
        aba_cadastro2.iconphoto(False, icon)


        # Logo

        logo = tk.Label(aba_cadastro2, text="Eco DinDin", bg='#005F40', fg='white', font='BahnschriftLightCondensed 18 bold',  justify = 'left', width= 42, height= 2)
        logo.place(relx=0, rely=0)

        # Iniciando o formulário

        mensagem2 = tk.Label(aba_cadastro2, text = "Informe seus dados:", bg='lightgray', justify= 'center', font='BahnschriftLight 12')
        mensagem2.place_configure(relx= 0.1, rely= 0.14)

        nome = tk.Label(aba_cadastro2, text = "Nome: ", bg='lightgray', font='BahnschriftLight 10')
        nome.place_configure(relx= 0.35, rely= 0.22)

        campo_nome = tk.Entry(aba_cadastro2)
        campo_nome.place_configure(relx= 0.45, rely= 0.22)

        sobrenome = tk.Label(aba_cadastro2, text = "Sobrenome: ", bg='lightgray',  font='BahnschriftLight 10')
        sobrenome.place_configure(relx= 0.31, rely= 0.31) 

        campo_sobrenome = tk.Entry(aba_cadastro2)
        campo_sobrenome.place_configure(relx= 0.45, rely= 0.31) 

        idade = tk.Label(aba_cadastro2, text = "Idade: ", bg='lightgray',  font='BahnschriftLight 10')
        idade.place_configure(relx= 0.35, rely= 0.4) 

        campo_idade = tk.Entry(aba_cadastro2)
        campo_idade.place_configure(relx= 0.45, rely= 0.4) 

        CPF = tk.Label(aba_cadastro2, text = "CPF: ", bg='lightgray',  font='BahnschriftLight 10')
        CPF.place_configure(relx= 0.35, rely= 0.49) 

        campo_CPF = tk.Entry(aba_cadastro2)
        campo_CPF.place_configure(relx= 0.45, rely= 0.49) 
        campo_CPF.size()

        CEP = tk.Label(aba_cadastro2, text = "CEP da Recicladora: ", bg='lightgray',  font='BahnschriftLight 10')
        CEP.place_configure(relx= 0.23, rely= 0.58) 

        campo_CEP = tk.Entry(aba_cadastro2)
        campo_CEP.place_configure(relx= 0.45, rely= 0.58) 

        numero = tk.Label(aba_cadastro2, text = "Número: ", bg='lightgray',  font='BahnschriftLight 10')
        numero.place_configure(relx= 0.33, rely= 0.68) 

        campo_numero = tk.Entry(aba_cadastro2)
        campo_numero.place_configure(relx= 0.45, rely= 0.68) 

        senha = tk.Label(aba_cadastro2, text = "Nova senha: ", bg='lightgray',  font='BahnschriftLight 10')
        senha.place_configure(relx= 0.3, rely= 0.77) 

        campo_senha = tk.Entry(aba_cadastro2, show="*")
        campo_senha.place_configure(relx= 0.45, rely= 0.77)

        def validacao():
            cpf = campo_CPF.get()
            cpf_errado = tk.Label(aba_cadastro2, text="Erro, o CPF deve conter 11 dígitos.", bg='lightgray',  font='BahnschriftLight 10')

            if len(cpf) != 11:
                cpf_errado.place_configure(relx= 0.35, rely= 0.535)

            else: 

                # Verificando se o CPF já está cadastrado:

                cpf_existe = collection.find_one({'CPF': str(cpf)})

                if cpf_existe:
                    cpf_existente = tk.Label(aba_cadastro2, text="CPF cadastrado", bg='lightgray',  font='BahnschriftLight 10')
                    cpf_existente.place_configure(relx= 0.7, rely= 0.49) 

                else:
                    cep = campo_CEP.get()

                    cep_errado = tk.Label(aba_cadastro2, text="Erro, o CEP deve conter 8 dígitos.", bg='lightgray',  font='BahnschriftLight 10')

                    if len(cep) != 8:
                        cep_errado.place_configure(relx= 0.35, rely= 0.63)

                    else:

                        # Validando CEP

                        resposta = requests.get(f'https://viacep.com.br/ws/{int(cep)}/json/')

                        if resposta.status_code == 200:
                            dado = resposta.json()

                            if "erro" in dado:
                                erro = tk.Label(aba_cadastro2, text="CEP inválido", bg='lightgray',  font='BahnschriftLight 10')
                                erro.place_configure(relx= 0.7, rely= 0.58)

                            else:
                                rua = dado['logradouro']
                                print(rua)
                                bairro = dado['bairro']
                                print(bairro)
                                cidade = dado['localidade']
                                print(cidade)
                                estado = dado['uf']
                                print(estado)

                                if len(campo_numero.get()) == 0:
                                    erro2 = tk.Label(aba_cadastro2, text="Informe o número do estabelecimento", bg='lightgray',  font='BahnschriftLight 10')
                                    erro2.place_configure(relx= 0.3, rely= 0.72)

                                else:
                                    if len(campo_senha.get()) <= 7:
                                        erro2 = tk.Label(aba_cadastro2, text="A senha deve conter no min. 8 dígitos", bg='lightgray',  font='BahnschriftLight 10')
                                        erro2.place_configure(relx= 0.32, rely= 0.82)

                                    else:
                                        def confima_clica():

                                            print('Cadastro efetuado')

                                            cadastro_concluido = tk.Label(janela, text="Cadastro efetudo, faça o login para acessar seu perfil.", bg='lightgray',  font='BahnschriftLight 10')
                                            cadastro_concluido.place(relx= 0.1, rely= 0.9)

                                            # Captando os dados do contribuidor:

                                            contribuidor = {}
                                            contribuidor['Nome'] = str(campo_nome.get())
                                            contribuidor['Sobrenome'] = str(campo_sobrenome.get())
                                            contribuidor['Idade'] = str(campo_idade.get())
                                            contribuidor['CPF'] = str(campo_CPF.get())
                                            contribuidor['CEP'] = str(campo_CEP.get())
                                            contribuidor['Estado'] = estado
                                            contribuidor['Cidade'] = cidade 
                                            contribuidor['Bairro'] = bairro 
                                            contribuidor['Rua'] = rua
                                            contribuidor['Numero'] = str(campo_numero.get())
                                            contribuidor['Senha'] = str(campo_senha.get())
                                            contribuidor['Classe'] = 'Recicladora'

                                            # Inserir dado na collection:

                                            collection.insert_one(contribuidor)

                                            aba_cadastro.destroy()
                                            aba_cadastro2.destroy()

                                        bt = tk.Button(aba_cadastro2, text="Cadastrar", command=confima_clica, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2,  font='BahnschriftLight 10')
                                        bt.place_configure(relx= 0.43, rely= 0.89)


        bt_validacao = tk.Button(aba_cadastro2, text="Validar", command=validacao, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 8, height= 1,  font='BahnschriftLight 10')
        bt_validacao.place_configure(relx= 0.7, rely= 0.76) 

    bt_cadastro_usuario = tk.Button(aba_cadastro, text="Recicladora", command=cadastro2,bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2,  font='BahnschriftLight 10')
    bt_cadastro_usuario.place_configure(relx= 0.25, rely= 0.5) 


    def cadastro3():
        aba_cadastro3 = tk.Toplevel()
        aba_cadastro3.geometry("450x450")
        aba_cadastro3.configure(bg='lightgray')
        aba_cadastro3.title('Cadastro')

        # Configurando formato da jenela

        aba_cadastro3.resizable(False, False)

        window_height = 500
        window_width = 600

        screen_width = aba_cadastro3.winfo_screenwidth()
        screen_height = aba_cadastro3.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        aba_cadastro3.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # mudando icone da aba 

        urllib.request.urlretrieve(
          'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
           "icon.png")

        icon = PhotoImage(file = 'icon.png')
        aba_cadastro3.iconphoto(False, icon)

        # Logo

        logo = tk.Label(aba_cadastro3, text="Eco DinDin", bg='#005F40', fg='white', font='BahnschriftLightCondensed 18 bold',  justify = 'left', width= 42, height= 2)
        logo.place(relx=0, rely=0)

        # Iniciando formulário

        mensagem2 = tk.Label(aba_cadastro3, text = "Informe seus dados:", bg='lightgray', justify= 'center', font='BahnschriftLight 12')
        mensagem2.place_configure(relx= 0.1, rely= 0.14)

        nome = tk.Label(aba_cadastro3, text = "Nome do supermercado: ", bg='lightgray', font='BahnschriftLight 10')
        nome.place_configure(relx= 0.2, rely= 0.22)

        campo_nome = tk.Entry(aba_cadastro3)
        campo_nome.place_configure(relx= 0.45, rely= 0.22)

        CNPJ = tk.Label(aba_cadastro3, text = "CNPJ: ", bg='lightgray',  font='BahnschriftLight 10')
        CNPJ.place_configure(relx= 0.35, rely= 0.32) 

        campo_CNPJ = tk.Entry(aba_cadastro3)
        campo_CNPJ.place_configure(relx= 0.45, rely= 0.32) 
        campo_CNPJ.size()

        CPF = tk.Label(aba_cadastro3, text = "CPF de um representante: ", bg='lightgray',  font='BahnschriftLight 10')
        CPF.place_configure(relx= 0.17, rely= 0.42) 

        campo_CPF = tk.Entry(aba_cadastro3)
        campo_CPF.place_configure(relx= 0.45, rely= 0.42) 

        CEP = tk.Label(aba_cadastro3, text = "CEP: ", bg='lightgray',  font='BahnschriftLight 10')
        CEP.place_configure(relx= 0.35, rely= 0.52) 

        campo_CEP = tk.Entry(aba_cadastro3)
        campo_CEP.place_configure(relx= 0.45, rely= 0.52) 

        numero = tk.Label(aba_cadastro3, text = "Número: ", bg='lightgray',  font='BahnschriftLight 10')
        numero.place_configure(relx= 0.33, rely= 0.62) 

        campo_numero = tk.Entry(aba_cadastro3)
        campo_numero.place_configure(relx= 0.45, rely= 0.62) 

        senha = tk.Label(aba_cadastro3, text = "Nova senha: ", bg='lightgray',  font='BahnschriftLight 10')
        senha.place_configure(relx= 0.3, rely= 0.72) 

        campo_senha = tk.Entry(aba_cadastro3, show="*")
        campo_senha.place_configure(relx= 0.45, rely= 0.72) 

        def validacao():
            cpf = campo_CPF.get()
            cpf_errado = tk.Label(aba_cadastro3, text="Erro, o CPF deve conter 11 dígitos.", bg='lightgray',  font='BahnschriftLight 10')

            if len(cpf) != 11:
                cpf_errado.place_configure(relx= 0.35, rely= 0.47) 

            else:

                # Verificando se o CPF já está cadastrado:

                cpf_existe = collection.find_one({'CPF': str(cpf)})

                if cpf_existe:
                    cpf_existente = tk.Label(aba_cadastro3, text="CPF cadastrado", bg='lightgray',  font='BahnschriftLight 10')
                    cpf_existente.place_configure(relx= 0.7, rely= 0.42) 

                else:
                    cep = campo_CEP.get()
                    cep_errado = tk.Label(aba_cadastro3, text="Erro, o CEP deve conter 8 dígitos.", bg='lightgray',  font='BahnschriftLight 10')

                    if len(cep) != 8:
                        cep_errado.place_configure(relx= 0.35, rely= 0.57)

                    else:

                        # Validando CEP

                        resposta = requests.get(f'https://viacep.com.br/ws/{int(cep)}/json/')

                        if resposta.status_code == 200:
                            dado = resposta.json()

                            if "erro" in dado:
                                erro = tk.Label(aba_cadastro3, text="CEP inválido", bg='lightgray',  font='BahnschriftLight 10')
                                erro.place_configure(relx= 0.7, rely= 0.52)

                            else:
                                rua = dado['logradouro']
                                print(rua)
                                bairro = dado['bairro']
                                print(bairro)
                                cidade = dado['localidade']
                                print(cidade)
                                estado = dado['uf']
                                print(estado)

                                if len(campo_numero.get()) == 0:
                                    erro2 = tk.Label(aba_cadastro3, text="Informe o número do estabelecimento", bg='lightgray',  font='BahnschriftLight 10')
                                    erro2.place_configure(relx= 0.33, rely= 0.66)

                                else:
                                    if len(campo_senha.get()) <= 7:
                                        erro2 = tk.Label(aba_cadastro3, text="A senha deve conter no min. 8 dígitos", bg='lightgray',  font='BahnschriftLight 10')
                                        erro2.place_configure(relx= 0.32, rely= 0.77)

                                    else:

                                        def confima_clica():

                                            print('Cadastro efetuado')

                                            cadastro_concluido = tk.Label(janela, text="Cadastro efetudo, faça o login para acessar seu perfil.", bg='lightgray',  font='BahnschriftLight 10')
                                            cadastro_concluido.place(relx= 0.1, rely= 0.9)

                                            # Captando os dados do contribuidor:

                                            contribuidor = {}
                                            contribuidor['Nome'] = str(campo_nome.get())
                                            contribuidor['CPF'] = str(campo_CPF.get())
                                            contribuidor['CEP'] = str(campo_CEP.get())
                                            contribuidor['Estado'] = estado
                                            contribuidor['Cidade'] = cidade
                                            contribuidor['Bairro'] = bairro
                                            contribuidor['Rua'] = rua     
                                            contribuidor['Numero'] = str(campo_numero.get())                              
                                            contribuidor['Senha'] = str(campo_senha.get())
                                            contribuidor['Classe'] = 'Mercado'

                                            # Inserir dado na collection:

                                            collection.insert_one(contribuidor)

                                            aba_cadastro.destroy()
                                            aba_cadastro3.destroy()

                                    bt = tk.Button(aba_cadastro3, text="Cadastrar", command=confima_clica, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2,  font='BahnschriftLight 10')
                                    bt.place_configure(relx= 0.43, rely= 0.85)


        bt_validacao = tk.Button(aba_cadastro3, text="Validar", command=validacao, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 8, height= 1,  font='BahnschriftLight 10')
        bt_validacao.place_configure(relx= 0.7, rely= 0.71) 

    bt_cadastro_usuario = tk.Button(aba_cadastro, text="Mercado", command=cadastro3,bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2,  font='BahnschriftLight 10')
    bt_cadastro_usuario.place_configure(relx= 0.25, rely= 0.65) 




def login():  
    aba_login = tk.Toplevel()
    aba_login.geometry("450x450")
    aba_login.configure(bg='lightgray')
    aba_login.title('Login')

    # Configurando o formato da janela

    aba_login.resizable(False, False)

    window_height = 500
    window_width = 600

    screen_width = aba_login.winfo_screenwidth()
    screen_height = aba_login.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    aba_login.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # mudando icone da aba 

    urllib.request.urlretrieve(
      'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
       "icon.png")

    icon = PhotoImage(file = 'icon.png')
    aba_login.iconphoto(False, icon)

    # Logo

    logo = tk.Label(aba_login, text="Eco DinDin", bg='#005F40', fg='white', font='BahnschriftLightCondensed 18 bold',  justify = 'left', width= 42, height= 2)
    logo.place(relx=0, rely=0)
    
    # Imagem

    urllib.request.urlretrieve(
        'https://lh3.googleusercontent.com/pw/AL9nZEUzU48rOryyUCvU3s1I3si8XxR9rZi10lPeEODRFAT4OWHta2F-mavojjK2u1s4qM4nIrfm6Z414YJ_b0PUwRuv1eFAQzsMBq5FOVqCw84-PAgF6PRkzwXCQIAkGppXYJEHEd78JtG_JOBQ657hzWOt=w458-h570-no?authuser=2',
        "arvore.png")

    imagem2 = "arvore.png"
    frame = Frame(aba_login, width=458, height=570)
    frame.pack()
    frame.place(anchor='center', relx=0.7, rely=0.55)
    image = PIL.Image.open(f"{imagem2}")
    resize_image = image.resize((250,311))
    img = PIL.ImageTk.PhotoImage(resize_image)
    label = Label(frame, image = img, bg='lightgray')
    label.photo = img
    label.pack()

    # Acesso ao perfil
    
    acesso = tk.Label(aba_login, text = "Digite seu CPF e sua senha:", bg='lightgray', justify= 'center', font='BahnschriftLightCondensed 12')
    acesso.place_configure(relx= 0.05, rely= 0.25)

    cpf_login = tk.Label(aba_login, text = "CPF: ", bg='lightgray', font='BahnschriftLightCondensed 12')
    cpf_login.place_configure(relx= 0.1, rely= 0.4)

    campo_cpf_login = tk.Entry(aba_login)
    campo_cpf_login.place_configure(relx= 0.2, rely= 0.4)

    senha_login = tk.Label(aba_login, text = "Senha: ", bg='lightgray', font='BahnschriftLightCondensed 12')
    senha_login.place_configure(relx= 0.1, rely= 0.55)

    campo_senha_login = tk.Entry(aba_login, show="*")
    campo_senha_login.place_configure(relx= 0.2, rely= 0.55)

    def logando():

        # Procurando CPF no banco de dados

        logando_cpf = collection.find_one({'CPF': str(campo_cpf_login.get())})

        if logando_cpf:
            print(logando_cpf)

        else:
            cpf_login_erro = tk.Label(aba_login, text='CPF não cadastrado', bg='lightgray', font='BahnschriftLightCondensed 10')
            cpf_login_erro.place_configure(relx= 0.15, rely= 0.45)

        if str(campo_senha_login.get()) != logando_cpf['Senha']:
            senha_login_erro = tk.Label(aba_login, text='Senha incorreta', bg='lightgray', font='BahnschriftLightCondensed 10')
            senha_login_erro.place_configure(relx= 0.15, rely= 0.6)

        else:

            # Abrindo o perfil:

            perfil = tk.Toplevel()
            perfil.geometry("450x450")
            perfil.title('Perfil')
            perfil.configure(bg='lightgray')

            # Configurando o formato da janela

            perfil.resizable(False, False)

            window_height = 500
            window_width = 600

            screen_width = perfil.winfo_screenwidth()
            screen_height = perfil.winfo_screenheight()

            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))

            perfil.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

            # Logo

            logo = tk.Label(perfil, text="Eco DinDin", bg='#005F40', fg='white', font='BahnschriftLightCondensed 18 bold',  justify = 'left', width= 42, height= 2)
            logo.place(relx=0, rely=0)

            aba_login.destroy()

            # Perfil usuário 1: Pessoas que vão trocar materias recicláveis por pontos

            if logando_cpf['Classe'] == 'Usuário':
                
                # mudando icone da aba 

                urllib.request.urlretrieve(
                  'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
                   "icon.png")

                icon = PhotoImage(file = 'icon.png')
                perfil.iconphoto(False, icon)

                # Boas Vindas

                bv = tk.Label(perfil, text="""Bem-Vindo ao seu perfil. Aqui você pode acessar as informações de pontos de reciclagem e mercados
                parceiros, além de poder checar a sua quantidade de pontos.""", height= 5, font='BahnschriftLight 10')
                bv.place(relx = 0, rely = 0.1)

                # Nome e quantidade de pontos

                nome = tk.Label(perfil, text= "Nome:", bg="lightgray", font='BahnschriftLight 10')
                nome.place(relx = 0.1, rely=0.3)

                nome_usuario = tk.Label(perfil, text= f"{str(logando_cpf['Nome'])} {str(logando_cpf['Sobrenome'])}", font='BahnschriftLight 10')
                nome_usuario.place(relx = 0.2, rely=0.3)

                pontos_text = tk.Label(perfil, text= "Pontos:", bg="lightgray", font='BahnschriftLight 10')
                pontos_text.place(relx = 0.1, rely = 0.35)

                pontos = tk.Label(perfil, text= str(logando_cpf['Pontos']), font='BahnschriftLight 10')
                pontos.place(relx = 0.2, rely = 0.35)

                # Tabela com os endereços dos mercados

                columns = ('mercados_d', )

                tree = ttk.Treeview(perfil, columns=columns, show='headings')

                tree.heading('mercados_d', text='Mercados disponíveis')
                tree.column('mercados_d', width= 250, anchor=tk.CENTER)
                

                mercados = []
                for x in collection.find({'Classe':'Mercado'},{'_id':0, 'Senha':0, 'CPF':0, 'CEP':0, 'Classe':0}):
                    mercados.append(x)

                for mercado in mercados:
                    nome = mercado['Nome']
                    cidade = mercado['Cidade']
                    bairro = mercado['Bairro']
                    rua = mercado['Rua']
                    numero = f"nº {mercado['Numero']}"

                    endereco_total = f"{nome} - {cidade} , {bairro} , {rua}, {numero}"

                    tree.insert('', tk.END, values=[endereco_total])

                def item_selected():

                    for selected_item in tree.selection():
                        item = tree.item(selected_item)
                        record = item['values']

                        showinfo(title='information', massage=','.join(record))

                tree.bind('<<TreeviewSelect>>', item_selected)

                tree.grid(row=0, column=0, sticky='nsew')
                tree.place(relx= 0.06, rely=0.4, relwidth=0.9, relheight=0.25)

                # Barra de rolagem

                scrollbar = ttk.Scrollbar(perfil, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns', ipady=300)
                scrollbar.place(relx= 0.03, rely=0.4, relwidth=0.03, relheight=0.25)

                # Tabela com os endereços das recicladoras

                columns2 = ('recicladoras_d', )

                tree = ttk.Treeview(perfil, columns=columns2, show='headings')

                tree.heading('recicladoras_d', text='Recicladoras disponíveis')
                tree.column('recicladoras_d', width= 250, anchor=tk.CENTER)

                recicladoras = []
                for x in collection.find({'Classe':'Recicladora'},{'_id':0, 'Nome': 0 , 'Senha':0, 'CPF':0, 'CEP':0, 'Classe':0}):
                    recicladoras.append(x)

                for recicladora in recicladoras:
                    cidade = recicladora['Cidade']
                    bairro = recicladora['Bairro']
                    rua = recicladora['Rua']
                    numero = f"nº {recicladora['Numero']}"

                    endereco_total = f"{cidade}, {bairro}, {rua}, {numero}"

                    tree.insert('', tk.END, values=[endereco_total])

                def item_selected():

                    for selected_item in tree.selection():
                        item = tree.item(selected_item)
                        record = item['values']

                        showinfo(title='information', massage=','.join(record))

                tree.bind('<<TreeviewSelect>>', item_selected)

                tree.grid(row=0, column=0, sticky='nsew')
                tree.place(relx= 0.06, rely=0.7, relwidth=0.9, relheight=0.25)

                # Barra de rolagem

                scrollbar = ttk.Scrollbar(perfil, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns', ipady=300)
                scrollbar.place(relx= 0.03, rely=0.7, relwidth=0.03, relheight=0.25)

            # Perfil usuário 2: Pessoas que trabalham nas recicladoras

            if logando_cpf['Classe'] == 'Recicladora':

                # Imagem

                urllib.request.urlretrieve(
                  'https://lh3.googleusercontent.com/pw/AL9nZEXbeQylSG4jElUmJgmPSP10uEWhqrPmPZjKUc3253kUYKK7d9tVpqsU31gmOG58MjZkm550-EwvLS9BwS95b5yE-eciYXPlqe3SxH-fI3kAHbQc7kmHgAmwFWlliqlXVPtws6a_YiRaVSzZSz0T4efx=w410-h285-no?authuser=2',
                   "grupofeliz.png")
                imagem4 = "grupofeliz.png"
                frame = Frame(perfil, width=600, height=400)
                frame.pack()
                frame.place(anchor='center', relx=0.5, rely=0.75)
                image = PIL.Image.open(f"{imagem4}")
                resize_image = image.resize((285,198))
                img = PIL.ImageTk.PhotoImage(resize_image)
                label = Label(frame, image = img, bg='lightgray')
                label.photo = img
                label.pack()

                # mudando icone da aba 
    
                urllib.request.urlretrieve(
                  'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
                   "icon.png")

                icon = PhotoImage(file = 'icon.png')
                perfil.iconphoto(False, icon)
                
                # Boas Vindas

                bv = tk.Label(perfil, text="""Bem-Vindo ao perfil da recicladora. Aqui é possível enviar pontuações aos usuários que reciclaram 
                em sua empresa.""", font='BahnschriftLight 10', width= 78, height=4)
                bv.place(relx=-0.01, rely=0.1)

                # Evio de pontos para os usuários 1

                cpf_usuário = tk.Label(perfil, text = "Digite o CPF do cliente que reciclou:", bg="lightgray", font='BahnschriftLight 10')
                cpf_usuário.place(relx=0.1, rely= 0.35)
                campo_cpf_usuário = tk.Entry(perfil)
                campo_cpf_usuário.place(relx=0.5, rely = 0.35)

                envio_pontos = tk.Label(perfil, text = "Digite a pontuação a ser acrescentada:", bg="lightgray", font='BahnschriftLight 10')
                envio_pontos.place(relx=0.1, rely=0.45)
                campo_envio_pontos = tk.Entry(perfil)
                campo_envio_pontos.place(relx = 0.5, rely=0.45)

                def mudança_pontos():

                    dados_pontos= re.split(r":|}", (str(collection.find_one({'Classe':'Usuário','CPF':campo_cpf_usuário.get()},{'_id':0, 'Pontos':1})))) 
                    k = float(dados_pontos[1])
                    n = float(campo_envio_pontos.get())

                    nova_pontuação = collection.update_many({"CPF": str(campo_cpf_usuário.get())},{"$set":{"Pontos": k + n}, "$currentDate":{"lastModified":True}})
                    
                    enviado = tk.Label(perfil, text="Pontos enviados", bg='lightgray',  font='BahnschriftLight 10')
                    enviado.place_configure(relx= 0.2, rely= 0.5) 

                bt_enviar = tk.Button(perfil, text="Enviar",command=mudança_pontos, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 8, height= 1, font='BahnschriftLight 10')
                bt_enviar.place(relx = 0.8, rely=0.4)

            # Perfil usuário 3: Mercados

            if logando_cpf['Classe'] == 'Mercado':

                # mudando icone da aba 
    
                urllib.request.urlretrieve(
                  'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
                   "icon.png")

                icon = PhotoImage(file = 'icon.png')
                perfil.iconphoto(False, icon)

                # Imagem

                urllib.request.urlretrieve(
                  'https://lh3.googleusercontent.com/pw/AL9nZEVPwa2lC-h85zCwwXTpjIzLp13R-fA6zTZTGJAIzNRoKSpDfOQvERmE7rnhmbRM1DKNdBbRphvau2FdIriRH1rLevQEhG7U_YS9TzOpWcTtWIl9ah8J_azs2jCgjvxThxa0GJpGSlEVLa4Fe66lXmD1=w614-h562-no?authuser=2',
                   "ecofriendly.png")
                imagem5 = "ecofriendly.png"
                frame = Frame(perfil, width=535, height=489)
                frame.pack()
                frame.place(anchor='center', relx=0.5, rely=0.73)
                image = PIL.Image.open(f"{imagem5}")
                resize_image = image.resize((250,229))
                img = PIL.ImageTk.PhotoImage(resize_image)
                label = Label(frame, image = img, bg='lightgray')
                label.photo = img
                label.pack()

                # Boas vindas

                bv = tk.Label(perfil, text="""Bem-Vindo ao perfil do Mercado.
Aqui você pode retirar dos usuários os pontos que foram trocados por produtos.""", font='BahnschriftLight 10', width= 78, height=4)
                bv.place(relx=0, rely=0.1)

                dados_text = tk.StringVar()
                dados_text.set(str(logando_cpf))

                # Retirada de pontos que estão sendo trocados por produtos


                cpf_usuário2 = tk.Label(perfil, text = "Digite o CPF do cliente:", bg="lightgray", font='BahnschriftLight 10')
                cpf_usuário2.place(relx=0.1, rely= 0.3)
                campo_cpf_usuário2 = tk.Entry(perfil)
                campo_cpf_usuário2.place(relx=0.5, rely = 0.3)

                retiro_pontos = tk.Label(perfil, text = "Digite a pontuação a ser retirada:", bg="lightgray", font='BahnschriftLight 10')
                retiro_pontos.place(relx=0.1, rely=0.4)
                campo_retiro_pontos = tk.Entry(perfil)
                campo_retiro_pontos.place(relx = 0.5, rely=0.4)

                def mudança_pontos_mercado():

                    dados_pontos2= re.split(r":|}", (str(collection.find_one({'Classe':'Usuário','CPF':campo_cpf_usuário2.get()},{'_id':0, 'Pontos':1})))) 
                    p = float(dados_pontos2[1])
                    l = float(campo_retiro_pontos.get()) 

                    nova_pontuação_mercado = collection.update_many({"CPF": str(campo_cpf_usuário2.get())},{"$set":{"Pontos": p - l}, "$currentDate":{"lastModified":True}})
                    
                    retirado = tk.Label(perfil, text="Pontos retirados", bg='lightgray',  font='BahnschriftLight 10')
                    retirado.place_configure(relx= 0.2, rely= 0.45) 
                    

                bt_enviar = tk.Button(perfil, text="Retirar",command=mudança_pontos_mercado, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 8, height= 1, font='BahnschriftLight 10')
                bt_enviar.place(relx = 0.8, rely=0.35)
                
            perfil.mainloop()

    bt_logando = tk.Button(aba_login, text="Entrar", command=logando, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2, font='BahnschriftLight 10')
    bt_logando.place_configure(relx= 0.2, rely= 0.7)    

# Janela inicial principal

janela = tk.Tk()
janela.configure(bg='lightgray')
janela.geometry("450x450")
janela.title('Entrada')

# Configurando o formato da janela

janela.resizable(False, False)

window_height = 500
window_width = 600

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

janela.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# mudando icone da janela 

urllib.request.urlretrieve(
  'https://lh3.googleusercontent.com/pw/AL9nZEXjGV1L3J_3ci_jUHoOc7iBTrMyKLWgUr7clEvaikl9J5VpXMwuSEmBKwXUr0HBoLhF0fPByc9Z9K924Dj4crc7F3yCnQorENduHM4uOUcghyl3hxPtmy2i-h5DepZ4TqNQjf8V3QzWHysO5n31ZDpD=w147-h137-no?authuser=2',
   "icon.png")

icon = PhotoImage(file = 'icon.png')
janela.iconphoto(False, icon)

# Logo

logo = tk.Label(janela, text="Eco DinDin", bg='#005F40', fg='white', font='BahnschriftLightCondensed 18 bold',  justify = 'left', width= 42, height= 2)
logo.place(relx=0, rely=0)

# Imagem

urllib.request.urlretrieve(
  'https://lh3.googleusercontent.com/pw/AL9nZEVqph0lL55F4U2TBRAEAp68nXbLdL3D90AxjdusFj70kPwnGOeWkFhtgbRDIpmEIxGeCzSIXLNZW3jf95FNm6WBcQNZrNXcLejF67QvTd2ujmyxBr3cCB9fi0eJeM0Z6FZ6w5YdPFz_iW-dSatGxUU3=w565-h617-no?authuser=2',
   "ciclo.png")
imagem1 = "ciclo.png"
frame = Frame(janela, width=489, height=535)
frame.pack()
frame.place(anchor='center', relx=0.72, rely=0.7)
image = PIL.Image.open(f"{imagem1}")
resize_image = image.resize((220,240))
img = PIL.ImageTk.PhotoImage(resize_image)
label = Label(frame, image = img, bg='lightgray')
label.photo = img
label.pack()

# Boas Vindas

mensagem_inicial = tk.Label(janela, text="Bem-Vindo", bg='lightgray', font='BahnschriftLight 15')
mensagem_inicial.place(relx= 0.43, rely= 0.2)

mensagem_inicial2 = tk.Label(janela, text="""Aqui você pode ajudar o meio ambiente de uma forma simples 
e ainda ganhar pontos pela ação.""", bg='lightgray', font='BahnschriftLight 12')
mensagem_inicial2.place(relx= 0.15, rely= 0.3)

mensagem_inicial3 = tk.Label(janela, text="Faça login ou cadastre-se:", bg='lightgray', font='BahnschriftLight 12')
mensagem_inicial3.place(relx= 0.08, rely= 0.48)

# Login / Cadastro

bt_cadastro = tk.Button(janela, text="Cadastrar", command=cadastro, bg='#005F40', fg= 'white', cursor= 'draft_large', width= 10, height= 2,  font='BahnschriftLight 10')
bt_cadastro.place(relx=0.25,rely=0.75)

bt_login = tk.Button(janela, text="Login", command=login, bg='#005F40', cursor= 'draft_large', fg= 'white', justify = 'center', width= 10, height= 2,  font='BahnschriftLight 10')
bt_login.place_configure(relx=0.25,rely=0.6)
 
janela.mainloop()
