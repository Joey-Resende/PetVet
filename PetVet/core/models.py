from django.db import models
from django.urls import reverse
from datetime import date


castrated_status = (('Não', 'Não'), ('Sim', 'Sim'))

sex_status = (('Macho', 'Macho'), ('Fêmea', 'Fêmea'))

procedures = (('Consulta', 'Consulta'), ('Retorno', 'Retorno'),
              ('Exame', 'Exame'), ('Cirurgia', 'Cirurgia'))

type_sedative = (('Não', 'Não'), ('Simples', 'Simples'),
                 ('Complexo', 'Complexo'))

type_anamnese = (('Aula', 'Aula'), ('Rotina', 'Rotina'))

vaccination = (('Não Vacinado', 'Não Vacinado'), ('Não sabe', 'Não Sabe'), ('Vacinado, Desatualizada',
               'Vacinado, Desatualizada'), ('Vacinado, Atualizada', 'Vacinado, Atualizada'))

type_v = (('Nenhuma', 'Nenhuma'), ('V8', 'V8'), ('V10', 'V10'), ('V12', 'V12'))

type_felina = (('Nenhuma', 'Nenhuma'), ('Tríplice', 'Tríplice'),
               ('Quadrúpla', 'Quadrúpla'))

vermi_ecto = (('Não', 'Não'), ('Não sabe Informar', 'Não Sabe Informar'),
              ('Desatualizada', 'Desatualizada'), ('Atualizada', 'Atualizada'))

leish = (('Não', 'Não'), ('Vacinado', 'Vacinado'),
         ('Usa Coleira', 'Usa    Coleira'), ('Atualizada', 'Atualizada'), ('Desatualizada', 'Desatualizada'))

conduct = (('Dócil', 'Dócil'), ('Inquieto', 'Inquieto'), ('Medroso', 'Medroso'),
           ('Agressivo', 'Agressivo'))

consciousness = (('Coma', 'Coma'), ('Estupor', 'Estupor'), ('Confusão', 'Confusão'), ('Normal/Alerta',
                 'Normal/Alerta'), ('Sonolência/Apático', 'Sonolência/Apático'), ('Excitado', 'Excitado'))

nutricional_status = (('Caquético', 'Caquético'), ('Magro', 'Magro'),
                      ('Normal', 'Normal'), ('Gordo', 'Gordo'), ('Obeso', 'Obeso'))

dental_calculus = (('Não', 'Não'), ('Leve', 'Leve'),
                   ('Moderado', 'Moderado'), ('Intenso', 'Intenso'), ('Não Permitiu', 'Não Permitiu'))

dental_loss = (('Não', 'Não'), ('Sim', 'Sim'),
               ('Persistência de dente decíduo', 'Persistência de dente decíduo'), ('Não Permitiu', 'Não Permitiu'))

ulcera = (('Não', 'Não'), ('Sim', 'Sim'), ('Não Permitiu', 'Não Permitiu'))

auscu_cardio = (('Não Permitiu/Não Realizado', 'Não Permitiu/Não Realizado'), ('Bulhas Normofonéticas',
                'Bulhas Normofonéticas'), ('Bulhas Hipofonéticas', 'Bulhas Hipofonéticas'), ('Sopro em Valva', 'Sopro em Valva'))

auscu_pulmonar = (('Ruído Normal', 'Ruído Normal'), ('Alterado', 'Alterado'),
                  ('Não Permitiu', 'Não Permitiu'), ('Não Realizado ACP', 'Não Realizado ACP'))

percu_pulmonar = (('Normal', 'Normal'),
                  ('Submaciço', 'Submaciço'), ('Maciço', 'Maciço'), ('Não Realizado', 'Não Realizado'))

mamas = (('Normal', 'Normal'), ('Secreção', 'Secreção'),
         ('Hiperplasia', 'Hiperplasia'))

nodulo = (('Não', 'Não'), ('Firmes', 'Firmes'), ('Flutuante', 'Flutuante'),
          ('Aderido', 'Aderido'), ('Não Aderido', 'Não Aderido'))

local_pain = (('Não', 'Não'), ('Lado Esquerdo', 'Lado Esquerdo'),
              ('Lado Direito', 'Lado Direito'))

pain_m = (('Não', 'Não'), ('M1', 'M1'), ('M2', 'M2'),
          ('M3', 'M3'), ('M4', 'M4'), ('M5', 'M5'))

parasitas = (('Não', 'Não'), ('Carrapato', 'Carrapato'),
             ('Pulga', 'Pulga'), ('Miíase', 'Miíase'))

classifier = (('Caso Simples', 'Caso Simples'),
              ('Caso Complexo', 'Caso Complexo'))

evolucion_status = (('Piorou', 'Piorou'), ('Melhorou', 'Melhorou'),
                    ('Não evoluiu', 'Não evoluiu'), ('Não sabe', 'Não sabe'))

score = (('-', '-'), ('0', '0'), ('1', '1'), ('2', '2'),
         ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
         ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'))

choice_prurido = (('-', '-'), ('Esporádico', 'Esporádico'),
                  ('Frequente', 'Frequente'), ('Sazonal', 'Sazonal'),
                  ('Não sazonal', 'Não sazonal'), ('Diurno', 'Diurno'),
                  ('Noturno', 'Noturno'), ('Nos dois períodos', 'Nos dois períodos'))

contacts_sint = (('Sim', 'Sim'), ('Não', 'Não'),
                 ('Não sei', 'Não sei'), ('do paciente em atendimento foi antes', 'do paciente em atendimento foi antes'), ('do contactante foi antes', 'do contactante foi antes'))

contacts_access = (('Sim', 'Sim'), ('Não', 'Não'),
                   ('Esporadicamente', 'Esporadicamente'), ('Frequentemente', 'Frequentemente'), ('Diariamente', 'Diariamente'))

contacts_sleep = (('Fora de casa', 'Fora de casa'),
                  ('Dentro de casa', 'Dentro de casa'), ('Os dois', 'Os dois'))

pulgas_carrapatos = (('Não', 'Não'), ('Não sei', 'Não sei'), ('Sim', 'Sim'),
                     ('Leve', 'Leve'), ('Moderado', 'Moderado'), ('Intenso', 'Intenso'))


class Tutor(models.Model):
    """Model representing a classe Tutor."""
    tutor_name = models.CharField(
        max_length=50, verbose_name='Nome do Tutor')
    cpf = models.CharField(max_length=14, null=True,
                           verbose_name='CPF')
    phone = models.CharField(max_length=15, null=True,
                             verbose_name='Telefone')
    email = models.EmailField(max_length=254, verbose_name='Email')
    cep = models.CharField(max_length=9, verbose_name='Cep')
    street = models.CharField(max_length=40, verbose_name='Rua')
    number = models.IntegerField(verbose_name='Numero')
    district = models.CharField(max_length=40, verbose_name='Bairro')
    city = models.CharField(
        max_length=40, default='Petrolina', verbose_name='Cidade')
    state = models.CharField(
        max_length=40, default='Pernambuco', verbose_name='Estado')

    class Meta:
        ordering = ['tutor_name']

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('tutor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.tutor_name


class Pets(models.Model):
    """Model representing a classe pet."""
    id = models.AutoField(primary_key=True)
    pet_name = models.CharField(
        max_length=30, verbose_name='Nome do Pet')
    species = models.CharField(
        max_length=20, verbose_name='Espécie')
    breed = models.CharField(
        max_length=30, verbose_name='Raça')
    gender = models.CharField(
        max_length=5, choices=sex_status, verbose_name='Genêro')
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name='Data de Nascimento')
    castrated = models.CharField(
        max_length=3, choices=castrated_status, default='N', verbose_name='Castrado?')
    weight = models.DecimalField(
        max_digits=6, decimal_places=3, verbose_name='Peso', default=0)
    tutor_name = models.ForeignKey(
        'Tutor', on_delete=models.PROTECT, null=True, verbose_name='Nome do Tutor')

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('pet-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.pet_name


class Vet(models.Model):
    """Model representing a classe Vet."""
    vet_name = models.CharField(
        max_length=30, verbose_name='Nome')

    class Meta:
        ordering = ['vet_name']

    def __str__(self):
        """String for representing the Model object."""
        return self.vet_name


class MedicalCare(models.Model):
    """Model representing a classe Medical care."""
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today, verbose_name='Data')
    time = models.TimeField(verbose_name='Hora')
    pet_name = models.ForeignKey(
        'Pets', on_delete=models.PROTECT, null=True, verbose_name='Nome do Pet')
    procedure = models.CharField(
        max_length=8, choices=procedures, verbose_name='Tipo de atendimento')
    vet_name = models.ForeignKey(
        'Vet', on_delete=models.PROTECT, null=True, verbose_name='Veterinario')
    sedative = models.CharField(
        max_length=8, choices=type_sedative, default='Não', verbose_name='Tipo de sedativo')
    report = models.TextField(
        max_length=1000, verbose_name='Relato do problema')

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        """Returns the url to access a particular medical care instance."""
        return reverse('medical_care_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.procedure} - {self.pet_name} - {self.date}'


class GeneralClinic(models.Model):
    medical_care = models.ForeignKey(
        'MedicalCare', on_delete=models.PROTECT, null=True, verbose_name='Atendimento')
    choice_anamnese = models.CharField(
        max_length=6, choices=type_anamnese, verbose_name='Tipo atendimento')
    anamnese = models.TextField(max_length=2000, verbose_name='Anamnese')
    choice_anti_rabica = models.CharField(
        max_length=23, choices=vaccination, verbose_name='Anti-Rábica')
    choice_type_v = models.CharField(
        max_length=7, choices=type_v, verbose_name='V8/V10/V12')
    choice_v = models.CharField(
        max_length=23, choices=vaccination, verbose_name='')
    choice_type_felina = models.CharField(
        max_length=23, choices=type_felina, verbose_name='Tríplice/Quádrupla Felina')
    choice_felina = models.CharField(
        max_length=23, choices=vaccination, verbose_name='')
    others_felina = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='Outras Vacinas')
    choice_verminose = models.CharField(
        max_length=17, choices=vermi_ecto, verbose_name='Controle Verminose')
    others_verminose = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='Verminose - Fármaco/Dose/Frequência')
    choice_ectopas = models.CharField(
        max_length=17, choices=vermi_ecto, verbose_name='Prevenção Ectoparasitas')
    others_ectopas = models.CharField(
        max_length=30, null=True, blank=True, verbose_name='Ectoparasitas - Fármaco/Dose/Frequência')
    choice_leish = models.CharField(
        max_length=17, choices=leish, verbose_name='Prevenção Leishmaniose')

    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        """Returns the url to access a particular medical care instance."""
        return reverse('general_clinic_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.medical_care} - {self.anamnese}'


class PhysicalExam(models.Model):
    medical_care = models.ForeignKey(
        'MedicalCare', on_delete=models.PROTECT, null=True, verbose_name='Atendimento')
    choice_conduct = models.CharField(
        max_length=9, choices=conduct, verbose_name='Conduta')
    weight = models.DecimalField(
        max_digits=6, decimal_places=3, verbose_name='Peso', default=0)
    choice_consciousness = models.CharField(
        max_length=18, choices=consciousness, verbose_name='Nivel de Consciência')
    stance = models.CharField(max_length=30, verbose_name='Postura')
    hydration = models.CharField(max_length=30, verbose_name='Hidratação')
    choice_nutricional_status = models.CharField(
        max_length=18, choices=nutricional_status, verbose_name='Estado Nutricional')
    oculopalpebral = models.CharField(
        max_length=30, default='Não Permitiu', verbose_name='Mucosa Oculopalpebral')
    bucal = models.CharField(
        max_length=30, default='Não Permitiu', verbose_name='Mucosa Bucal')
    genital = models.CharField(
        max_length=30, default='Não Permitiu', verbose_name='Mucosa Genital')
    choice_dental_calculus = models.CharField(
        max_length=18, choices=dental_calculus, verbose_name='Cálculo Dentário')
    choice_dental_loss = models.CharField(
        max_length=29, choices=dental_loss, verbose_name='Perda Dentário')
    gengivite = models.CharField(
        max_length=18, choices=dental_calculus, verbose_name='Gengivite')
    choice_ulcera = models.CharField(
        max_length=12, choices=ulcera, verbose_name='Úlcera')
    choice_halitose = models.CharField(
        max_length=18, choices=dental_calculus, verbose_name='Halitose')
    linfonodos = models.CharField(max_length=60, verbose_name='Linfonodos')
    fc = models.CharField(max_length=30, default=0, verbose_name='FC')
    fr = models.CharField(max_length=30, default=0, verbose_name='FR')
    tpc = models.CharField(max_length=30, default=0, verbose_name='TPC')
    tr = models.CharField(max_length=30, default=0, verbose_name='TR')
    pulse = models.CharField(max_length=30, default=0, verbose_name='Pulso')
    choice_auscu_cardio = models.CharField(
        max_length=26, choices=auscu_cardio, verbose_name='Ausculta Cardíaca')
    heart_rate = models.CharField(
        max_length=30, default=0, verbose_name='Ritmo Cardíaco')
    choice_auscu_pulmonar = models.CharField(
        max_length=17, choices=auscu_pulmonar, verbose_name='Ausculta Pulmonar')
    choice_percu_pulmonar = models.CharField(
        max_length=17, choices=percu_pulmonar, verbose_name='Percussão Pulmonar')
    palpa_abdominal = models.CharField(
        max_length=60, verbose_name='Palpação Abdominal')
    choice_mamas = models.CharField(
        max_length=17, choices=mamas, verbose_name='Mamas/Tetos')
    choice_nodulo = models.CharField(
        max_length=17, choices=nodulo, verbose_name='Nódulos')
    choice_nodulo_pain = models.CharField(
        max_length=30, choices=castrated_status, verbose_name='Dor Nódulo')
    choice_local_pain = models.CharField(
        max_length=30, choices=local_pain, verbose_name='Localização da Dor')
    choice_pain_m = models.CharField(
        max_length=3, choices=pain_m, verbose_name='')
    genital_region = models.CharField(
        max_length=30, default='Normal', verbose_name='Região Genital')
    choice_ectoparasitas = models.CharField(
        max_length=30, choices=parasitas, verbose_name='Ectoparasitas')
    ectoparasitas_intensity = models.CharField(
        max_length=30,  null=True, blank=True, verbose_name='Intensidade dos Parasitas')
    pelage = models.CharField(
        max_length=60, default='Normal', verbose_name='Pelagem')
    ears = models.CharField(
        max_length=60, default='Normal', verbose_name='Orelhas')
    diag_differ = models.TextField(
        max_length=1000, verbose_name='Suspeitas')
    diag_final = models.TextField(
        max_length=1000, verbose_name='Diagnósticos Definitivos')
    case_classification = models.CharField(
        max_length=13, choices=classifier, verbose_name='Classificação de caso')

    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        """Returns the url to access a particular medical care instance."""
        return reverse('physical_exam_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.medical_care} - {self.diag_final} - {self.case_classification}'


class GeneralDhermExam(models.Model):
    medical_care = models.ForeignKey(
        'MedicalCare', on_delete=models.PROTECT, null=True, verbose_name='Atendimento')
    report = models.TextField(max_length=500, verbose_name='Queixa principal')
    choice_anamnese = models.CharField(
        max_length=6, choices=type_anamnese, verbose_name='Tipo atendimento')
    evolution_time = models.CharField(
        max_length=30, verbose_name='Tempo de evolução')
    choice_evolution_status = models.CharField(
        max_length=30, choices=evolucion_status, verbose_name='Status da evolução')
    evolution_score = models.CharField(
        max_length=2, default='-', choices=score, verbose_name='Nota de evolução')
    quest_01_where_begin = models.CharField(
        max_length=60, verbose_name='Onde as lesões iniciaram?')
    quest_02_how_are_lesions = models.CharField(
        max_length=60, verbose_name='Como eram as primeiras lesões?')
    prurido = models.CharField(
        max_length=3, default='Não', choices=castrated_status, verbose_name='Prurido')
    prurido_intensity = models.CharField(
        max_length=2, default='-', choices=score, verbose_name='Intensidade do prurido')
    choice_prurido = models.CharField(
        max_length=17, default='-', choices=choice_prurido, verbose_name='')
    quest_03_prurido_history = models.CharField(
        max_length=3, default='Não', choices=castrated_status, verbose_name='O prurido antecede as lesões?')
    quest_04_recent_medical_care = models.TextField(
        max_length=200, default='Não', verbose_name='Recentemente foi atendido por veterinário? - Quais exames realizados?')
    quest_05_aplication_prescrition_topic = models.TextField(
        max_length=200, default='Não', verbose_name='Foi aplicado ou prescrito algum produto tópico? (nome, dose, tempo de uso)')
    quest_06_feels_better_topic = models.CharField(
        max_length=3, default='Não', choices=castrated_status, verbose_name='Melhorou?')
    feels_intensity_topic = models.CharField(
        max_length=2, default='-', choices=score, verbose_name='Nota')
    quest_07_feels_intensity_topic = models.CharField(
        max_length=2, default='-', choices=score, verbose_name='Foi usando antes ou depois do surgimento das lesões?')
    quest_08_aplication_prescrition_oral = models.TextField(
        max_length=200, default='Não', verbose_name='Foi aplicado ou prescrito algum produto via oral?')
    quest_09_feels_better_oral = models.CharField(
        max_length=3, default='Não', choices=castrated_status, verbose_name='Melhorou?')
    quest_10_feels_intensity_oral = models.CharField(
        max_length=2, default='-', choices=score, verbose_name='Foi usando antes ou depois do surgimento das lesões?')
    quest_11_aplication_prescrition_oral = models.TextField(
        max_length=200, default='Não', verbose_name='É alérgico a algum fármaco/Produto? Quais?')
    quest_12_aplication_prescrition_oral = models.TextField(
        max_length=200, default='Não', verbose_name='Há histórico anterior de dermatopias? Exames realizados/Tratamento prescrito')
    quest_13_color_skin = models.TextField(
        max_length=200, default='Não', verbose_name='Pele mudou de cor? / Quais áreas?')
    quest_14_color_fur = models.TextField(
        max_length=200, default='Não', verbose_name='Pelagem mudou de cor? / Quais áreas?')
    quest_15_dermatopias = models.TextField(
        max_length=200, default='Não', verbose_name='Há histórico de dermatopias familiar? / Quais áreas?')
    quest_16_persons_dermatopias = models.CharField(
        max_length=3, default='Não', choices=castrated_status, verbose_name='Há lesões nas pessoas que convivem com o animal?')
    quest_17_contacts = models.CharField(
        max_length=3, default='Não', choices=castrated_status, verbose_name='Contactantes?')
    quest_18_contacts_quant = models.CharField(
        max_length=60, default='Não', verbose_name='Espécie / Quantidade')
    quest_19_contacts_assint = models.CharField(
        max_length=60, default='Assintomáticos', verbose_name='Assintomáticos / Sintomáticos')
    quest_20_contacts_sint_quant = models.CharField(
        max_length=30, default='Não', verbose_name='Se sintomáticos, quantos? semelhante ao observado neste animal?')
    quest_21_contacts_sint_period = models.CharField(
        max_length=36, default='Não', choices=contacts_sint, verbose_name='As lesões apareceram no mesmo período?')
    quest_22_contacts_access_street = models.CharField(
        max_length=15, default='Não', choices=contacts_access, verbose_name='Tem acesso à rua?')
    quest_23_contacts_sleep_local = models.CharField(
        max_length=14, default='Não', choices=contacts_sleep, verbose_name='Local onde dorme / passa o dia?')
    quest_24_contacts_petbed = models.CharField(
        max_length=30, default='-', verbose_name='Onde o animal dorme? Sobre o que o animal se deita?')
    quest_25_contacts_wash_petbed = models.CharField(
        max_length=30, default='-', verbose_name='Como é feita a limpeza do local onde o animal dorme? Qual o produto?')
    quest_26_contacts_grass_earth = models.CharField(
        max_length=15, default='Não', choices=contacts_access, verbose_name='Tem contato com terra e grama?')
    quest_27_contacts_plants = models.CharField(
        max_length=30, default='Não', verbose_name='Há plantas em casa ou que ele tenha contato?')
    quest_28_special_place = models.CharField(
        max_length=30, default='Não', verbose_name='Foi levado em algum em especial nos últimos meses?')
    quest_29_travel_cities = models.CharField(
        max_length=30, default='Não', verbose_name='Viaje para outras cidades?')
    quest_30_pulgas_carrapatos = models.CharField(
        max_length=15, default='Não', choices=pulgas_carrapatos, verbose_name='Tem pulgas/carrapatos?')
