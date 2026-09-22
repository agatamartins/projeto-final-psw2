from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'opiniao', 'data_criacao')
    search_fields = ('usuario__username', 'opiniao')
    list_filter = ('data_criacao',)
