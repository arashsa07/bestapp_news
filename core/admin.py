from django.contrib import admin
from models import News, Category, Person, Agency
from mce_filebrowser.admin import MCEFilebrowserAdmin


class NewsAdmin(MCEFilebrowserAdmin):
    list_display = ('id', 'title', 'category', 'sub_title', 'source', 'date_modify', 'url')
    date_hierarchy = 'date_modify'
    search_fields = ('category', 'title')


class CategeoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'agency', 'title')
    search_fields = ('parent', )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_name')


class AgencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategeoryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Agency, AgencyAdmin)
