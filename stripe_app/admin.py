from django.contrib import admin
from stripe_app.models import Item


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
