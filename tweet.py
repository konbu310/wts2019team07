import math
import random
from collections import defaultdict
import tweepy

consumer_key = 'yffvpQmXpj13sittanWNKTulm'
consumer_secret = 'VCQyGpFLx7YmFUZkXo8k91Cqstoo4SmRpE8ZxzobMTbPOqEF2H'
access_token = '1214403479503900673'
access_token_secret = 'VVccckXRBODCspZRU4Gbjg1nmToosMEWiXz69giTICT1p'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

dict = defaultdict(list)


def create_dataset(path):
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
            dict[prev].append(now)
    for index, key in enumerate(dict):
        dict[key] = list(set(dict[key]))


def sample(word):
    words = dict[word]
    if words == None:
        return None
    else:
        return random.choice(words)


def generate():
    sentence = []
    word = sample(None)
    while word:
        sentence.append(word)
        word = sample(word)
    return "".join(sentence)


create_dataset("musuka.txt.mecab")

text = generate()

# ツイートを送信
try:
    api.update_status(status=text)
except tweepy.TweepError as e:
    print(e)
