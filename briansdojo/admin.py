from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project

    def clean_image(self)

admin.site.register(Project, ProjectAdmin)
