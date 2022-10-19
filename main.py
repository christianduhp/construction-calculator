from tkinter import *
from tkinter.font import Font

janela = Tk()
janela.title('Calculadora Primos Depósito')
janela.geometry('490x560+500+80')
photo = PhotoImage(file = 'images//icon.png')
janela.wm_iconphoto(False, photo)
janela.resizable(0, 0)

img_bg_main = PhotoImage(file='images//img_bg_main.png')
img_bg_forro = PhotoImage(file='images//img_bg_forro.png')
img_bg_laje = PhotoImage(file='images//img_bg_laje.png')
img_bg_forro = PhotoImage(file='images//img_bg_forro.png')
img_bg_opcao_laje = PhotoImage(file='images//img_bg_opcao_laje.png')
img_bg_area_laje = PhotoImage(file='images//img_bg_area_laje.png')
img_button_calcular_forro = PhotoImage(file='images//button_calcular_forro.png')
img_button_calcular_laje = PhotoImage(file='images//button_calcular_laje.png')
img_button_tenho_trilho = PhotoImage(file='images//button_tenho_trilho.png')
img_button_nao_tenho_trilho = PhotoImage(file='images//button_nao_tenho_trilho.png')
img_button_calcular = PhotoImage(file='images//button_calcular.png')
img_button_back = PhotoImage(file='images//button_back.png')
img_button_info = PhotoImage(file='images//button_info.png')
img_button_trilho_comprimento = PhotoImage(file='images//button_trilho_comprimento.png')
img_button_trilho_largura = PhotoImage(file='images//button_trilho_largura.png')

def forro(largura, comprimento):
    text_forro = Label(janela,
                       font=("Helvica", "10", "bold"),
                       bg='white',
                       fg="#414092",
                       text='')
    forro = largura / 0.2
    sugestao = lim = 1
    sugestao_list = []
    lim_list = []
    area_list = []
    while sugestao > 0 and lim < 6:
        lim += 1
        sugestao = (comprimento / lim) * forro
        area = round(sugestao + 0.5) * lim * 0.2
        sugestao = int(sugestao)
        if sugestao % 2 == 0:
            sugestao_list.append(round(sugestao, 1))
            lim_list.append(lim)
            area_list.append(round(area, 2))

    list_size = len(sugestao_list)

    if list_size == 1:
        text_output = " SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n".format(
            sugestao_list[0], lim_list[0], area_list[0])

    if list_size == 2:
        text_output = " SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n".format(
            sugestao_list[0], lim_list[0], area_list[0], sugestao_list[1],
            lim_list[1], area_list[1])

    if list_size == 3:
        text_output = " SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n".format(
            sugestao_list[0], lim_list[0], area_list[0], sugestao_list[1],
            lim_list[1], area_list[1], sugestao_list[2], lim_list[2],
            area_list[2])

    if list_size == 4:
        text_output = " SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n".format(
            sugestao_list[0], lim_list[0], area_list[0], sugestao_list[1],
            lim_list[1], area_list[1], sugestao_list[2], lim_list[2],
            area_list[2], sugestao_list[3], lim_list[3], area_list[3])

    if list_size == 5:
        text_output = " SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n".format(
            sugestao_list[0], lim_list[0], area_list[0], sugestao_list[1],
            lim_list[1], area_list[1], sugestao_list[2], lim_list[2],
            area_list[2], sugestao_list[3], lim_list[3], area_list[3],
            sugestao_list[4], lim_list[4], area_list[4])

    if list_size == 6:
        text_output = " SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)\n SUGESTÃO: {} PEÇAS DE {}m (ÁREA DE {}m²)".format(
            sugestao_list[0], lim_list[0], area_list[0], sugestao_list[1],
            lim_list[1], area_list[1], sugestao_list[2], lim_list[2],
            area_list[2], sugestao_list[3], lim_list[3], area_list[3],
            sugestao_list[4], lim_list[4], area_list[4], sugestao_list[5],
            lim_list[5], area_list[5])

    text_forro['text'] = text_output
    text_forro.place(width=435, height=160, x=25, y=350)


def laje_largura(largura, comprimento):
    text_laje_largura = Label(janela,
                              font=("Helvica", "12", "bold"),
                              fg="#414092",
                              bg='white',
                              text='')

  
    quant_trilho = comprimento / 0.43
    if quant_trilho ==round(quant_trilho):
      novo_comprimento = quant_trilho * 0.43
      area_laje = largura * novo_comprimento
      text_laje_largura['text'] = "QUANTIDADE: {} TRILHOS DE {} METROS \nÁREA DA LAJE: {}m²".format(round(quant_trilho), largura, round(area_laje, 2))
      text_laje_largura.place(width=435, height=80, x=25, y=383)
      
    else:
      novo_comprimento = round(quant_trilho+0.5) * 0.43
      area_laje = largura * novo_comprimento
      text_laje_largura['text'] = "QUANTIDADE: {} TRILHOS DE {} METROS \nÁREA DA LAJE: {}m²".format(round(quant_trilho+0.5), largura, round(area_laje, 2))
      text_laje_largura.place(width=435, height=80, x=25, y=383)



def laje_comprimento(largura, comprimento):
    text_laje_comprimento = Label(janela,
                              font=("Helvica", "12", "bold"),
                              fg="#414092",
                              bg='white',
                              text='')
  
    quant_trilho = largura / 0.43
    if quant_trilho ==round(quant_trilho):
      nova_largura = quant_trilho * 0.43
      area_laje = comprimento * nova_largura
      text_laje_comprimento['text'] = "QUANTIDADE: {} TRILHOS DE {} METROS \nÁREA DA LAJE: {}m²".format(round(quant_trilho), comprimento ,round(area_laje, 2))
      text_laje_comprimento.place(width=435, height=80, x=25, y=383)
      
    else:
      nova_largura = round(quant_trilho+0.5) * 0.43
      area_laje = comprimento * nova_largura
      text_laje_comprimento['text'] = "QUANTIDADE: {} TRILHOS DE {} METROS \nÁREA DA LAJE: {}m²".format(round(quant_trilho+0.5), comprimento ,round(area_laje, 2))
      text_laje_comprimento.place(width=435, height=80, x=25, y=383)



def laje_area(qt_trilho, tam_trilho):
  bg_image = Label(janela,
                   highlightthickness=0,
                   borderwidth=0,
                   image=img_bg_area_laje)
  bg_image.grid()
  text_area = Label(janela,
                     font=("Helvica", "10", "bold"),
                     bg='white',
                     fg="#414092",
                     text='')
  area = qt_trilho *0.43  *tam_trilho 
  area = "A ÁREA DA LAJE É {} m²".format(area)
  text_area['text'] = area
  text_area.place(width=435, height=160, x=25, y=350)

def opcao_laje_tkinter():
    main_bg = Label(janela, image=img_bg_opcao_laje)
    main_bg.grid()

    img_button_laje = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_tenho_trilho,
        command=lambda: [clear_frame(), opcao_tenho_trilho_tkinter()])
    img_button_laje.place(width=301, height=40, x=90, y=300)

    img_button_forro = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_nao_tenho_trilho,
        command=lambda: [clear_frame(), opcao_nao_tenho_trilho_tkinter()])
    img_button_forro.place(width=301, height=40, x=90, y=350)

    button_back = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_back,
        command=lambda: [clear_frame(), main_janela()])
    button_back.place(width=40, height=40, x=230, y=525)




def opcao_tenho_trilho_tkinter():
    bg_image = Label(janela,
                     highlightthickness=0,
                     borderwidth=0,
                     image=img_bg_area_laje)
    bg_image.grid()

    qt_trilho = Entry(janela, font=("Helvica", "12", "bold"), justify=CENTER, fg='#414092')
    qt_trilho.place(width=205, height=30, x=26, y=170)

    tam_trilho = Entry(janela, font=("Helvica", "12", "bold"), justify=CENTER, fg='#414092')
    tam_trilho.place(width=205, height=30, x=260, y=170)

    button_calcular = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_calcular,
        command=lambda: laje_area(float(qt_trilho.get()), float(tam_trilho.get())))
    button_calcular.place(width=301, height=40, x=90, y=250)

    button_back = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_back,
        command=lambda: [clear_frame(), opcao_laje_tkinter()])
    button_back.place(width=40, height=40, x=230, y=525)


def opcao_nao_tenho_trilho_tkinter():
    bg_image = Label(janela,
                     highlightthickness=0,
                     borderwidth=0,
                     image=img_bg_laje)
    bg_image.grid()

    largura = Entry(janela, font=("Helvica", "12", "bold"), justify=CENTER, fg='#414092')
    largura.place(width=205, height=30, x=26, y=158)

    comprimento = Entry(janela, font=("Helvica", "12", "bold"), justify=CENTER, fg='#414092')
    comprimento.place(width=205, height=30, x=260, y=158)

    button_largura = Button(janela,
                            highlightthickness=0,
                            borderwidth=0,
                            image=img_button_trilho_largura,
                            command=lambda: laje_largura(
                                float(largura.get()), float(comprimento.get())))
    button_largura.place(width=301, height=40, x=90, y=230)

    button_comprimento = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_trilho_comprimento,
        command=lambda: laje_comprimento(float(largura.get()),
                                         float(comprimento.get())))
    button_comprimento.place(width=301, height=40, x=90, y=280)

    button_back = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_back,
        command=lambda: [clear_frame(), opcao_laje_tkinter()])
    button_back.place(width=40, height=40, x=230, y=525)


def forro_tkinter():

    bg_image = Label(janela,
                     highlightthickness=0,
                     borderwidth=0,
                     image=img_bg_forro)
    bg_image.grid()

    largura = Entry(janela, font=("Helvica", "12", "bold"), justify=CENTER, fg='#414092')
    largura.place(width=205, height=30, x=26, y=170)

    comprimento = Entry(janela, font=("Helvica", "12", "bold"), justify=CENTER, fg='#414092')
    comprimento.place(width=205, height=30, x=260, y=170)

    button_calcular = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_calcular,
        command=lambda: forro(float(largura.get()), float(comprimento.get())))
    button_calcular.place(width=301, height=40, x=90, y=250)

    button_back = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_back,
        command=lambda: [clear_frame(), main_janela()])
    button_back.place(width=40, height=40, x=230, y=525)


def main_janela():
    main_bg = Label(janela, image=img_bg_main)
    main_bg.grid()

    img_button_laje = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_calcular_laje,
        command=lambda: [clear_frame(), opcao_laje_tkinter()])
    img_button_laje.place(width=301, height=40, x=90, y=350)

    img_button_forro = Button(
        janela,
        highlightthickness=0,
        borderwidth=0,
        image=img_button_calcular_forro,
        command=lambda: [clear_frame(), forro_tkinter()])
    img_button_forro.place(width=301, height=40, x=90, y=400)


def clear_frame():
    # destroy all widgets from frame
    for widget in janela.winfo_children():
        widget.destroy()


main_janela()
janela.mainloop()
