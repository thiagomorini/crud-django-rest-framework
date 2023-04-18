from django.db import models

class Module(models.Model):
    serial_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"Serial Number: {self.serial_number} Name: {self.name}"
