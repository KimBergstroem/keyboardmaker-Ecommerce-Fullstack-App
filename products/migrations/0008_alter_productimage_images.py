# Generated by Django 3.2.23 on 2023-12-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20231207_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.FileField(upload_to=''),
        ),
    ]
