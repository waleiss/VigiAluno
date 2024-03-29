# Generated by Django 5.0.1 on 2024-03-23 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncia', '0007_denuncia_praticantes_denuncia_titulo_and_more'),
        ('medida_tomada', '0001_initial'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='denuncia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='denuncia.denuncia'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='medida_tomada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='medida_tomada.medidatomada'),
        ),
    ]
