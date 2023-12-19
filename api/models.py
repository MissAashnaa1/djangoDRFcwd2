from django.db import models

# Create your models here.
class Company(models.Model):
  company_id = models.AutoField(primary_key= True)
  name = models.CharField(max_length = 70)
  domain = models.CharField(max_length = 50)
  location = models.CharField(max_length = 100)
  about = models.TextField()
  type = models.CharField(max_length = 50)
  added_date = models.DateTimeField(auto_now = True)
  active = models.BooleanField(default = True)
  
  def __str__(self):
    return self.name
  
  
class Employee(models.Model):
  employee_id = models.AutoField(primary_key = True)
  name = models.CharField(max_length = 70)
  email = models.EmailField(max_length = 254)
  address = models.CharField(max_length = 100)
  phone = models.CharField(max_length = 15)
  about = models.TextField()
  role = models.CharField(max_length = 50, choices=(
    ('CEO', 'CEO'),
    ('VP', 'VP'),
    ('MANAGER', 'MANAGER'),
    ('STAFF', 'STAFF'),
    ('Project Lead','Project Lead'),
    ))
  company = models.ForeignKey(Company, on_delete = models.CASCADE)
  added_date = models.DateTimeField(auto_now = True)
  active = models.BooleanField(default = True)