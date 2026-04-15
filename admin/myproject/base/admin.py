from django.contrib import admin
from .models import FruitModel

# Register your models here.
class FruitAdmin(admin.ModelAdmin):
    model = FruitModel
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)


admin.site.register(FruitModel, FruitAdmin)
