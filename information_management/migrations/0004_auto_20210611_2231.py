# Generated by Django 3.1.7 on 2021-06-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information_management', '0003_chat_isending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='isEnding',
            field=models.BooleanField(default=False),
        ),
    ]