import os
from tkinter import *
from tkinter import ttk
import donnees, application

# =================
# Affiche le titre selectionné
# =================
def affichageTitre():
    labelMenu = ttk.Label(edt, text="Menu Test",background="#f1f8e9", font=txtfont)
    labelMenu.place(x=250,y=50)

# ===============
# Fonction qui affiche le contenaire du centre de la fenetre
# ===============
def container_menu(fenetre, txtfont):
    global ListeSemaine
    menu = Frame(fenetre, background="#dcedc8", width=200, height=500)
    labelMenu = ttk.Label(menu, text="Menu",background="#dcedc8", font=txtfont)
    labelMenu.place(x=65,y=80)

    ListeSemaine = ttk.Combobox(menu, values=donnees.data["semaine"])
    ListeSemaine.set("Numero de la Semaine")
    ListeSemaine.place(x=25,y=125)

    ListeGroupe = ttk.Combobox(menu, values=donnees.data["groupe"])
    ListeGroupe.set("Nom du Groupe")
    ListeGroupe.place(x=25,y=175)

    ListeJour = ttk.Combobox(menu, values=donnees.data["jour"])
    ListeJour.set("Jour")
    ListeJour.place(x=25,y=225)

    btnValide = ttk.Button(menu, text="Valider", command=application.getterMenu)
    btnValide.place(x=60,y=275)
    menu.pack()


# ===================
# Fonction qui affiche le contenaire du Menu
# ==================
def container_edt(fenetre, txtfont):
    global edt
    edt = Frame(fenetre, background="#f1f8e9",width=600, height=500)
    labelMenu = ttk.Label(edt, text="EDT",background="#f1f8e9", font=txtfont)
    labelMenu.place(x=250,y=50)
    edt.pack(side=LEFT)


# =====================
# Fonction qui créer la fenetre de l'application 
# =====================
def app():
    global txtfont
    fenetre = Tk()
    fenetre.title("Application EDT")
    fenetre.geometry("800x500+400+150")
    fenetre.resizable(False, False)
    txtfont = ("Verdana", 18, "bold")
    container_edt(fenetre, txtfont)
    container_menu(fenetre, txtfont)
   
    
    


    fenetre.mainloop()

# Demarrage de la fenetre
if __name__ == '__main__':
    app()