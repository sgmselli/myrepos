from django.contrib import admin
from .models import Ingredient, MenuItem

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)