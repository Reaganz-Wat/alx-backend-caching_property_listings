from django.db import models

# Create your models here.
class Properties(models.Model):
    """
    title (CharField, max_length=200)
    description (TextField)
    price (DecimalField, maxdigits=10, decimalplaces=2)
    location (CharField, max_length=100)
    created_at (DateTimeField, autonowadd=True)
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} -> {self.price}"