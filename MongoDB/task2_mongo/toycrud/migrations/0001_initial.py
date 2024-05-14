# Generated by Django 4.1.13 on 2024-05-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=10, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
