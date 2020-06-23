# Contient les différente listes et dictionnaires
# nécessaire à la bonne éxecution du programme
import sys
import operator

hexa = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

decimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

operation = ["+", "-", "/", "%", "*", "(", ")"]

binaire = ["0", "1"]

hexadict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13,
            "E": 14, "F": 15}



#Liste des alphanum gérés par le format Hexadécimal et ses valeurs retournées
hex_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D',
           14: 'E', 15: 'F'}

#Listre des Caractéres Hexadécimaux et leurs valeurs binaire retournés
bin_map = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
           "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}