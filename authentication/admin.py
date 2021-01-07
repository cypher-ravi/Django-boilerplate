from django.contrib import admin
from .models import User
# from core_api.models import Cart
# Register your models here.


# class UserCartAdmin(admin.StackedInline):
#     model = Cart

# class UserAdmin(admin.ModelAdmin):
#     inlines = [UserCartAdmin]


admin.site.register(User)
# ,UserAdmin)