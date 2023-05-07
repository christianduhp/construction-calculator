from imports import *

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

    text_output = ""
    for i in range(list_size):
        text_output += " SUGESTÃO {}: {} PEÇAS DE {}m (ÁREA DE {}m²)\n".format(
            i+1, sugestao_list[i], lim_list[i], area_list[i])

        text_forro['text'] = text_output
        text_forro.place(width=435, height=160, x=25, y=350)