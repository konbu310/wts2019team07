import math
from random import random
from collections import defaultdict


class MarkovChain:
    def __init__(self, path):
        self.__dict = defaultdict(list)
        self.__create_dataset(path)

    def __create_dataset(self, path):
        words_set = []
        tmp = []
        for line in open(path, "r"):
            line = line.rstrip()
            if line == "EOS":
                words_set.append(tmp)
                tmp = []
                pass
            else:
                lis = line.split("\t")
                word = lis[0]
                tmp.append(word)
        for words in words_set:
            for i in range(len(words) + 1):
                now = None
                if i < len(words):
                    now = words[i]
                prev = None
                if i != 0:
                    prev = words[i-1]
                self.__dict[prev].append(now)

    def __sample(self, word):
        words = self.__dict[word]
        if words == None:
            words = []
        return words[math.floor(random() * len(words))]

    def generate(self):
        sentence = []
        word = self.__sample(None)
        while word:
            sentence.append(word)
            word = self.__sample(word)
        return "".join(sentence)
