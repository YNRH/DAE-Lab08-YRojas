from rest_framework import serializers
from .models import Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')


'''
from rest_framework import serializers
from .models import TuModelo

class TuModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuModelo
        fields = '__all__'

'''