from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        today = datetime.date.today()
        year = today.strftime('%y')
        if data['publication_year'] > year:
            raise serializers.ValidationError("ERROR: the year can not be in the future")
        return data

class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields ="__all__"