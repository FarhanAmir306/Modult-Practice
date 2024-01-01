from django.contrib import admin
from .models import CatagoryModel,Post

# Register your models here.


class category_admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']

admin.site.register(CatagoryModel,category_admin)
admin.site.register(Post)