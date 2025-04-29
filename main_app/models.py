from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Plant(models.Model):
    LIGHT_CHOICES = [
        ('LOW', 'Low Light - Indirect light, no direct sun'),
        ('MEDIUM', 'Medium Light - Bright indirect light'),
        ('HIGH', 'Bright Light - Direct sunlight needed')
    ]

    name = models.CharField(
        max_length=100,
        help_text="Give your plant a unique name"
    )
    species = models.CharField(
        max_length=100,
        help_text="The botanical or common name of your plant"
    )
    description = models.TextField(
        max_length=250,
        help_text="Share some details about your plant's appearance, history, or care requirements"
    )
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Approximate age in years (0 for new plants)"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    light_requirements = models.CharField(
        max_length=50,
        choices=LIGHT_CHOICES,
        default='MEDIUM',
        help_text="Select the amount of light your plant needs"
    )
    
    water_frequency = models.IntegerField(
        help_text='Number of days between watering',
        validators=[MinValueValidator(1), MaxValueValidator(60)],
        verbose_name="Watering Frequency",
        null=True,  # Temporarily allow null
        blank=True,  # Temporarily allow blank
        default=7  # Set a default value
    )
    
    last_watered = models.DateField(
        null=True,
        blank=True,
        help_text="The last date this plant was watered"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plant-detail', kwargs={'plant_id': self.id})

    class Meta:
        ordering = ['name']

# Define choices for fertilizer types
FERTILIZER_TYPES = (
    ('O', 'Organic'),
    ('S', 'Synthetic'),
    ('N', 'Natural')
)

class Watering(models.Model):
    date = models.DateField('Watering date')
    amount = models.CharField(
        max_length=1,
        choices=[
            ('L', 'Light'),
            ('M', 'Moderate'),
            ('H', 'Heavy')
        ],
        default='M'
    )
    notes = models.TextField(max_length=250, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_amount_display()} watering on {self.date}"

    class Meta:
        ordering = ['-date']

class Fertilizer(models.Model):
    date = models.DateField('Fertilization date')
    type = models.CharField(
        max_length=1,
        choices=FERTILIZER_TYPES,
        default=FERTILIZER_TYPES[0][0]
    )
    amount = models.CharField(
        max_length=1,
        choices=[
            ('L', 'Light'),
            ('M', 'Moderate'),
            ('H', 'Heavy')
        ],
        default='M'
    )
    notes = models.TextField(max_length=250, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} fertilizer on {self.date}"

    class Meta:
        ordering = ['-date']

 
