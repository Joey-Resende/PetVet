# Generated by Django 4.0.4 on 2022-05-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_generalclinic_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='physicalexam',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='generalclinic',
            name='anamnese',
            field=models.TextField(max_length=2000, verbose_name='Anamnese'),
        ),
        migrations.AlterField(
            model_name='generalclinic',
            name='choice_anti_rabica',
            field=models.CharField(choices=[('Não Vacinado', 'Não Vacinado'), ('Não sabe', 'Não Sabe'), ('Vacinado, Desatualizada', 'Vacinado, Desatualizada'), ('Vacinado, Atualizada', 'Vacinado, Atualizada')], max_length=23, verbose_name='Anti-Rábica'),
        ),
        migrations.AlterField(
            model_name='generalclinic',
            name='choice_felina',
            field=models.CharField(choices=[('Não Vacinado', 'Não Vacinado'), ('Não sabe', 'Não Sabe'), ('Vacinado, Desatualizada', 'Vacinado, Desatualizada'), ('Vacinado, Atualizada', 'Vacinado, Atualizada')], max_length=23, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='generalclinic',
            name='choice_type_felina',
            field=models.CharField(choices=[('Nenhuma', 'Nenhuma'), ('Tríplice', 'Tríplice'), ('Quadrúpla', 'Quadrúpla')], max_length=23, verbose_name='Tríplice/Quádrupla Felina'),
        ),
        migrations.AlterField(
            model_name='generalclinic',
            name='choice_type_v',
            field=models.CharField(choices=[('Nenhuma', 'Nenhuma'), ('V8', 'V8'), ('V10', 'V10'), ('V12', 'V12')], max_length=7, verbose_name='V8/V10/V12'),
        ),
        migrations.AlterField(
            model_name='generalclinic',
            name='choice_v',
            field=models.CharField(choices=[('Não Vacinado', 'Não Vacinado'), ('Não sabe', 'Não Sabe'), ('Vacinado, Desatualizada', 'Vacinado, Desatualizada'), ('Vacinado, Atualizada', 'Vacinado, Atualizada')], max_length=23, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='choice_local_pain',
            field=models.CharField(choices=[('Não', 'Não'), ('Lado Esquerdo', 'Lado Esquerdo'), ('Lado Direito', 'Lado Direito')], max_length=30, verbose_name='Localização da Dor'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='choice_mamas',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Secreção', 'Secreção'), ('Hiperplasia', 'Hiperplasia')], max_length=17, verbose_name='Mamas/Tetos'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='choice_percu_pulmonar',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Submaciço', 'Submaciço'), ('Maciço', 'Maciço'), ('Não Realizado', 'Não Realizado')], max_length=17, verbose_name='Percussão Pulmonar'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='diag_differ',
            field=models.TextField(max_length=1000, verbose_name='Suspeitas'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='ears',
            field=models.CharField(default='Normal', max_length=60, verbose_name='Orelhas'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='ectoparasitas_intensity',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Intensidade dos Parasitas'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='palpa_abdominal',
            field=models.CharField(max_length=60, verbose_name='Palpação Abdominal'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='pelage',
            field=models.CharField(default='Normal', max_length=60, verbose_name='Pelagem'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='tpc',
            field=models.CharField(default=0, max_length=30, verbose_name='TPC'),
        ),
    ]
