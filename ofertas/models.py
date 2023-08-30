from django.db import models


class Oferta(models.Model):

    PERFIL_CHOICES = (
        ('FrontEnd', 'FrontEnd'),
        ('BackEnd', 'BackEnd')
    )

    NIVEL_CHOICES = (
        ('junior', 'Junior'),
        ('semisenior', 'Semisenior'),
        ('senior', 'Senior')
    )

    titulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    pub_date = models.DateField()
