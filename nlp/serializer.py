from rest_framework import serializers

from .models import Word2Vec
from rest_framework.exceptions import UnsupportedMediaType

class Word2VecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word2Vec
        fields = ['first_word', 'second_word','distance','minor_level']

    # saveとは save処理を行わない #create or updateをいい感じに呼び出すメソッド

    #create ではsaveしてインスタンスを返す
    def create(self, validated_data):
        word2vec = Word2Vec(first_word=validated_data["first_word"],
                            second_word=validated_data["second_word"],
                            distance = 0.0,
                            minor_level = 0,
                            )
        flg = word2vec._set_scores()
        if not flg:
            raise UnsupportedMediaType('登録されていない単語')
        return word2vec