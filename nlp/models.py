import os

from django.db import models

# Create your models here.
from django.db import models
import gensim
import numpy as np
from honmakaina.settings import BASE_DIR
class Word2Vec(models.Model):
    first_word = models.CharField(max_length=20)
    second_word = models.CharField(max_length=20)
    distance = models.FloatField()
    minor_level = models.IntegerField()

    #distanceとlevelを算出する
    def _set_scores(self):
        print(self.first_word)
        flg,self.distance = W2V.calc_distance(self.first_word,self.second_word)
        self.minor_level = int((self.distance +1)*50)
        return flg

#w2vのクラス
class W2V():
    path = str(BASE_DIR) + "/data/nlp/ja.bin"
    model = gensim.models.Word2Vec.load(path)
    #距離を返す
    @staticmethod
    def calc_distance(word1,word2):
        try:
            return True, W2V.cos_sim(W2V.model[word1],W2V.model[word2])
        except:
            return False, 0

    @staticmethod
    def cos_sim(v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))