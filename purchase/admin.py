from django.contrib import admin

from purchase.models import Purchase, ItensPurchase


class ItensPurchaseInline(admin.TabularInline):
    model = ItensPurchase


class PurchaseAdmin(admin.ModelAdmin):
    inlines = [ItensPurchaseInline]


admin.site.register(Purchase, PurchaseAdmin)
