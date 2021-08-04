# Vincenzo Russotto

# librerie builtin
import string
import unicodedata
import os

# classe che contiene l'algoritmo di sentiment analisys
class Russentiment:
    """Classe che restituisce la polarità di un testo
    """
    @staticmethod
    def testo_pulito(testo: str)->list:
        """Restituisce la versione tokenizzata e ripulita del test in input

        Args:
            testo (str): testo 

        Returns:
            list: lista tokenizzata del testo
        """
        # pulisce il testo dai numeri, punteggiatura
        # conversione di lettere accentate
        # rende tutto minuscolo
        testo = testo.lower()
        testo = testo.translate(str.maketrans("","",string.punctuation))
        testo = testo.translate(str.maketrans("","",string.digits))
        testo = unicodedata.normalize('NFKD', testo).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        testo = testo.split()
        return testo

    @staticmethod
    def polarita_testo(testo: list):
        """Restituisce la polarita del testo

        Args:
            testo (list): testo tokenizzato

        Returns:
            tuple(int, int, int): polarita
        """
        # calcola il numero di parole positive, negative, neutrali
        dataset_parole = open("dataset/pulito.csv","r").read()
        dataset_parole = dataset_parole.splitlines()
        p_negative = 0
        p_positive = 0
        p_neutrali = 0
        for parola in testo:
            for riga in dataset_parole:
                polarita, p_dataset = riga.split(sep=",")
                if parola == p_dataset:
                    if polarita == "positive":
                        p_positive += 1
                    elif polarita == "negative":
                        p_negative += 1
                    else:
                        p_neutrali+= 1
        return p_positive, p_negative, p_neutrali

    @staticmethod
    def predizione(p_testo: tuple)->str:
        """Predizione in base alla polarita del testo

        Args:
            p_testo (tuple): polarita del testo

        Returns:
            str: predizione
        """
        if p_testo[0]>p_testo[1]:
            return "positiva"
        elif p_testo[1]>p_testo[0]:
            return "negativa"
        else:
            return ""

if __name__ == "__main__":
    # test dell'algoritmo
    algo = Russentiment()

    text = """Questo libro è molto bello ed emozionante"""
    text2 = """Questo libro non mi è piaciuto, era noioso e brutto"""

    text = algo.testo_pulito(text)
    text2 = algo.testo_pulito(text2)
    p_testo1 = algo.polarita_testo(text)
    p_testo2 = algo.polarita_testo(text2)

    print(p_testo1)
    print(p_testo2)

    print(f"Il primo testo è {algo.predizione(p_testo1)}")
    print(f"Il secondo testo è {algo.predizione(p_testo2)}")
    
    