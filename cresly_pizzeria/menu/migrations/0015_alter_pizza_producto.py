# Generated by Django 5.0.7 on 2024-08-19 21:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_bebida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.producto'),
        ),
    ]
