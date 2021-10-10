import numpy as np
import pandas as pd
from collections import defaultdict


def scavenger_hunt() -> dict:
    #read the file into a dataframe
    df = pd.read_csv('wine.csv')
    #display the df
    print(df.shape)


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


    scavenger_hunt()