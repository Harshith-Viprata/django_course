# Generated by Django 5.1.4 on 2024-12-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(max_length=200),
        ),
    ]