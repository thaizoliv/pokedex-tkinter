from tkinter import *
from tkinter import ttk

#pillow
from PIL import Image, ImageTk

from dados import *

#####     cores   #####
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

#criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style  = ttk.Style(janela)
style.theme_use("clam")

#criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief="flat")
frame_pokemon.grid(row=1, column=0)


def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem

    #trocar cor do fundo do frame
    frame_pokemon['bg'] = pokemon[i]['tipo'][3]

    #tipo de pokemon
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    imagem_pokemon = pokemon[i]['tipo'][2]

    #imagem 
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(frame_pokemon, image = imagem_pokemon, relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    pok_imagem.place(x=60, y=50)

    pok_tipo.lift()

    #pokemon status
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_ataque['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    #pokemon habilidades
    pok_hb_1['text'] = pokemon[i]['habilidades'][0]
    pok_hb_2['text'] = pokemon[i]['habilidades'][1]


#nome
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER,font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12, y=15)

#categoria
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER,font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

#id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER,font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)




#status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER,font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

#hp
pok_hp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER,font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

#ataque
pok_ataque = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER,font=('Verdana 10'), bg=co1, fg=co4)
pok_ataque.place(x=15, y=385)

#defesa
pok_defesa = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER,font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

#velocidade
pok_velocidade = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER,font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

#total
pok_total = Label(janela, text='Total: 1.700', relief='flat', anchor=CENTER,font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)


#Habilidades
pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER,font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidades.place(x=180, y=310)

#hp
pok_hb_1 = Label(janela, text='Choque do Trovão', relief='flat', anchor=CENTER,font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_1.place(x=195, y=360)

#ataque
pok_hb_2 = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER,font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_2.place(x=195, y=385)


#criando botões para pokemon

#imagem1 
imagem_pokemon1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon1 = imagem_pokemon1.resize((40, 40))
imagem_pokemon1 = ImageTk.PhotoImage(imagem_pokemon1)

b_pok_imagem = Button(janela, command=lambda:trocar_pokemon('Pikachu') , image = imagem_pokemon1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_imagem.place(x=375, y=10)

#imagem2
imagem_pokemon2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon2 = imagem_pokemon2.resize((40, 40))
imagem_pokemon2 = ImageTk.PhotoImage(imagem_pokemon2)

b_pok_imagem2 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur') , image = imagem_pokemon2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_imagem2.place(x=375, y=60)

#imagem3
imagem_pokemon3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon3 = imagem_pokemon3.resize((40, 40))
imagem_pokemon3 = ImageTk.PhotoImage(imagem_pokemon3)

b_pok_imagem3 = Button(janela, command=lambda:trocar_pokemon('Charmander') , image = imagem_pokemon3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_imagem3.place(x=375, y=110)


#imagem4
imagem_pokemon4 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon4 = imagem_pokemon4.resize((40, 40))
imagem_pokemon4 = ImageTk.PhotoImage(imagem_pokemon4)

b_pok_imagem4 = Button(janela, command=lambda:trocar_pokemon('Gyarados') , image = imagem_pokemon4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_imagem4.place(x=375, y=160)


#imagem5
imagem_pokemon5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon5 = imagem_pokemon5.resize((40, 40))
imagem_pokemon5 = ImageTk.PhotoImage(imagem_pokemon5)

b_pok_imagem5 = Button(janela, command=lambda:trocar_pokemon('Gengar') , image = imagem_pokemon5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_imagem5.place(x=375, y=210)


#imagem6
imagem_pokemon6 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon6 = imagem_pokemon6.resize((40, 40))
imagem_pokemon6 = ImageTk.PhotoImage(imagem_pokemon6)

b_pok_imagem6 = Button(janela, command=lambda:trocar_pokemon('Dragonite') , image = imagem_pokemon6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_imagem6.place(x=375, y=260)


import random
Lista_pokemon = ['Pikachu', 'Bulbasaur', 'Charmander', 'Gyarados', 'Gengar', 'Dragonite']
pokemon_escolhido = random.sample(Lista_pokemon, 1)
trocar_pokemon(pokemon_escolhido[0])









janela.mainloop()