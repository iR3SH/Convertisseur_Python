import operator
    #######################################################################################################################################################
    ###############################                              Déclaration des variables
    #######################################################################################################################################################
import convertisseur_support
from controlconcat import decchain, ccdec
from conversion import *

ope = {"+" : operator.add,
"-" : operator.sub,
"*" : operator.mul,
"/" : operator.floordiv,
"%" : operator.mod
}

prio = {"+" : 1, "-" : 1, "*" : 2, "/" : 2, "%" : 2}
operator = ["+", "-", "*", "/", "%"]
final = []
stack = []
pile = []

    #######################################################################################################################################################
    ###############################                              Infix To Postfix
    #######################################################################################################################################################


def infixtopostfix (calcchaindec, decchain) :
    stack = []
    print("calcchaindec = ", calcchaindec)
    print("decchain = ", decchain)
    for elem in range(len(calcchaindec)) :                                                        # Parcours complet de la chaîne d'entrée
        if calcchaindec[elem] in decchain :                                                        # Si valeur
            final.append(calcchaindec[elem])                                                       # Ajout à la liste finale
            print(final)
        if calcchaindec[elem] == "(" :                                                             # Si parenthèse ouverte
            stack.append(calcchaindec[elem])                                                       # On ajoute à stack en attendant la prochaine parenthèse
            print(stack)
        if calcchaindec[elem] == ")" :                                                             # Si parenthèse fermée
            stackinv = stack[::-1]                                                                 # On inverse le stack pour faciliter le parcours
            while stackinv[0] != "(" :                                                             # Tant que l'élément n'est pas une parenthèse ouvrant
                final.append(stackinv[0])                                                          # On ajoute l'opérateur à final
                del(stackinv[0])                                                                   # On le supprime de stack
            del(stackinv[0])                                                                       # Sortie du while, donc parenthèse ouvrante, donc on supprime
            stack = stackinv[::-1]                                                                 # On actualise stack
        if calcchaindec[elem] in operator :                                                        # Si elem est un opérator
            if len(stack) < 1 or stack[-1] == "(" :                                                # Si la liste d'opérator est vide ou dernier élément = parenthèse ouvrante
                stack.append(calcchaindec[elem])                                                   # Ajout de l'opérateur à stack
                print(stack)
            else :
                if prio[stack[-1]] < prio[calcchaindec[elem]] :                                    # Opérateur top stack prio plus faible opé à rajouter à stack
                    stack.append(calcchaindec[elem])                                               # Ajout au stack
                    print(stack)
                else :
                    while len(stack) > 0 and prio[calcchaindec[elem]] <= prio[stack[-1]] :         # opérateur prio sup ou = op top stack
                        final.append(stack[-1])                                                    # Ajout du top stack a final chain
                        print(stack)
                        print(final)
                        del(stack[-1])                                                             # Suppression de la valeur qu'on vient de bouger
                        print(stack)
                    stack.append(calcchaindec[elem])                                               # Ajout au stack
                    print(stack)

    for i in range(len(stack)) :                                                                  # On append le reste de la liste au stack à la fin
        final.append(stack[-1])
        del(stack[-1])
    calcul(final, decchain)
    print(final)
    final.clear()
    stack.clear()

    #######################################################################################################################################################
    ###############################                              Calculatrice POLONAISE SUKA
    #######################################################################################################################################################


def calcul(final, decchain) :
    for elem in range(len(final)) :                                                                # Parcours de la chaîne finales
        if final[elem] in decchain :                                                               # Si opérande
            pile.append(final[elem])                                                               # Ajout à la pile
            print(pile)
        if final[elem] in operator :                                                               # Si opérateur
            val1 = pile[-2]                                                                        # Valeur intermédiaire 1
            print(val1)
            val2 = pile[-1]                                                                        # Valeur intermédiaire 2
            print(val2)
            if (final[elem] == "/" or final[elem] == "%" ) and val2 == 0 :                         # Gestion de la division par zero
                Error = "Pas de division par Zero! Dumb fuck!"
                return Error
            val = ope[final[elem]](int(val1) , int(val2))                                          # On effectue le calcul
            del(pile[-2])                                                                          # On enlève la première valeur ayant servie au calcul    
            print(pile)
            pile[-1] = val                                                                         # On y intègre la valeur trouvée
            print(pile)
    convertisseur_support.decimaloutput.set(pile)                                                  #Envoie à l'entry
    convertisseur_support.deciresult = str(pile[0])
    pile.clear()
