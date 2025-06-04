from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('title', 'company')
    actions = ['approve_jobs']

    def approve_jobs(self, request, queryset):
        queryset.update(is_approved=True)
    approve_jobs.short_description = "Approve selected jobs"