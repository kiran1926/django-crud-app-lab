from django.db import models

# Create your models here.
class Plant(models.Model):
    name =  models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

     # Additional plant-specific fields
    light_requirements = models.CharField(
        max_length=50,
        choices=[
            ('LOW', 'Low Light'),
            ('MEDIUM', 'Medium Light'),
            ('HIGH', 'Bright Light')
        ],
        default='MEDIUM',
        null=True,  # Allow null temporarily for migration
        blank=True
    )
    water_frequency = models.IntegerField(
        help_text='Number of days between watering',
        null=True,  # Allow null temporarily for migration
        blank=True
    )
    last_watered = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

 
