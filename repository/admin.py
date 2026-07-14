from django.contrib import admin
from .models import Material


class MaterialAdmin(admin.ModelAdmin):

    list_display = (
        
    )


admin.site.register(Material, MaterialAdmin)