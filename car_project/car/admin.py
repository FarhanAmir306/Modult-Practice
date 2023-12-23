from django.contrib import admin
from .models import Car,Comment
# Register your models here.
admin.site.register(Car)
admin.site.register(Comment)


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug' : ('name',)}
#     list_display = ['name', 'slug']
    
# admin.site.register( CategoryAdmin)