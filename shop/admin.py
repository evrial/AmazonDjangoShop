from django.contrib import admin

from models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('active', 'title', 'amazon_id')
    list_display_links = ('title',)
    list_editable = ('active',)
    list_filter = ('title', 'created', 'active')
    search_fields = ['title', 'description', 'amazon_id']


admin.site.register(Category, CategoryAdmin)