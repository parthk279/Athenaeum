"""
Model serializers
"""
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):  #A model serializer for Book class that contains all the associated variables 
    """ Serializer for Book model """
    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'isbn', 'description', 'condition', 'price', 'link_to_buy', 'is_in_stock')
