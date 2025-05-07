from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=50)
    salary = models.IntegerField()

    class Meta:
        db_table = 'employee_table'

    def __str__(self):
        return self.name
    
    