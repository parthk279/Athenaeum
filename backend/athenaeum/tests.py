"""
Backend unit tests
"""
from django.test import TestCase
from .models import Book

# Use this class to test all the attributes of book
class BookTestCase(TestCase):
    """ Unit tests for book """
    def setUp(self):
        """ Setting up Book object for tests """
        Book.objects.create(title="Test book", authors="Test authors")

    def test_author_persists(self):
        """ Testing book author """
        test_book = Book.objects.get(title="Test book")
        self.assertEqual(test_book.authors, "Test authors")

    def test_book_title_label(self):
        """ Testing book title label """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_book_authors_label(self):
        """ Testing author label """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('authors').verbose_name
        self.assertEqual(field_label, 'authors')

    def test_book_isbn_label(self):
        """ Testing book ISBN label """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'isbn')

    def test_book_description_label(self):
        """ Testing book description label """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_book_condition_label(self):
        """ Testing book condition label """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('condition').verbose_name
        self.assertEqual(field_label, 'condition')

    def test_book_price_label(self):
        """ Testing book price label """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_book_link_to_buy_label(self):
        """ Testing the link for purchase """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('link_to_buy').verbose_name
        self.assertEqual(field_label, 'link to buy')

    def test_book_is_in_stock_label(self):
        """ Testing the in-stock label """
        test_book = Book.objects.get(id=1)
        field_label = test_book._meta.get_field('is_in_stock').verbose_name
        self.assertEqual(field_label, 'is in stock')
        
