# Generated by Django 4.1.1 on 2022-09-14 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athenaeum', '0002_books_description_books_isinstock'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
