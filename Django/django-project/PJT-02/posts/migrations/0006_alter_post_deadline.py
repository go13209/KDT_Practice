# Generated by Django 3.2.18 on 2023-04-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateField(default='2023-04-07'),
        ),
    ]
