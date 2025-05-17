from django.contrib import admin
from storage.models import Storage, Size, Color

@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')

@admin.register(Size)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
