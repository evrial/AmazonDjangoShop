from django.contrib import admin

from models import Category, Product, AdditionalPage

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('active', 'title', 'amazon_node_id', 'created', 'modified')
    list_display_links = ('title',)
    list_editable = ('active',)
    list_filter = ('title', 'created', 'modified')
    search_fields = ['title', 'description', 'amazon_node_id']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(AdditionalPage)