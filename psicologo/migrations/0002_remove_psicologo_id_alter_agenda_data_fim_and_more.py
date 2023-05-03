# Generated by Django 4.0.2 on 2023-04-19 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psicologo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psicologo',
            name='id',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='data_fim',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='data_inicio',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='psicologo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psicologo.psicologo'),
        ),
        migrations.AlterField(
            model_name='psicologo',
            name='crp',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]