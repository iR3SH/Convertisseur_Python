import convertisseur_support
from controlconcat import *
import controlconcat
from convertisseur_support import *
from dict import *
from polonais import *
import polonais


    ######################################################################################################################################################
    ###############################                         Déclarations des variables qui seront retournées
    ######################################################################################################################################################

global inputbininter
inputbininter = ""
inputdecinter = ""
inputhexinter = ""


def dectobin (calcchaindec1, decchain, inputbininter, isforcalc, isforcalc2) :

    #######################################################################################################################################################
    ###############################                        Déclaration des variables
    #######################################################################################################################################################


    #######################################################################################################################################################
    ###############################                               Conversion
    #######################################################################################################################################################

    for i in range (len(calcchaindec1)) :                 # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchaindec1[i] in decchain :                   # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            inp = int(calcchaindec1[i])                     # Conversion en int pour les calculs
            bininter = ""                                  # Création d'une variable intermédiaire pour ce bout de chaîne spécifique
            while inp >= 1 :                               # Contrôle de la fin de conversion
                if inp % 2 == 0 :       
                    inp //= 2                              # Division par 2 pour le calcul suivant
                    bininter += "0"                        # Ajout de la valeur binaire dans la variable bininter
                else :           
                    inp //= 2                              # Division par 2 pour le calcul suivant
                    bininter += "1"                        # Ajout de la valeur binaire dans la variable bininter
            bininter = bininter[::-1]                     # Invertion de la chaîne pour remettre les caractères dans le bon ordre
            calcchaindec1[i] = bininter                    # Remplacement dans la variable intermédiaire

    for i in range (len(calcchaindec1)) :                # Parcours du tableau de manipulations
        inputbininter += calcchaindec1[i]                       # Ajout en str à la variable de sortie

    inputbin = inputbininter

    print(inputbin)
    print(inputbininter)
    if isforcalc == bool(False):
        if isforcalc2 == bool(False):
            convertisseur_support.bin.set("")
            convertisseur_support.bin.set(inputbin)
        else:
            convertisseur_support.binoutput.set("")
            convertisseur_support.binoutput.set(inputbin)
            convertisseur_support.deciresult = ""
    else:
        convertisseur_support.bin.set("")
        convertisseur_support.bin.set(inputbin)


def bintodec (calcchainbin1, binchain, inputdecinter, iscalc) :

    #######################################################################################################################################################
    ###############################                                Conversion
    #######################################################################################################################################################

    for i in range(len(calcchainbin1)) :                 # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchainbin1[i] in binchain :                   # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            inp = (calcchainbin1[i])                        # Variable prenant contenant la chaîne à convertir
            decinter = 0                                   # Création d'une variable intermédiaire int à retourner dans la châine
            inp = inp[::-1]                                # Inversion de la chaîne pour effectuer les calculs
            for number in range(0, len(inp)) :            # Parcours complet de la chaîne
                if inp[int(number)] == "1":                # Calcul uniquement lorsque ce bit vaut '1'
                    decinter += (1*(2**int(number)))       # Ajout successif à la valeur intermédiaire
            calcchainbin1[i] = str(decinter)                   # Remplacement dans la variable intermédiaire

    for i in range(len(calcchainbin1)) :                # Parcours du tableau de manipulations
        inputdecinter += calcchainbin1[i]                       # Ajout en str à la variable de sortie
    inputdec = inputdecinter
    
    print(inputdec)
    print(inputdecinter)
    if iscalc == bool(False) :
        convertisseur_support.deci.set(inputdec)
    else:
        convertisseur_support.deci.set(inputdec)
        controlconcat.ccdec(inputdecinter, bool(False))


def dectohex (calcchaindec1, decchain, inputhexinter, isforcalc, isforcalc2) :

    #######################################################################################################################################################
    ###############################                                Conversion
    #######################################################################################################################################################

    for i in range(len(calcchaindec1)) :                 # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchaindec1[i] in decchain :                   # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            inp = int(calcchaindec1[i])                     # Conversion en int pour les calculs
            hexinter = ""                                  # Création d'une variable intermédiaire pour ce bout de chaîne spécifique
            while inp != 0 :                               # Contrôle de fin de conversion
                remind = inp % 16                          # Calcul du reste
                inp //= 16                                 # Division entière
                hexinter += hexa[remind-1]                 # Ajout de la valeur hexa à la chaine de caractère
            hexinter = hexinter[::-1]                     # Invertion de la chaîne pour remettre les caractères dans le bon ordre
            calcchaindec1[i] = hexinter                    # Remplacement dans la variable intermédiaire

    for i in range(len(calcchaindec1)) :                # Parcours du tableau de manipulations
        inputhexinter += calcchaindec1[i]                       # Ajout en str à la variable de sortie
    inputhex = inputhexinter
    print(inputhex)
    print(inputhexinter)
    if isforcalc == bool(False):
        if isforcalc2 == bool(False):
            convertisseur_support.hexad.set("")
            convertisseur_support.hexad.set(inputhex)
        else:
            convertisseur_support.hexaoutput.set("")
            convertisseur_support.hexaoutput.set(inputhex)
    else:
        convertisseur_support.hexad.set("")
        convertisseur_support.hexad.set(inputhex)


def hextodec (calcchainhex1, hexchain, inputdecinter, isforcalc) :
    #######################################################################################################################################################
    ###############################                              Conversions
    #######################################################################################################################################################
    global dec
    for i in range(len(calcchainhex1)) :                        # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchainhex1[i] in hexchain :                       # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            dec = 0                                             # Variable de calcul
            inp = calcchainhex1[i]                              # Variable intermédiaire contenant la valeur contenue dans les deux tableaux
            inp = inp[::-1]                                     # Inversion de la chaîne pour les calculs
            for elem in range(len(inp)) :                      # Parcours de la premiere valeur
                if inp[elem] in hexa :                          # Contrôle du fait que ce soit un caractère autorisé hexa
                    dec += ((hexadict[inp[elem]]) * (16 ** elem)) # On effectue le calcul après avoir récupérer la valeur dec dans le dictionnaire
            calcchainhex1[i] = str(dec)                         # Remplacement dans la variable intermédiaire

    for i in range(len(calcchainhex1)) :       # Parcours du tableau de manipulations
        inputdecinter += calcchainhex1[i]      # Ajout en str à la variable de sortie
    inputdec = inputdecinter

    print(inputdec)
    print(inputdecinter)
    if isforcalc == bool(False):
        convertisseur_support.deci.set(inputdec)
    else:
        convertisseur_support.deci.set(inputdec)
        controlconcat.ccdec(inputdecinter, bool(False))


def bintohex(calcchainbin1, binchain, inputhexinter, isforcalc):
    #######################################################################################################################################################
    ###############################                                Conversion
    #######################################################################################################################################################

    for i in range(len(calcchainbin1)):  # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchainbin1[i] in binchain and calcchainbin1[i] not in operation:  # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            inp = (calcchainbin1[i])  # Variable prenant contenant la chaîne à convertir
            hexinter = 0  # Création d'une variable intermédiaire int à retourner dans la châine
            inp = inp[::-1]  # Inversion de la chaîne pour effectuer les calculs
            for number in range(0, len(inp)):  # Parcours complet de la chaîne
                if inp[int(number)] == "1":  # Calcul uniquement lorsque ce bit vaut '1'
                    hexinter += (1 * (2 ** int(number)))  # Ajout successif à la valeur intermédiaire
            calcchainbin1[i] = str(hexinter)  # Remplacement dans la variable intermédiaire

    for i in range(len(calcchainbin1)):  # Parcours du tableau de manipulations
        inputhexinter += calcchainbin1[i]  # Ajout en str à la variable de sortie

    inputhex = inputhexinter
    #Conversion vers hexadécimal
    inputhexinter2 = ""
    for i in range(len(calcchainbin1)):  # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchainbin1[i] in inputhex and calcchainbin1[i] not in operation:  # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            inp = int(calcchainbin1[i])  # Conversion en int pour les calculs
            hexinter = ""  # Création d'une variable intermédiaire pour ce bout de chaîne spécifique
            while inp != 0:  # Contrôle de fin de conversion
                remind = inp % 16  # Calcul du reste
                inp //= 16  # Division entière
                hexinter += hexa[remind - 1]  # Ajout de la valeur hexa à la chaine de caractère
            hexinter = hexinter[::-1]  # Invertion de la chaîne pour remettre les caractères dans le bon ordre
            calcchainbin1[i] = hexinter  # Remplacement dans la variable intermédiaire

    for i in range(len(calcchainbin1)):  # Parcours du tableau de manipulations
        inputhexinter2 += calcchainbin1[i]  # Ajout en str à la variable de sortie
    inputhex = inputhexinter2
    print(inputhex)
    print(inputhexinter2)
    if isforcalc == bool(False):
        convertisseur_support.hexad.set(inputhex)
    else:
        convertisseur_support.hexad.set(inputhexinter2)

def hextobin(calcchainhex1, hexchain, inputbininter, isforcalc) :
    #######################################################################################################################################################
    ###############################                              Conversions
    #######################################################################################################################################################
    global dec
    for i in range(len(calcchainhex1)):  # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchainhex1[i] in hexchain:  # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            dec = 0  # Variable de calcul
            inp = calcchainhex1[i]  # Variable intermédiaire contenant la valeur contenue dans les deux tableaux
            inp = inp[::-1]  # Inversion de la chaîne pour les calculs
            for elem in range(len(inp)):  # Parcours de la premiere valeur
                if inp[elem] in hexa:  # Contrôle du fait que ce soit un caractère autorisé hexa
                    dec += ((hexadict[inp[elem]]) * (
                                16 ** elem))  # On effectue le calcul après avoir récupérer la valeur dec dans le dictionnaire
            calcchainhex1[i] = str(dec)  # Remplacement dans la variable intermédiaire

    for i in range(len(calcchainhex1)):  # Parcours du tableau de manipulations
        inputbininter += calcchainhex1[i]  # Ajout en str à la variable de sortie
    inputbin = inputbininter
    #Conversion vers Binaire
    inputbininter2 = ""
    for i in range(len(calcchainhex1)) :                 # Parcours de la chaîne retournée par controlconcat.ccdec
        if calcchainhex1[i] in inputbin :                # Vérification de du fait que calchaindec[i] est bien une valeur à convertir et pas un opérateur
            if calcchainhex1[i] not in operation:
                inp = int(calcchainhex1[i])                     # Conversion en int pour les calculs
                bininter = ""                                  # Création d'une variable intermédiaire pour ce bout de chaîne spécifique
                while inp >= 1 :                               # Contrôle de la fin de conversion
                    if inp % 2 == 0 :
                        inp //= 2                              # Division par 2 pour le calcul suivant
                        bininter += "0"                        # Ajout de la valeur binaire dans la variable bininter
                    else :
                        inp //= 2                              # Division par 2 pour le calcul suivant
                        bininter += "1"                        # Ajout de la valeur binaire dans la variable bininter
                bininter = bininter[::-1]                     # Invertion de la chaîne pour remettre les caractères dans le bon ordre
                calcchainhex1[i] = bininter                    # Remplacement dans la variable intermédiaire

    for i in range(len(calcchainhex1)) :                # Parcours du tableau de manipulations
        inputbininter2 += calcchainhex1[i]                       # Ajout en str à la variable de sortie

    inputbin = inputbininter2

    print(inputbin)
    print(inputbininter2)
    if isforcalc == bool(False):
        convertisseur_support.bin.set(inputbin)
    else:
        convertisseur_support.bin.set(inputbininter2)

