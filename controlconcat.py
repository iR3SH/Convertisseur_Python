from dict import *
from conversion import *
from polonais import *
import polonais
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk



    ######################################################################################################################################################
    ###############################                         Listes de stockage
    ######################################################################################################################################################

decope = []                                                                        # Liste qui contiendra les opérateurs trouvés dans l'input
decchain = []                                                                      # Liste qui contiendra les chaînes de valeur trouvées dans l'input
calcchaindec = []                                                                  # Liste utilisée par la calculette
calcchaindec2 = []                                                                 # Nécéssaire pour les deux conversions
decchain2 =[]                                                                      # Nécéssaire pour les deux conversions

binope = []                                                                        # Liste qui contiendra les opérateurs trouvés dans l'input
binchain = []                                                                      # Liste qui contiendra les chaînes de valeur trouvées dans l'input
binchain2 = []
calcchainbin = []                                                                  # Liste utilisée par la calculette
calcchainbin2 = []

hexope = []                                                                        # Liste qui contiendra les opérateurs trouvés dans l'input
hexchain = []                                                                      # Liste qui contiendra les chaînes de valeur trouvées dans l'input
hexchain2 = []
calcchainhex = []                                                                  # Liste utilisée par la calculette
calcchainhex2 = []

result = ""


def ccdec (inputdec, isforcalc) :      # Fonction de contrôle de saisie, de concaténation décimal

    count = 0                                                # Variable permettant le parcours de la chaîne
           

    #######################################################################################################################################################
    ###############################                        Variables d'indices
    #######################################################################################################################################################   
    
    opeindice = 0                                           # Variable de gestion des indices de la liste des opérateurs trouvés
    chainindice = 0                                         # Variable de gestion des indices de la liste des chaînes de valeur trouvées

    #######################################################################################################################################################
    ###############################                        Variables intermédiaires
    #######################################################################################################################################################

    interchain = ""                                         # Variable intermédiaire de stockage de la chaîne

    #######################################################################################################################################################
    ###############################                         Parcours de la chaîne et enregistrements dans les listes
    #######################################################################################################################################################        
    while count < len(inputdec):
        car = inputdec[count]
        
        if car not in operation and car != " " :                                        # Parcours de la chaîne de caractère au complet et append en Chain
            if car in decimal :                                                         # Contrôle si le caractère appartient bien au bon type
                interchain += car                                                       # Si appartient au bon type, ajout à une première chaine      
                count += 1                                                              # Incrémentation pour passer à la lettre suivante
            else :
                typeerror = "Le caractère '" + car + "' n'est pas autorisé"             # Si ni opérateur, ni espace, ni in decimal, caractère non autorisé
                print(typeerror)                                                        # Renvoi de l'erreur
                fail(typeerror)                                                         # Message d'erreur
                break
        if car == " " :                                                                 # Gestion de la rupture while en cas d'espaces
            count += 1                                                                  # Incrémentation pour passer à la lettre suivante

        if car in operation :                                                           # Gestion de la rupture while en cas d'opérateur
            decope.append(car)                                                          # Enregistrement de l'opérateur dans la liste dédiée
            count += 1                                                                  # Incrémentation pour passer à la lettre suivante
            if interchain != "" :                                                       # Gestion du cas où le premier caractère n'est pas un opérateur
                decchain.append(interchain)                                             # Incrémentation pour passer à la lettre suivante
                decchain2.append(interchain)
                calcchaindec.append(interchain)                                         # Ajout à la liste référence calculette
                calcchaindec2.append(interchain)
                interchain = ""                                                         # Remise à zero pour prochaine série
            calcchaindec.append(car)                                                    # Ajout à la liste référence calculette
            calcchaindec2.append(car)                                                   # Ajout à la seconde liste ref cacl.

    if interchain != "" : 
        decchain.append(interchain)                                                    # Gestion du cas ou le dernier caratère n'est pas un opérateur
        decchain2.append(interchain)                                                   # """""""""""""""""""""""""""""
        calcchaindec.append(interchain)                                                # Ajout à la liste référence calculette
        calcchaindec2.append(interchain)                                               # """"""""""""""""""""""""""""""

    if isforcalc == bool(False):                         #Condition pour savoir si la requête viens d'un calcule
        if not decope:                           #Vérification s'il y a un opérateur enregistré
            dectohex(calcchaindec, decchain, inputhexinter, bool(False), bool(False))  #Retour vers la conversion
            dectobin(calcchaindec2, decchain2, inputbininter, bool(False), bool(False))  #Retour vers la conversion
        else:
            polonais.infixtopostfix(calcchaindec, decchain)  # Retour de la chaine vers le calcul
            dectohex(calcchaindec, decchain, inputhexinter, bool(True), bool(False))  # Retour vers la conversion
            dectobin(calcchaindec2, decchain2, inputbininter, bool(True), bool(False))  # Retour vers la conversion
    else:
        dectohex(calcchaindec, decchain, inputhexinter, bool(False), bool(True))  # Retour vers la conversion
        dectobin(calcchaindec2, decchain2, inputbininter, bool(False), bool(True))  # Retour vers la conversion

    calcchaindec.clear()                 #On reset la variable une fois la conversion terminée pour eviter les surchages
    calcchaindec2.clear()                #Reset de la Variable (sécurité)
    decchain.clear()                     #Reset de la Variable (sécurité)
    decchain2.clear()                    #Reset de la Variable (sécurité)
    decope.clear()                       #Reset de la Variable (sécurité)


def ccbin (inputbin) :                                                                          # Fonction de contrôle de saisie, de concaténation décimal

    count = 0                                                                                   # Variable permettant le parcours de la chaîne

    #######################################################################################################################################################
    ###############################                        Variables d'indices
    #######################################################################################################################################################   
    
    opeindice = 0                                                              # Variable de gestion des indices de la liste des opérateurs trouvés
    chainindice = 0                                                            # Variable de gestion des indices de la liste des chaînes de valeur trouvées

    #######################################################################################################################################################
    ###############################                        Variables intermédiaires
    #######################################################################################################################################################

    interchain = ""                                                                                       # Variable intermédiaire de stockage de la chaîne 

    #######################################################################################################################################################
    ###############################                         Parcours de la chaîne et enregistrements dans les listes
    #######################################################################################################################################################        
    while count < len(inputbin) :
        car = inputbin[count]
        
        if car not in operation and car != " " :                                        # Parcours de la chaîne de caractère au complet et append en Chain
            if car in binaire :                                                         # Contrôle si le caractère appartient bien au bon type
                interchain += car                                                       # Si appartient au bon type, ajout à une première chaine      
                count += 1                                                              # Incrémentation pour passer à la lettre suivante
            else :
                typeerror = "Le caractère '" + car + "' n'est pas autorisé"             # Si ni opérateur, ni espace, ni in decimal, caractère non autorisé
                print(typeerror)                                                        # Renvoi de l'erreur
                fail(typeerror)
                break

        if car == " " :                                                                 # Gestion de la rupture while en cas d'espaces
            count += 1                                                                  # Incrémentation pour passer à la lettre suivante                                     

        if car in operation :                                                           # Gestion de la rupture while en cas d'opérateur
            binope.append(car)                                                          # Enregistrement de l'opérateur dans la liste dédiée
            count += 1                                                                  # Incrémentation pour passer à la lettre suivante
            if interchain != "" :                                                       # Gestion du cas où le premier caractère n'est pas un opérateur
                binchain.append(interchain)                                             # Incrémentation pour passer à la lettre suivante
                binchain2.append(interchain)
                calcchainbin.append(interchain)                                         # Ajout à la liste référence calculette
                calcchainbin2.append(interchain)
                interchain = ""                                                         # Remise à zero pour prochaine série
            calcchainbin.append(car)                                                    # Ajout à la liste référence calculette
            calcchainbin2.append(car)

    if interchain != "" : 
        binchain.append(interchain)                                                    # Gestion du cas ou le dernier caratère n'est pas un opérateur
        binchain2.append(interchain)
        calcchainbin.append(interchain)                                                # Ajout à la liste référence calculette
        calcchainbin2.append(interchain)
    if not binope:                                                  #Vérification s'il y a un opérateur enregistré
        bintodec(calcchainbin, binchain, inputdecinter, bool(False))    #Retour vers la Conversion
        bintohex(calcchainbin2, binchain2, inputdecinter, bool(False))  #Retour vers la deuxième conversion
    else:
        bintodec(calcchainbin, binchain, inputdecinter, bool(True))  #Retour vers la conversion
        bintohex(calcchainbin2, binchain2, inputhexinter, bool(True))  #Retour vers la deuxième conversion
    calcchainbin.clear()                                              #Reset de la variable (sécurité)
    binchain.clear()                                                  #Reset de la variable (sécurité)
    binope.clear()                                                    #Reset de la variable (sécurité)
    calcchainbin2.clear()                                             #Reset de la variable (sécurité)
    binchain2.clear()                                                 #Reset de la variable (sécurité)


def cchex (inputhex) :                                                                         # Fonction de contrôle de saisie, de concaténation décimal

    count = 0                                                                                  # Variable permettant le parcours de la chaîne
         
    #######################################################################################################################################################
    ###############################                        Variables d'indices
    #######################################################################################################################################################   
    
    opeindice = 0                                                              # Variable de gestion des indices de la liste des opérateurs trouvés
    chainindice = 0                                                            # Variable de gestion des indices de la liste des chaînes de valeur trouvées

    #######################################################################################################################################################
    ###############################                        Variables intermédiaires
    #######################################################################################################################################################

    interchain = ""                                                                                       # Variable intermédiaire de stockage de la chaîne 

    #######################################################################################################################################################
    ###############################                         Parcours de la chaîne et enregistrements dans les listes
    #######################################################################################################################################################        
    while count < len(inputhex):
        car = inputhex[count]
        car = car.upper()                                                               # Pour éviter tout problème de mauvaise gestion de caractère

        if car not in operation and car != " " :                                        # Parcours de la chaîne de caractère au complet et append en Chain
            if car in hexa :                                                            # Contrôle si le caractère appartient bien au bon type
                interchain += car                                                       # Si appartient au bon type, ajout à une première chaine      
                count += 1                                                              # Incrémentation pour passer à la lettre suivante
            else :
                typeerror = "Le caractère '" + car + "' n'est pas autorisé"             # Si ni opérateur, ni espace, ni in decimal, caractère non autorisé
                print(typeerror)                                                        # Renvoi de l'erreur
                fail(typeerror)
                break

        if car == " " :                                                                 # Gestion de la rupture while en cas d'espaces
            count += 1                                                                  # Incrémentation pour passer à la lettre suivante                                     

        if car in operation :                                                           # Gestion de la rupture while en cas d'opérateur
            hexope.append(car)                                                          # Enregistrement de l'opérateur dans la liste dédiée
            count += 1                                                                  # Incrémentation pour passer à la lettre suivante
            if interchain != "" :                                                       # Gestion du cas où le premier caractère n'est pas un opérateur
                hexchain.append(interchain)                                             # Incrémentation pour passer à la lettre suivante
                hexchain2.append(interchain)
                calcchainhex.append(interchain)                                         # Ajout à la liste référence calculette
                calcchainhex2.append(interchain)
                interchain = ""                                                         # Remise à zero pour prochaine série
            calcchainhex.append(car)                                                    # Ajout à la liste référence calculette
            calcchainhex2.append(car)

    if interchain != "" : 
        hexchain.append(interchain)                                                    # Gestion du cas ou le dernier caratère n'est pas un opérateur
        hexchain2.append(interchain)
        calcchainhex.append(interchain)                                                # Ajout à la liste référence calculette
        calcchainhex2.append(interchain)

    if not hexope:                                          #Vérification s'il y a un opérateur enregistré
        hextodec(calcchainhex, hexchain, inputdecinter, bool(False))  #Retour vers la Conversion
        hextobin(calcchainhex2, hexchain2, inputdecinter, bool(False))  #Retour vers la deuxième conversion
    else:
        hextodec(calcchainhex, hexchain, inputdecinter, bool(True))  #Retour vers la Conversion
        hextobin(calcchainhex2, hexchain2, inputdecinter, bool(True))  #Retour vers la deuxième Conversion
    calcchainhex.clear()                    #Reset de la variable (sécurité)
    hexchain.clear()                        #Reset de la variable (sécurité)
    calcchainhex2.clear()                   #Reset de la variable (sécurité)
    hexchain2.clear()                       #Reset de la variable (sécurité)
    hexope.clear()                          #Reset de la variable (sécurité)


def fail(msgerr):                           #Fonction pour gérer les erreurs de caractère
    erreur = tk.Tk()
    MsgErreur = tk.Label(erreur, text=msgerr)
    MsgErreur.pack()
