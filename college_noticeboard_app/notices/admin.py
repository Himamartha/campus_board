from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'created_by', 'created_at', 'is_important')
    list_filter = ('department', 'created_at', 'is_important')
    search_fields = ('title', 'content', 'department')
    date_hierarchy = 'created_at'
