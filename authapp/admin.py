from django.contrib import admin
from authapp.models import User
from baskets.admin import BasketAdmin
from baskets.models import Basket


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketAdmin,)

