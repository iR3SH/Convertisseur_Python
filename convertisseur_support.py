#Importation des ressources
import sys
import polonais
from controlconcat import *
import controlconcat
from dict import operation
from conversion import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


#Variables des Objets Tkinter
def set_Tk_var():
    #Entrée Decimale
    global deci
    deci = tk.StringVar()
    #Entrée Hexadécimal
    global hexad
    hexad = tk.StringVar()
    #Entrée Binaire
    global bin
    bin = tk.StringVar()
    global decimaloutput
    decimaloutput = tk.StringVar()
    global hexaoutput
    hexaoutput = tk.StringVar()
    global binoutput
    binoutput = tk.StringVar()


deciresult = ""  #Variable pour avoir la valeur du dernier résultat de calcul


#Commande Bouton de Conversion Binaire
def convert_bin():
    decimaloutput.set("")
    hexaoutput.set("")
    binoutput.set("")
    deci.set("")
    hexad.set("")
    bininp = bin.get()
    controlconcat.ccbin(bininp)


#Commande Bouton de Conversion Décimale
def convertir_deci():
    decimaloutput.set("")
    binoutput.set("")
    hexaoutput.set("")
    hexad.set("")
    bin.set("")
    decinp = deci.get()
    controlconcat.ccdec(decinp, bool(False))


#Commande Bouton de Conversion Hexadécimal
def convertir_hex():
    decimaloutput.set("")
    binoutput.set("")
    hexaoutput.set("")
    bin.set("")
    deci.set("")
    hexinp = hexad.get()
    controlconcat.cchex(hexinp)


#Commande Bouton de Conversion du Résultat
def converti_resultat():
    hexaoutput.set("")
    binoutput.set("")
    controlconcat.ccdec(deciresult, bool(True))


#Initialisation de la Form
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


#Gère la fermeture de la Form
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


#Lancement de la Form
if __name__ == '__main__':
    import convertisseur
    convertisseur.vp_start_gui()




