from rest_framework import serializers
from .models import filesModel, userData


class fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = filesModel
        fields = "__all__"


class userDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = "__all__"
