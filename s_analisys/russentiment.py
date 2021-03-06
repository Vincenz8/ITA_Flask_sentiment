# Vincenzo Russotto

# standard libraries
import string
import unicodedata
import os

"""This script contains a class called Russentiment that contain some static methods 
for calculating polarity of a text written in Italian
"""

class Russentiment:
    """This class calculate the polarity of a text written in Italian
    """
    @staticmethod
    def cleaned_text(text: str)->list:
        """Return the tokenized text without punctuation and numbers

        Args:
            text (str): text 

        Returns:
            list: tokenized text
        """
        text = text.lower()
        text = text.translate(str.maketrans("","",string.punctuation))
        text = text.translate(str.maketrans("","",string.digits))
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        text = text.split()
        return text

    @staticmethod
    def polarity_text(text: list):
        """Return polarity of the text

        Args:
            text (list): tokenized text 

        Returns:
            tuple(int, int, int): polarity
        """
        # get dataset
        dataset_words = open("./s_analisys/dataset/words.csv","r").read()
        dataset_words = dataset_words.splitlines()
        # count the number of 
        # positive, negative, neutral word
        negative_w = 0
        positive_w = 0
        neutral_w = 0
        for word in text:
            for raw in dataset_words:
                polarity, dataset_w = raw.split(sep=",")
                if word == dataset_w:
                    if polarity == "positive":
                        positive_w += 1
                    elif polarity == "negative":
                        negative_w += 1
                    else:
                        neutral_w+= 1
        return positive_w, negative_w, neutral_w

    @staticmethod
    def result(text_w: tuple)->int:
        """Output based on polarity of the text

        Args:
            text_w (tuple): polarity of the text

        Returns:
            int: return 1 if positive or 0 if negative
        """
        if text_w[0]>text_w[1]:
            return 1
        elif text_w[1]>text_w[0]:
            return 0

if __name__ == "__main__":
    # test 
    algo = Russentiment()
    
    text = """Questo libro ?? molto bello ed emozionante"""
    text2 = """Questo libro non mi ?? piaciuto, era noioso e brutto"""
    
    print(f"First text: \n{text}")
    print(f"Second text: \n{text2}")
    
    text = algo.cleaned_text(text)
    text2 = algo.cleaned_text(text2)
    text1_w = algo.polarity_text(text)
    text2_w = algo.polarity_text(text2)

    print(text1_w)
    print(text2_w)

    print(f"The first text is {algo.result(text1_w)}")
    print(f"The second text is {algo.result(text2_w)}")
    
    