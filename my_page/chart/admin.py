from django.contrib import admin
from .models import Offers, Skills, Brands, BrandsOffice, EmploymentTypes, Page
# Register your models here.

admin.site.register(Offers)
admin.site.register(Skills)
admin.site.register(Brands)
admin.site.register(BrandsOffice)
admin.site.register(EmploymentTypes)
admin.site.register(Page)
