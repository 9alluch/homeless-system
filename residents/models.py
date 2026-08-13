from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Resident(models.Model):
     GENDER_CHOICES = [
        ("M", "Homme"),
        ("F", "Femme"),
     ]
     STATUS_CHOICES = [
        ("active", "Présent"),
        ("left", "Parti"),
        ("hospital", "Hospitalisé"),
     ]
     first_name = models.CharField(
        max_length=100,
        verbose_name="Prénom"
     )
     last_name = models.CharField(
        max_length=100,
        verbose_name="Nom"
     )
     birth_date = models.DateField(
        verbose_name="Date de naissance",
        null=True,
        blank=True
     )
     gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name="Sexe"
     )
     nationality = models.CharField(
        max_length=100,
        verbose_name="Nationalité",
        blank=True
     )
     phone = models.CharField(
        max_length=20,
        verbose_name="Téléphone",
        blank=True
     )
     emergency_contact = models.CharField(
        max_length=150,
        verbose_name="Personne à contacter",
        blank=True
     )
     emergency_phone = models.CharField(
        max_length=20,
        verbose_name="Téléphone d'urgence",
        blank=True
     )
     admission_date = models.DateField(
        verbose_name="Date d'admission"
     )
     allergies = models.TextField(
        verbose_name="Allergies",
        blank=True
     )
     diseases = models.TextField(
        verbose_name="Maladies",
        blank=True
     )
     treatments = models.TextField(
        verbose_name="Traitements",
        blank=True
     )
     medical_notes = models.TextField(
        verbose_name="Notes médicales",
        blank=True
     )
     observations = models.TextField(
        verbose_name="Observations",
        blank=True
     )
     status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
        verbose_name="Statut",
     )
     photo = models.ImageField(
        upload_to="residents/",
        blank=True,
        null=True,
        verbose_name="Photo"
     )
     room = models.ForeignKey(
      "Room",
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name="residents",
      verbose_name="Chambre"
     )

     def __str__(self):
        return f"{self.first_name} {self.last_name}"

     class Meta:
        verbose_name = "Résident"
        verbose_name_plural = "Résidents" 

class Room(models.Model):
    number = models.PositiveIntegerField(
        unique=True,
        verbose_name="Numéro de chambre"
    )

    capacity = models.PositiveIntegerField(
        verbose_name="Capacité",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(20),
        ],
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )

    def __str__(self):
        return f"Chambre {self.number}"

    @property
    def occupancy(self):
        return self.residents.count()

    @property
    def is_full(self):
        return self.occupancy >= self.capacity

    class Meta:
        verbose_name = "Chambre"
        verbose_name_plural = "Chambres"
        ordering = ["number"]