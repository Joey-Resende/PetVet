# Generated by Django 4.0.4 on 2022-05-07 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='weight',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6, verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='tutor_name',
            field=models.CharField(max_length=50, verbose_name='Nome do Tutor'),
        ),
        migrations.CreateModel(
            name='GeneralClinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_anamnese', models.CharField(choices=[('Aula', 'Aula'), ('Rotina', 'Rotina')], max_length=6, verbose_name='Tipo anamnese')),
                ('anamnese', models.TextField(max_length=1000, verbose_name='Anamnese')),
                ('medical_care', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.medicalcare', verbose_name='Atendimento')),
            ],
        ),
    ]
