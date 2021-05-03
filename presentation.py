import os
from tkinter import *
from tkinter import ttk
import donnees, application

class IHM:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("Application EDT")
        self.fenetre.geometry("800x500+400+150")
        self.fenetre.resizable(False, False)
    
    def creationWidget(self):
        txtFont = ("Verdana", 18, "bold")
        self.containerMenu(txtFont)
        self.containerEdt(txtFont)
        self.fenetre.mainloop()

    def containerEdt(self, txtFont):
        edt = Frame(self.fenetre, background="#f1f8e9",width=600, height=500)
        labelMenu = ttk.Label(edt, text="EDT",background="#f1f8e9", font=txtFont)
        labelMenu.place(x=250,y=50)
        edt.place(x=0,y=0)

    def erreurParametre(self, typeError):
        if typeError == "saisi":
            self.labelErreurParametre.config(text="Saisi des parametres invalides")
        if typeError == "incomplet":
            self.labelErreurParametre.config(text="Saisi des parametres incompletes")

    def getSemaine(self):
        return self.listeSemaine.get()

    def getJour(self):
        return self.listeJour.get()

    def getGroupe(self):
        return self.listeGroupe.get()

    def getValidation(self):
        validation = application.Application(self.getSemaine, self.getJour,self.getGroupe)
        if (validation.validationMenu()):
            self.erreurParametre(typeError)

    def containerMenu(self, txtFont):
        menu = Frame(self.fenetre, background="#dcedc8", width=200, height=500)
        labelMenu = ttk.Label(menu, text="Menu",background="#dcedc8", font=txtFont)
        labelMenu.place(x=65,y=80)

        self.labelErreurParametre = ttk.Label(menu, text="",background="#dcedc8",)
        self.labelErreurParametre.place(x=10,y=107)

        self.listeSemaine = ttk.Combobox(menu, values=donnees.data["semaine"])
        self.listeSemaine.set("Numero de la Semaine")
        self.listeSemaine.place(x=25,y=125)

        self.listeGroupe = ttk.Combobox(menu, values=donnees.data["groupe"])
        self.listeGroupe.set("Nom du Groupe")
        self.listeGroupe.place(x=25,y=175)

        self.listeJour = ttk.Combobox(menu, values=donnees.data["jour"])
        self.listeJour.set("Jour")
        self.listeJour.place(x=25,y=225)

        btnValide = ttk.Button(menu, text="Valider", command=self.getValidation)
        btnValide.place(x=60,y=275)
        menu.place(x=600,y=0)

if __name__ == '__main__':
    app = IHM()
    app.creationWidget()