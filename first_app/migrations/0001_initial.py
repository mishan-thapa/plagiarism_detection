# Generated by Django 4.1.5 on 2023-02-01 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_file', models.FileField(upload_to='')),
                ('second_file', models.FileField(upload_to='')),
            ],
        ),
    ]
