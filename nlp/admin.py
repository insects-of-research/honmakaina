from django.contrib import admin

# Register your models here.

from .models import Word2Vec

@admin.register(Word2Vec)
class Word2VecAdmin(admin.ModelAdmin):
    pass