# Generated by Django 3.2.18 on 2023-04-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('모든글', '모든글'), ('개발', '개발')], max_length=20),
        ),
    ]
