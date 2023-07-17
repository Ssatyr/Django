from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') # wyświetla kolumny w panelu admina
    list_filter = ('status', 'created', 'publish', 'author') # dodaje pasek filtrowania po prawej stronie
    search_fields = ('title', 'body') # dodaje pole wyszukiwania
    prepopulated_fields = {'slug': ('title',)} # automatycznie wypełnia pole slug na podstawie pola title
    raw_id_fields = ('author',) # dodaje pole wyszukiwania po autorze
    date_hierarchy = 'publish' # dodaje pasek nawigacji po dacie publikacji
    ordering = ('status', 'publish') # sortuje wyniki po statusie i dacie publikacji

admin.site.register(Post, PostAdmin) # rejestruje model Post w panelu admina
