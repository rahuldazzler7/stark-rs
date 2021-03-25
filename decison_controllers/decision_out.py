import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
import random
from train_stark.model_trainer import TrainBot
from os import environ as env

stemmer = LancasterStemmer()


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)
