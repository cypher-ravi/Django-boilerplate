from django.contrib import admin
from .models import Item,Dish,Breakfast,Weekly,Lunch,Dinner
from django import forms

from django.forms.utils import ErrorList

# Register your models here.

class ItemInline(admin.StackedInline):
    model = Item
    

class DishAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

# admin.site.register(Item)
admin.site.register(Dish,DishAdmin)
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)

class WeekModelForm(forms.ModelForm):
    def clean(self):
        if Weekly.objects.count() > 6:
            self._errors.setdefault('__all__', ErrorList()).append("You can add only  7 weekly diets.")
        return self.cleaned_data


class WeeklyAdmin(admin.ModelAdmin):
    form = WeekModelForm


admin.site.register(Weekly,WeeklyAdmin)
