# Generated by Django 3.1.7 on 2021-06-11 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information_management', '0001_initial'),
        ('man_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servinglist',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man_management.customer'),
        ),
        migrations.AddField(
            model_name='servinglist',
            name='servicer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man_management.servicer'),
        ),
        migrations.AddField(
            model_name='notification',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man_management.dispatcher'),
        ),
        migrations.AddField(
            model_name='chat',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man_management.customer'),
        ),
        migrations.AddField(
            model_name='chat',
            name='servicer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man_management.servicer'),
        ),
    ]
