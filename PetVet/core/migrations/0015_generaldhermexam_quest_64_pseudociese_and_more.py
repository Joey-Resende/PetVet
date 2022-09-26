# Generated by Django 4.0.4 on 2022-09-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_generaldhermexam_quest_61_castrated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_64_pseudociese',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Pseudociese?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_65_gave_birth',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Já pariu?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_66_gave_birth_quant',
            field=models.CharField(default='-, vivos(-), mortos(-)', max_length=30, verbose_name='Quantas vezes(vivos(), mortos()):'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_67_mamas_add',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Mamas aumentadas?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_68_mamas_nodulo',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Nódulos mamários?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_69_libido',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Animal tem libido?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_70_libido_sex',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='É por animais do mesmo sexo?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_71_otites',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=25, verbose_name='Otites? - (Sazonal ou não):'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_72_polifagia',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Tem Polifagia?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_73_polifagia',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Tem Polidipsia?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_74_poliuria',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Tem Poliúria?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_75_tumor_nodulo',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='Não', max_length=3, verbose_name='Tem tumor/nódulo?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_76_tumor_grow_speed',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='-', max_length=25, verbose_name='Qual a velocidade do crescimento do tumor?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_77_tumor_where_begin',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='-', max_length=30, verbose_name='Onde começou?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_78_tumor_pruriginoso',
            field=models.CharField(default='Não', max_length=30, verbose_name='Pruriginoso? (nota - 0 a 10):'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_79_tumor_operado',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='-', max_length=3, verbose_name='Já foi operado anteriormente?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_79_tumor_operado_renew',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='-', max_length=3, verbose_name='Houve recidiva?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_80_pet_bath',
            field=models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='-', max_length=3, verbose_name='Banha o animal?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_81_pet_bath_local',
            field=models.CharField(default='Casa', max_length=10, verbose_name='Banha o animal em casa ou Pet Shop?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_82_pet_bath_freq',
            field=models.CharField(default='-', max_length=25, verbose_name='Frequência?:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_83_pet_bath_prod',
            field=models.CharField(default='-', max_length=150, verbose_name='Produtos usados no banho:'),
        ),
        migrations.AddField(
            model_name='generaldhermexam',
            name='quest_84_other_system',
            field=models.CharField(default='-', max_length=150, verbose_name='Outros sistemas:'),
        ),
    ]
