# Generated by Django 2.2.5 on 2019-10-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skladnik',
            old_name='pizza',
            new_name='pizze',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='cena',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='opis',
            field=models.TextField(blank=True, default='', help_text='Opis pizzy'),
        ),
        migrations.AlterField(
            model_name='skladnik',
            name='cena',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
