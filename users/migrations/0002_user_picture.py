# Generated by Django 2.0.7 on 2018-07-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='img/blank-pic.png', upload_to='', verbose_name='Foto de perfil'),
        ),
    ]
