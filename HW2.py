import numpy as np
import pandas as pd
from collections import defaultdict


def scavenger_hunt() -> dict:
    #read the file into a dataframe
    df = pd.read_csv('wine.csv')
    #calculate dimensions of the dataframe
    answer0 = df.shape #(178, 15)
    #calculate avg alcohol content over all wines
    answer1 = df['alcohol'].mean()
    #calculate the st. dev. of magnesium content
    answer2 = df['magnesium'].std()
    #mean alcohol content grouped by target and displayed as a list
    answer3 = df.groupby(['target']).mean()['alcohol'].tolist()
    #minimum proline content and maximum proline content
    answer4 = [(df['proline'].min()), (df['proline'].max())]
    #identify # rows in dataset have malic_acid content > 2.5
    answer5 = len(df[df['malic_acid'] > 2.5])
    #identify index of wine with lowest flavanoid content
    answer6 = df['flavanoids'].idxmin()
    #identify num of unique hue vals in dataset
    answer7 = len(df['hue'].unique())

    #all answers to scavenger hunt in dictionary
    answers = {0: answer0, 1: answer1, 2: answer2, 3: answer3, 4: answer4, 5: answer5, 6: answer6, 7: answer7}
    #return dictionary
    return answers

#load the data from a given text file into memory
def get_words(file_path) -> list:
    pass


def get_ngrams(words, size) -> list:
    pass


def get_counts(n_grams) -> dict:
    pass


def generate_gram(counts, context) -> tuple:
    pass


def generate_sentence(counts, context, length=10) -> list:
    pass


def stringify(sentence) -> list:
    return " ".join("".join(gram[0]) for gram in sentence)


if __name__ == '__main__':
    # # create model
    # words = get_words('corpus.txt')
    # n_grams = get_ngrams(words, 1)
    # counts = get_counts(n_grams)

    # # generate text
    # context = n_grams[np.random.choice(len(n_grams))]
    # sentence = generate_sentence(counts, context, length=50)
    # print(stringify(sentence))


    # scavenger_hunt()