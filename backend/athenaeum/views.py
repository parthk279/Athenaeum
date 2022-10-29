"""
Views
"""
from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password, check_password
from .serializers import BookSerializer
from .models import Book, Login

# Create your views here.

class BookView(viewsets.ModelViewSet):
    """ View for the Book model """
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Login and Encryption instructions from https://pythonguides.com/encrypt-and-decrypt-password-in-django/
def login(request):
    """ Login """
    if request.method == 'POST':
        email = request.POST['email']
        encryptedpassword=make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword=check_password(request.POST['password'], encryptedpassword)
        print(checkpassword)
        data=Login(email=email, password=encryptedpassword)

        data.save()
        return HttpResponse('Done')
    return render(request, 'index.html')
