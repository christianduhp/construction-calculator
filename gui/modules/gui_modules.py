from tkinter import Entry, Label, Button
from .gui_set import janela

def create_label_style(janela, font, fg, bg, text, width, height, x, y):
    label = Label(janela,
                  font=font,
                  fg=fg,
                  bg=bg,
                  text=text)
    label.place(width=width, height=height, x=x, y=y)
    return label

def create_label(image):    
    for widget in janela.winfo_children():
        if isinstance(widget, Label):
            widget.destroy()
    
    label = Label(janela, image=image, highlightthickness=0, borderwidth=0)
    label.grid()

def create_button(image, command):
    button = Button(janela, image=image, highlightthickness=0, borderwidth=0, command=command)
    return button

def create_entry(font, justify, fg, width, height, x, y):
    entry = Entry(janela, font=font, justify=justify, fg=fg)
    entry.place(width=width, height=height, x=x, y=y)
    return entry

def clear_frame():
    for widget in janela.winfo_children():
        widget.destroy()
