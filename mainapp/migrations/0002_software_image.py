# Generated by Django 4.0.1 on 2022-04-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='image',
            field=models.ImageField(default='media/soft.PNG', upload_to='media/software_profile'),
        ),
    ]
