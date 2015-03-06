from django.contrib import admin

# Register your models here.

from p.models import Store, AccessPoint

#class AccessPointInline(admin.StackedInline):
class AccessPointInline(admin.TabularInline):
    model = AccessPoint
    extra = 0

class StoreAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['address', 'phone'], 'classes': ['collapse']}),
    ]
    inlines = [AccessPointInline]

admin.site.register(Store, StoreAdmin)

#admin.site.register(AccessPoint)
