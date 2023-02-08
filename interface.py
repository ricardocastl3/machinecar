

from validation import *
from customtkinter import *
import pandas as pd

class App(CTk):
    def __init__(self):
        super().__init__()

        varPreco = StringVar(value="")
        varIdade = StringVar(value="")
        varMilhas = StringVar(value="")

        frameSidebar = CTkFrame(master=self,)
        frameSidebar.grid(row=0, column=1, stick="w", ipadx=40, ipady=5000)

        frameSDBottom = CTkFrame(master=frameSidebar, fg_color="transparent")
        frameSDBottom.pack(side="bottom", anchor="w", pady=50)

        frameContent = CTkFrame(master=self, )
        frameContent.grid(row=0, column=1, ipadx=400, ipady=50, padx=250, pady=50, sticky="n")

        frameContentResults = CTkFrame(master=self, )
        frameContentResults.grid(row=0, column=1, ipadx=400, ipady=50, pady=50, padx=250, sticky="sw",)

        #### SIDEBAR
        lbWelcome = CTkLabel(frameSidebar, text="AUTOVENDAS", font=("",14,"bold"))
        lbWelcome.pack(anchor="w", pady=20, padx=20)

        lbTheme = CTkLabel(frameSDBottom, text="Escolha o seu tema")
        lbTheme.pack(anchor="w", padx=20)

        def changeTheme(theme):
            if theme == "Escuro":
                set_appearance_mode("Dark")
            elif theme == "Claro":
                set_appearance_mode("Light")

        varTheme = StringVar(value="Dark")
        cbTheme = CTkComboBox(frameSDBottom, values=["Escuro", "Claro"], variable=varTheme,
                              command=changeTheme)
        cbTheme.pack(side="left", padx=20)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        lbWelCont = CTkLabel(frameContent, text="PREVISÃO DE COMPRA", font=("",20,"bold"))
        lbWelCont.grid(row=0, padx=50, pady=40, sticky="w")

        lbPreco = CTkLabel(frameContent, text="Preço", font=("",13,"bold"))
        lbPreco.grid(row=1, column=0, sticky="w", padx = 50)

        lbIdade = CTkLabel(frameContent, text="Idade do modelo", font=("", 13, "bold"))
        lbIdade.grid(row=1, column=1, sticky="w", padx=50)

        lbMilhas = CTkLabel(frameContent, text="Milhas por hora", font=("", 13, "bold"))
        lbMilhas.grid(row=1, column=2, sticky="w", padx=50)

        self.txtPreco = CTkEntry(frameContent, width=200, height=40, corner_radius=10, font=("",15,"bold"),
                                 textvariable=varPreco)
        self.txtPreco.grid(row=2, column=0, padx=50, sticky="w", pady=20)

        self.txtIdade = CTkEntry(frameContent, width=200, height=40, corner_radius=10, font=("",15,"bold"),
                                 textvariable=varIdade)
        self.txtIdade.grid(row=2, column=1, padx=50, sticky="w", pady=20)

        self.txtMilhas = CTkEntry(frameContent, width=200, height=40, corner_radius=10, font=("",15,"bold"),
                                  textvariable=varMilhas)
        self.txtMilhas.grid(row=2, column=2, padx=50, sticky="w", pady=20)

        #STATUS BAR
        lbAccuracy = CTkLabel(frameContentResults, text="ACURÁCIA: ", font=("",19,"bold"))
        lbAccuracy.grid(row=3, column=0, sticky="w", columnspan=20, padx=50, pady=40)

        accr = results.mean() * 100

        lbAccuracyShow = CTkLabel(frameContentResults, text="%.1f"%accr, font=("", 19, "bold"), text_color="green")
        lbAccuracyShow.grid(row=3, column=0, pady=20, sticky="w", padx=160)

        #SHOW PREVISION
        lbPrevision = CTkLabel(frameContentResults, text="PREVISÃO: ", font=("", 19, "bold"))
        lbPrevision.grid(row=3, column=1, sticky="w", columnspan=20, padx=50)

        accr = results.mean() * 100

        def predictSell():
            values = {
                "preco": varPreco.get(),
                "idade_modelo": varIdade.get(),
                "milhas_por_hora": varMilhas.get()
            }
            datas = pd.DataFrame(values, index=[0])

            prevision = model.predict(datas)
            lbPrevisionShow = CTkLabel(frameContentResults, text=prevision, font=("", 19, "bold"),
                                           text_color="green")
            lbPrevisionShow.grid(row=3, column=1, pady=20, sticky="w", padx=160)

        self.btPredict = CTkButton(frameContentResults, width=100, height=50, text="PREVER POSSÍVEL COMPRA",
                                   font=("", 14, "bold"), command=predictSell)
        self.btPredict.grid(row=4, column=0, sticky="w", padx=50)

def setConfigs(self):
    self.title("Venda de automóveis")
    self.geometry("900x500")
    self.mainloop()

def show():
    app = App()
    setConfigs(app)