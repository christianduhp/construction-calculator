from imports import *

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
    if quant_trilho == round(quant_trilho):
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