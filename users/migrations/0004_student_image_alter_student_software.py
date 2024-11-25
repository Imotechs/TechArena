# Generated by Django 4.0.1 on 2022-04-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='media/default.PNG', upload_to='media/profile_pics'),
        ),
        migrations.AlterField(
            model_name='student',
            name='software',
            field=models.ManyToManyField(null=True, to='mainapp.Software'),
        ),
    ]
