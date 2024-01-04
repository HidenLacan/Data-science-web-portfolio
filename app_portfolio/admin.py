from django.contrib import admin
from .models import Project,Contact

class Project_Admin(admin.ModelAdmin):
    list_display = ('image_url','subtitle','title','description','url_project')
    list_editable = ('subtitle','title','description','url_project')

admin.site.register(Contact)
admin.site.register(Project,Project_Admin)

