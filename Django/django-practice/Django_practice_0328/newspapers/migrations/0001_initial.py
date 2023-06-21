# Generated by Django 3.2.18 on 2023-03-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('journalist', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
