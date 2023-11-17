from django.contrib import admin
from .models import Product
# from .models import YourModel

# Register your models here.

admin.site.register(Product)

# @admin.register(YourModel)
# class YourModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'photo',)
#     list_display_links = ('id', 'photo',)