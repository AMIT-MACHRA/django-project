# Generated by Django 4.1 on 2022-09-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=200)),
                ('PhoneNumber', models.CharField(max_length=300)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]
