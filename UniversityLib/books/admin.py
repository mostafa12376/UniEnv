from django.contrib import admin
from pages.models import Book

# Register your models here.

class bookAdmin(admin.ModelAdmin):
    search_fields=('title','ISBN','author','pubYear','category')
    list_display=('title','author','ISBN','category')
    filter_horizontal=()
    list_filter=('author','category')
    fieldsets=()




admin.site.register(Book,bookAdmin)
admin.site.title="Uni Lib"
admin.site.site_header="FCAI-CU University Library"
