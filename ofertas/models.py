from django.db import models


class Oferta(models.Model):
    JUNIOR = 'junior'
    SEMISENIOR = 'semisenior'
    SENIOR = 'senior'

    PERFIL_CHOICES = (
        ('FrontEnd', 'FrontEnd'),
        ('BackEnd', 'BackEnd')
    )

    NIVEL_CHOICES = (
        (JUNIOR, 'Junior'),
        (SEMISENIOR, 'Semisenior'),
        (SENIOR, 'Senior')
    )

    titulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    pub_date = models.DateField()
