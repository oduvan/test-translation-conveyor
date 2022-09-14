from django.contrib import admin

from .models import Translation

class TranslationAdmin(admin.ModelAdmin):
    list_display = ['txt_original', 'txt_translation', 'status', 'user_translator', 'user_qa', 'qa_comment']
    list_filter = ['status']

admin.site.register(Translation, TranslationAdmin)