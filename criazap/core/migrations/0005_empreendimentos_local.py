# Generated by Django 4.1.5 on 2023-01-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_empreendimentos_autor_empreendimentos_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='empreendimentos',
            name='local',
            field=models.CharField(default='', max_length=100),
        ),
    ]
