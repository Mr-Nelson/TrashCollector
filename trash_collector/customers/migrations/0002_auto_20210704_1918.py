# Generated by Django 3.1.8 on 2021-07-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=101, null=True),
        ),
    ]