# Generated by Django 3.2.5 on 2021-07-10 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeudaSbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_deuda', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('E', 'En Proceso'), ('A', 'Aprovado'), ('N', 'No Aprovado')], max_length=1)),
                ('monto', models.IntegerField(default=0)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('ia_algoritm', models.IntegerField(default=0)),
                ('sentinel_status', models.CharField(choices=[('B', 'Bueno'), ('R', 'Regular'), ('M', 'Malo')], max_length=1)),
                ('sbs_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.deudasbs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
