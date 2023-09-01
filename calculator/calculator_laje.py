from tkinter import Label
from gui.modules.gui_set import *
from gui.modules.gui_modules import create_label_style

def laje_largura(largura, comprimento):
    quant_trilho = comprimento / 0.43
    if quant_trilho == round(quant_trilho):
        novo_comprimento = quant_trilho * 0.43
    else:
        novo_comprimento = round(quant_trilho + 0.5) * 0.43
    
    area_laje = largura * novo_comprimento
    text = "QUANTIDADE: {} TRILHOS DE {} METROS \nÁREA DA LAJE: {}m²".format(
        round(quant_trilho), largura, round(area_laje, 2))
    
    create_label_style(janela,font,fg,bg, text, 435, 80, 25, 383)

def laje_comprimento(largura, comprimento):
    quant_trilho = largura / 0.43
    if quant_trilho == round(quant_trilho):
        nova_largura = round(quant_trilho * 0.43 , 3)
    else:
        nova_largura = round(quant_trilho + 0.5) * 0.43
    
    area_laje = comprimento * nova_largura
    text = "QUANTIDADE: {} TRILHOS DE {} METROS \nÁREA DA LAJE: {}m²".format(
        round(quant_trilho), comprimento, round(area_laje, 2))
    
    create_label_style(janela,font,fg, bg, text, 435, 80, 25, 383)

def laje_area(qt_trilho, tam_trilho):
    bg_image = Label(janela,
                     highlightthickness=0,
                     borderwidth=0,
                     image=img_bg_area_laje)
    bg_image.grid()

    area = qt_trilho * 0.43 * tam_trilho 
    text = "A ÁREA DA LAJE É {} m²".format(round(area,3))
    
    create_label_style(janela,font,fg,bg, text, 435, 160, 25, 350)
