# Generated by Django 3.2 on 2021-05-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_alter_item_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.IntegerField(default=''),
        ),
    ]
