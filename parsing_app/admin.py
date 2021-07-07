from django.contrib import admin

from parsing_app.models import Author, Quote


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'birth_date', 'birth_place', 'description']}),
    ]
    list_display = ['name', 'birth_date', 'birth_place', 'description', ]
    search_fields = ['name']


class QuoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text', 'author']}),
    ]
    list_display = ['text', 'author', ]
    list_filter = ['author']
    search_fields = ['text']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Quote, QuoteAdmin)
