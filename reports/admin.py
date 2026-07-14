from django.contrib import admin
from .models import Issue, Department, Reply

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 1

class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'submitted_by', 'created_at')
    inlines = [ReplyInline]

admin.site.register(Issue, IssueAdmin)
admin.site.register(Department)
admin.site.register(Reply)
