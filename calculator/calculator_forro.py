from gui.modules.gui_set import *
from gui.modules.gui_modules import create_label_style

def forro(largura, comprimento):
   
    text_forro = create_label_style(janela,font,fg,bg, '', 435, 160, 25, 350)
    
    def calculate_forro(largura, comprimento):
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
    
    calculate_forro(largura, comprimento)
    janela.mainloop()
