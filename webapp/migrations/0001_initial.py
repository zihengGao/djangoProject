# Generated by Django 3.2.13 on 2022-05-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
            ],
        ),
    ]
