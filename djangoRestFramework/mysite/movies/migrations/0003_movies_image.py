# Generated by Django 5.0.7 on 2024-09-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movies_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
