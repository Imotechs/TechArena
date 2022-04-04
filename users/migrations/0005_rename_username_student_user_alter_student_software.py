# Generated by Django 4.0.1 on 2022-04-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
        ('users', '0004_student_image_alter_student_software'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='username',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='student',
            name='software',
            field=models.ManyToManyField(blank=True, to='mainapp.Software'),
        ),
    ]
