from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'publication_date',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('author', 'title', 'content', 'excerpt', 'published',
                       'publication_date')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('protect_html', 'content_html', 'excerpt_html', 'slug',
                       'meta_description')
        }),
    )


admin.site.register(Article, ArticleAdmin)
