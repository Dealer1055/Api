from rest_framework import serializers
from .models import Author, Genre, Book
from datetime import date

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField(required=False, allow_null=True)

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Ism kamida 3 harfdan iborat bo‘lishi kerak.")
        return value

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.save()
        return instance

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Janr faqat harflardan iborat bo‘lishi kerak.")
        return value

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    published_date = serializers.DateField()
    price = serializers.DecimalField(max_digits=15, decimal_places=2)

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Narx 0 dan katta bo‘lishi kerak.")
        return value

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Nashr sanasi kelajakda bo‘lishi mumkin emas.")
        return value

    def validate(self, data):
        if data['title'].lower() == data['author'].name.lower():
            raise serializers.ValidationError("Kitob nomi muallif ismiga teng bo‘lmasligi kerak.")
        return data

    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        book = Book.objects.create(**validated_data)
        book.genre.set(genre_data)
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.price = validated_data.get('price', instance.price)
        if 'genre' in validated_data:
            instance.genre.set(validated_data['genre'])
        instance.save()
        return instance
