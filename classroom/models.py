from django.db import models


# Create your models here.
#Model Form
class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100, help_text="Enter your first name", verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=100, help_text="Enter your last name", verbose_name="Last Name"
    )
    subject = models.CharField(max_length=100, help_text="Enter your subject")

    def __str__(self):
        return f"{self.first_name} {self.last_name} teaches {self.subject}"
    
    
#Non model Form

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
