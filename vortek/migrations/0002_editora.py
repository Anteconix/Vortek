# Generated by Django 5.1.7 on 2025-03-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vortek', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
