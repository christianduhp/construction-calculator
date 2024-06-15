import tkinter as tk
from construction_calculator_engine import ConstructionCalculatorEngine
from tkinter import PhotoImage, Entry, Label, Button, messagebox


class ConstructionCalculatorApp:

    def __init__(self):
        self.engine = ConstructionCalculatorEngine()
        self.setup_window()
        self.load_assets()
        self.set_styles()

    def setup_window(self):
        self.window = tk.Tk()
        self.window.title("Calculadora Primos Depósito")
        self.window.geometry("490x560+500+80")
        self.window.resizable(0, 0)

    def load_assets(self):
        try:
            self.photo = PhotoImage(file="assets/icon.png")
            self.window.wm_iconphoto(False, self.photo)

            self.assets = {
                "main_bg": PhotoImage(file="assets/img_bg_main.png"),
                "ceiling_bg": PhotoImage(file="assets/img_bg_forro.png"),
                "slab_bg": PhotoImage(file="assets/img_bg_laje.png"),
                "opcao_laje_bg": PhotoImage(file="assets/img_bg_opcao_laje.png"),
                "area_laje_bg": PhotoImage(file="assets/img_bg_area_laje.png"),
                "btn_forro": PhotoImage(
                    file="assets/button_calculate_ceiling_panels.png"
                ),
                "btn_laje": PhotoImage(file="assets/button_calculate_slab_area.png"),
                "btn_trilho": PhotoImage(file="assets/button_tenho_trilho.png"),
                "btn_no_trilho": PhotoImage(file="assets/button_nao_tenho_trilho.png"),
                "btn_calcular": PhotoImage(file="assets/button_calcular.png"),
                "btn_back": PhotoImage(file="assets/button_back.png"),
                "btn_trilho_comp": PhotoImage(
                    file="assets/button_trilho_comprimento.png"
                ),
                "btn_trilho_larg": PhotoImage(file="assets/button_trilho_largura.png"),
            }
        except tk.TclError as e:
            messagebox.showerror("Erro de Assets", f"Erro ao carregar assets: {e}")

    def set_styles(self):
        self.font = ("Helvetica", 12, "bold")
        self.fg = "#414092"
        self.bg = "white"
        self.justify = tk.CENTER

    def display_slab_result(
        self,
        width=None,
        length=None,
        direction=None,
        has_track=False,
        n_track=None,
        track_length=None,
    ):
        if has_track:
            area = self.engine.calculate_slab_area(
                has_track=True, n_track=n_track, track_length=track_length
            )
            text_output = f"A ÁREA DA LAJE É {round(area, 3)} m²"
        else:
            n_track, length_choosen, area = self.engine.calculate_slab_area(width, length, direction)
            text_output =  f"QUANTIDADE: {round(n_track)} TRILHOS DE {length_choosen} METROS \nÁREA DA LAJE: {round(area, 2)}m²"

        self.create_label_style(text_output, 435, 160, 25, 350)

    def display_slab_options(self):
        self.create_label(self.assets["opcao_laje_bg"])

        self.create_button(
            self.assets["btn_trilho"], self.display_option_with_track, 301, 40, 90, 300
        )
        self.create_button(
            self.assets["btn_no_trilho"],
            self.display_option_without_track,
            301, 40, 90, 350
        )
        self.button_back()

    def display_option_with_track(self):
        self.create_label(self.assets["area_laje_bg"])

        qt_trilho = self.create_entry(205, 30, 26, 170)
        track_length = self.create_entry(205, 30, 260, 170)

        self.create_button(
            self.assets["btn_calcular"],
            lambda: self.display_slab_result(
                has_track=True,
                n_track=float(qt_trilho.get()),
                track_length=float(track_length.get()),
            ),
            301, 40, 90, 250
        )
        self.create_button(
            self.assets["btn_back"], self.display_slab_options, 40, 40, 230, 525
        )

    def display_option_without_track(self):
        self.create_label(self.assets["slab_bg"])

        width = self.create_entry(205, 30, 26, 158)
        length = self.create_entry(205, 30, 260, 158)

        self.create_button(
            self.assets["btn_trilho_larg"],
            lambda: self.display_slab_result(
                float(width.get()), float(length.get()), "width"
            ),
            301, 40, 90, 230
        )

        self.create_button(
            self.assets["btn_trilho_comp"],
            lambda: self.display_slab_result(
                float(width.get()), float(length.get()), "length"
            ),
            301, 40, 90, 280
        )

        self.create_button(
            self.assets["btn_back"], self.display_slab_options, 40, 40, 230, 525
        )

    def display_ceiling_result(self, width, length):
        
        result = self.engine.calculate_ceiling_panels(width, length)
        suggestions = []

        for key, value in enumerate(result):
            suggestion = value["pieces"]
            lim = value["pieces_length"]
            area = value["area"]
            suggestions.append(f"SUGESTÃO {key + 1}: {suggestion} PEÇAS DE {lim}m (ÁREA DE {area}m²)\n")

        text_output = ''.join(suggestions)  
        self.create_label_style(text_output, 435, 160, 25, 350)

    def display_ceiling_screen(self):
        self.create_label(self.assets["ceiling_bg"])

        width = self.create_entry(205, 30, 26, 170)
        length = self.create_entry(205, 30, 260, 170)

        self.create_button(
            self.assets["btn_calcular"],
            lambda: self.display_ceiling_result(float(width.get()), float(length.get())),
            301, 40, 90, 250
        )
        self.button_back()

    def button_back(self):
        self.create_button(self.assets["btn_back"], self.main_window, 40, 40, 230, 525)

    def create_label_style(self, text, width, height, x, y):
        label = Label(self.window, font=self.font, fg=self.fg, bg=self.bg, text=text)
        label.place(width=width, height=height, x=x, y=y)
        return label

    def create_label(self, image):
        self.clear_frame()
        label = Label(self.window, image=image, highlightthickness=0, borderwidth=0)
        label.grid()
        return label

    def create_button(self, image, command, width=None, height=None, x=None, y=None):
        button = Button(
            self.window,
            image=image,
            highlightthickness=0,
            borderwidth=0,
            command=command,
        )
        if width and height and x and y:
            button.place(width=width, height=height, x=x, y=y)
        return button

    def create_entry(self, width, height, x, y):
        entry = Entry(self.window, font=self.font, justify=self.justify, fg=self.fg)
        entry.place(width=width, height=height, x=x, y=y)
        return entry

    def clear_frame(self):
        for widget in self.window.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()

    def main_window(self):
        self.create_label(self.assets["main_bg"])

        self.create_button(
            self.assets["btn_laje"], self.display_slab_options, 301, 40, 90, 350
        )
        self.create_button(
            self.assets["btn_forro"], self.display_ceiling_screen, 301, 40, 90, 400
        )
        self.window.mainloop()


if __name__ == "__main__":
    app = ConstructionCalculatorApp()
    app.main_window()
