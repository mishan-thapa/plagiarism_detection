#from rest_framework import serializers
from .models import words

#class pos_sentence_serializer(serializers.ModelSerializer):
#    class Meta:
#        model = pos_sentence
#        fields = '__all__'  # You can specify specific fields here if needed
#

from rest_framework import serializers

class pos_sentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = words
        fields = ["sentence"]
