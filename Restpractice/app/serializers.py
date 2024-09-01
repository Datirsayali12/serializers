from rest_framework import serializers
from .models import *


def alphanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("the alphnumeric value required")

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[alphanumeric])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get("roll",instance.roll)
        instance.city=validated_data.get("city",instance.city)
        instance.save()
        return instance

    def validate_roll(self, value):  # Field-level validation
        if value < 0:
            raise serializers.ValidationError("Roll number must be greater than 0.")
        return value

    def validate(self, data):  # Object-level validation
        if data['name'] == data['city']:
            raise serializers.ValidationError("Name and city must be different.")
        return data


class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField()


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title=validated_data.get("title",instance.name)
        instance.author=validated_data.get("author",instance.author)
        instance.price=validated_data.get("price",instance.price)
        instance.save
        return instance

    def validate_price(self,value):
        if value < 0 :
            raise serializers.ValidationError("price should be greater than 0")

    def validate(self, data):
        if data['title']==data['author']:
            raise serializers.ValidationError("title and author name should not be same")






