# Generated by Django 3.1.4 on 2021-01-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201215_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
