from django.contrib import admin

# Register your models here.

from .models import *

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, SlugAdmin)
admin.site.register(Category)
admin.site.register(Brand)
