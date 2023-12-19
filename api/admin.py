from django.contrib import admin
from api.models import Company, Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
  list_display = ('company_id', 'name', 'domain', 'location', 'about', 'type', 'added_date', 'active')
  
class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('employee_id', 'name', 'email', 'address', 'phone', 'about', 'role', 'company', 'added_date', 'active')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)