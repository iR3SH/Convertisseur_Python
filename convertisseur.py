#Importation des ressources
import sys

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

import convertisseur_support


#Lancement de la forme et prise en compte des composants
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    convertisseur_support.set_Tk_var()
    top = Toplevel1(root)
    convertisseur_support.init(root, top)
    root.mainloop()


#Variable Write
w = None


#Création de la Form et de ses composants
def create_Toplevel1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    convertisseur_support.set_Tk_var()
    top = Toplevel1 (w)
    convertisseur_support.init(w, top, *args, **kwargs)
    return w, top


#Destruction des composants en cas de fermeture
def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


#Configuration des composants
class Toplevel1:
    def __init__(self, top=None):
        '''Cette class configure et peuple le toplevel window. top est le toplevel contenu dans la fenêtre.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor, foreground=_fgcolor, font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("729x314+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Convertisseur")
        top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.014, rely=0.032, height=26, width=61)
        self.Label1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Décimal''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.014, rely=0.35, height=26, width=93)
        self.Label2.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Hexadécimal''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.014, rely=0.669, height=26, width=52)
        self.Label3.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Binaire''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.535, rely=0.032, height=26, width=61)
        self.Label4.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''Décimal''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.535, rely=0.35, height=26, width=93)
        self.Label5.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''Hexadécimal''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.535, rely=0.669, height=26, width=52)
        self.Label6.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''Binaire''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.014, rely=0.127,height=24, relwidth=0.486)
        self.Entry1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightcolor="black")
        self.Entry1.configure(highlightbackground="#d9d9d9", insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry1.configure(textvariable=convertisseur_support.deci)

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.014, rely=0.446,height=24, relwidth=0.486)
        self.Entry2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightcolor="black")
        self.Entry2.configure(highlightbackground="#d9d9d9", insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry2.configure(textvariable=convertisseur_support.hexad)

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.014, rely=0.764,height=24, relwidth=0.486)
        self.Entry3.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightcolor="black")
        self.Entry3.configure(highlightbackground="#d9d9d9", insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry3.configure(textvariable=convertisseur_support.bin)

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.535, rely=0.127,height=24, relwidth=0.458)
        self.Entry4.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", insertbackground="black")
        self.Entry4.configure(textvariable=convertisseur_support.decimaloutput)

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.535, rely=0.446, height=24, relwidth=0.458)
        self.Entry5.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", insertbackground="black")
        self.Entry5.configure(textvariable=convertisseur_support.hexaoutput)

        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.535, rely=0.764, height=24, relwidth=0.458)
        self.Entry6.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", insertbackground="black")
        self.Entry6.configure(textvariable=convertisseur_support.binoutput)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.014, rely=0.86, height=33, width=356)
        self.Button1.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", pady="0")
        self.Button1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Convertir / Calculer''')
        self.Button1.configure(command=convertisseur_support.convert_bin)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.014, rely=0.541, height=33, width=356)
        self.Button2.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", pady="0")
        self.Button2.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Convertir / Calculer''')
        self.Button2.configure(command=convertisseur_support.convertir_hex)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.014, rely=0.223, height=33, width=356)
        self.Button3.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", pady="0")
        self.Button3.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Convertir / Calculer''')
        self.Button3.configure(command=convertisseur_support.convertir_deci)

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.535, rely=0.223, height=33, width=336)
        self.Button4.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", pady="0")
        self.Button4.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''Convertir''')
        self.Button4.configure(command=convertisseur_support.converti_resultat)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.521, rely=0.032, relheight=0.924)
        self.TSeparator1.configure(orient="vertical")


#Lancement de l'interface graphique
if __name__ == '__main__':
    vp_start_gui()





