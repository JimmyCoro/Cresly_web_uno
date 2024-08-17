# Generated by Django 5.0.7 on 2024-08-11 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_rename_sabor_pizza_sabor_1_pizza_sabor_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sabor_1', models.CharField(choices=[('BBQ', 'BBQ'), ('MYM', 'Miel y Mostaza'), ('MAR', 'Macaruyá'), ('BRS', 'Broster'), ('PIN', 'Piña')], max_length=3)),
                ('sabor_2', models.CharField(choices=[('BBQ', 'BBQ'), ('MYM', 'Miel y Mostaza'), ('MAR', 'Macaruyá'), ('BRS', 'Broster'), ('PIN', 'Piña')], max_length=3)),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.producto')),
            ],
        ),
    ]
