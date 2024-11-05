import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
#import openpyxl, xdrlib
#import pathlib
#from openpyxl import Woorkbook


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.appearence()
        self.all_system()

    def layout_config(self):
        self.title ("Sistema de Cadastro de Produtos")
        self.geometry("500x700")

    def appearence(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=["#000", "#fff"], font=("Neuzeit Grotesk Light", 16)).place(x=300, y=0)
        self.opt_apm = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"], command = self.change_apm, font=("Neuzeit Grotesk Light", 16)). place(x=350, y=0)

    
    def all_system(self):
        frame = ctk.CTkFrame(self, width=700, height=70, corner_radius=0, bg_color="#000578", fg_color="#000578").place(x=0, y=30)
        title = ctk.CTkLabel(frame, text= "Cadastrar de Produtos", font=("BebasNeue-Regular", 24), text_color="#fff").place(x=150, y=50)
        subtitle = ctk.CTkLabel(self, text= "Por favor preencher as informações abaixo:", font=("Neuzeit Grotesk Bold", 12), text_color=["#000","#fff"]).place(x=50, y=100)
        
        #inputs_texto
        name_input = ctk.CTkEntry(self, width=400, height=50,corner_radius=20, textvariable="name_value", font=("Neuzeit Grotesk Light", 16), fg_color="transparent", border_color="#006eff")
        tipo_input = ctk.CTkEntry(self, width=200, height=50,corner_radius=20, textvariable="tipo_value",font=("Neuzeit Grotesk Light", 16), fg_color="transparent", border_color="#006eff")

        #input_select e text

        unidade_input = ctk.CTkComboBox(self, values=["PCT","CX","UNI"], font=("Neuzeit Grotesk Light", 16), width=150, height=50, corner_radius=20, border_color="#006eff", dropdown_fg_color="#006eff", dropdown_hover_color="#000578")
        unidade_input.set("UNI")
        observaçao_input = ctk.CTkTextbox(self, width=400, height=200, font=("BebasNeue-Light", 16), border_color="#006eff", border_width=2, fg_color="transparent", corner_radius=20)

        def submit():

            #pegando dados dos inputs
            name = name_value.get()
            tipo = tipo_value.get()
            obs = observaçao_input.get(0.0,END)
            unit = unidade_input.get()
            pass

        def clear():
            name = name_value.set("")
            tipo = tipo_value.set("")
            obs = observaçao_input.set("")
            pass

        #textos variaveis
        name_value = StringVar()
        tipo_value = StringVar()
        

        #btn
        bnt_submit = ctk.CTkButton(self, text="salvar".upper(), command=submit, fg_color="#151", hover="131")
        bnt_limpar = ctk.CTkButton(self, text="limpar".upper(), command=clear, fg_color="#555", hover="333")
        
        #campos
        lb_name = ctk.CTkLabel(self, text= "Nome do Produto:", font=("Neuzeit Grotesk Light", 16), text_color=["#006eff","#fff"])
        lb_tipo = ctk.CTkLabel(self, text= "Tipo:", font=("Neuzeit Grotesk Light", 16), text_color=["#006eff","#fff"])
        lb_unidade = ctk.CTkLabel(self, text= "Unidade:", font=("Neuzeit Grotesk Light", 16), text_color=["#006eff","#fff"])
        lb_observacao = ctk.CTkLabel(self, text= "Observações:", font=("Neuzeit Grotesk Light", 16), text_color=["#006eff","#fff"])

        #posições inputs na janelaA
        lb_name.place(x=50, y=120)
        name_input.place(x=50, y=150)

        lb_tipo.place(x=50, y=210)
        tipo_input.place(x=50,y=240)

        lb_unidade.place(x=270, y=210)
        unidade_input.place(x=270,y=240)

        lb_observacao.place(x=50, y=300)
        observaçao_input.place(x=50, y=330)

        bnt_submit.place(x=50,y=550)
        bnt_limpar.place(x=200,y=550)

    def change_apm(self, new_aparence_mode):
        ctk.set_appearance_mode(new_aparence_mode)

if __name__=="__main__":
    app = App()
    app.mainloop()

