from imports import *

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

