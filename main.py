import tkinter as tk
from gui.modules.gui_set import *
from gui.modules.gui_modules import create_label, create_button, create_entry
from calculator.calculator_forro import forro
from calculator.calculator_laje import laje_largura, laje_area, laje_comprimento

def opcao_laje_tkinter():
    create_label(img_bg_opcao_laje)

    img_button_laje = create_button(img_button_tenho_trilho, opcao_tenho_trilho_tkinter)
    img_button_laje.place(width=301, height=40, x=90, y=300)

    img_button_forro = create_button(img_button_nao_tenho_trilho, opcao_nao_tenho_trilho_tkinter)
    img_button_forro.place(width=301, height=40, x=90, y=350)
    
    button_back = create_button(img_button_back, main_janela)
    button_back.place(width=40, height=40, x=230, y=525)

def opcao_tenho_trilho_tkinter():
    create_label(img_bg_area_laje)

    qt_trilho = create_entry(font, tk.CENTER, fg, 205, 30, 26, 170)
    tam_trilho = create_entry(font, tk.CENTER, fg, 205, 30, 260, 170)

    button_calcular = create_button(img_button_calcular, lambda: laje_area(float(qt_trilho.get()), float(tam_trilho.get())))
    button_calcular.place(width=301, height=40, x=90, y=250)

    button_back = create_button(img_button_back, opcao_laje_tkinter)
    button_back.place(width=40, height=40, x=230, y=525)

def opcao_nao_tenho_trilho_tkinter():
    create_label(img_bg_laje)

    largura = create_entry(font, tk.CENTER, fg, 205, 30, 26, 158)
    comprimento = create_entry(font, tk.CENTER, fg, 205, 30, 260, 158)

    button_largura = create_button(img_button_trilho_largura, lambda: laje_largura(float(largura.get()), float(comprimento.get())))
    button_largura.place(width=301, height=40, x=90, y=230)

    button_comprimento = create_button(img_button_trilho_comprimento, lambda: laje_comprimento(float(largura.get()), float(comprimento.get())))
    button_comprimento.place(width=301, height=40, x=90, y=280)

    button_back = create_button(img_button_back, opcao_laje_tkinter)
    button_back.place(width=40, height=40, x=230, y=525)

def forro_tkinter():
    create_label(img_bg_forro)

    largura = create_entry(font, tk.CENTER, fg, 205, 30, 26, 170)
    comprimento = create_entry(font, tk.CENTER, fg, 205, 30, 260, 170)

    button_calcular = create_button(img_button_calcular, lambda: forro(float(largura.get()), float(comprimento.get())))
    button_calcular.place(width=301, height=40, x=90, y=250)
    
    button_back = create_button(img_button_back, main_janela)
    button_back.place(width=40, height=40, x=230, y=525)

def main_janela():
    create_label(img_bg_main)

    img_button_laje = create_button(img_button_calcular_laje, opcao_laje_tkinter)
    img_button_laje.place(width=301, height=40, x=90, y=350)

    img_button_forro = create_button(img_button_calcular_forro, forro_tkinter)
    img_button_forro.place(width=301, height=40, x=90, y=400)


if __name__ == "__main__":
    main_janela()
    janela.mainloop()