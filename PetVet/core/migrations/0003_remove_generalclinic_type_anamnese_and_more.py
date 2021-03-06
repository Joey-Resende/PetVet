# Generated by Django 4.0.4 on 2022-05-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pets_weight_alter_tutor_tutor_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalclinic',
            name='type_anamnese',
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_anamnese',
            field=models.CharField(choices=[('Aula', 'Aula'), ('Rotina', 'Rotina')], default='', max_length=6, verbose_name='Tipo anamnese'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_anti_rabica',
            field=models.CharField(choices=[('Não Vacinado', 'Não Vacinado'), ('Vacinado', 'Vacinado'), ('Não sabe', 'Não Sabe'), ('Desatualizada', 'Desatualizada'), ('Atualizada', 'Atualizada'), ('Não Ética', 'Não Ética'), ('Ética', 'Ética')], default='', max_length=13, verbose_name='Anti-Rábica'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_ectopas',
            field=models.CharField(choices=[('Não', 'Não'), ('Não sabe Informar', 'Não Sabe Informar'), ('Desatualizada', 'Desatualizada'), ('Atualizada', 'Atualizada')], default='', max_length=17, verbose_name='Prevenção Ectoparasitas'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_felina',
            field=models.CharField(choices=[('Não Vacinado', 'Não Vacinado'), ('Vacinado', 'Vacinado'), ('Não sabe', 'Não Sabe'), ('Desatualizada', 'Desatualizada'), ('Atualizada', 'Atualizada'), ('Não Ética', 'Não Ética'), ('Ética', 'Ética')], default='', max_length=13, verbose_name=''),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_leish',
            field=models.CharField(choices=[('Não', 'Não'), ('Vacinado', 'Vacinado'), ('Usa Coleira', 'Usa Coleira'), ('Atualizada', 'Atualizada'), ('Desatualizada', 'Desatualizada')], default='', max_length=17, verbose_name='Prevenção Leishmaniose'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_type_felina',
            field=models.CharField(choices=[('Tréplice', 'Tríplice'), ('Quadrúpla', 'Quadrúpla')], default='', max_length=9, verbose_name='Tríplice/Quádrupla Felina'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_type_v',
            field=models.CharField(choices=[('V8', 'V8'), ('V10', 'V10'), ('V12', 'V12')], default='', max_length=3, verbose_name='V8/V10/V12'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_v',
            field=models.CharField(choices=[('Não Vacinado', 'Não Vacinado'), ('Vacinado', 'Vacinado'), ('Não sabe', 'Não Sabe'), ('Desatualizada', 'Desatualizada'), ('Atualizada', 'Atualizada'), ('Não Ética', 'Não Ética'), ('Ética', 'Ética')], default='', max_length=13, verbose_name=''),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='choice_verminose',
            field=models.CharField(choices=[('Não', 'Não'), ('Não sabe Informar', 'Não Sabe Informar'), ('Desatualizada', 'Desatualizada'), ('Atualizada', 'Atualizada')], default='', max_length=17, verbose_name='Controle Verminose'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='others_ectopas',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ectoparasitas - Fármaco/Dose/Frequência'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='others_felina',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Outras Vacinas'),
        ),
        migrations.AddField(
            model_name='generalclinic',
            name='others_verminose',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Verminose - Fármaco/Dose/Frequência'),
        ),
    ]
