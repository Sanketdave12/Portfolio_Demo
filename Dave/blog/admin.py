from django.contrib import admin
from .models import Blog, Comment, Contact, SubscribeNewsletter, LetsConnect
from django.contrib.admin.options import ModelAdmin


class BlogAdmin(ModelAdmin):
    list_display = ["Title", "Tag", "Date"]
    search_fields = ["Title", "Tag", "Date"]
    list_filter = ["Tag", "Date"]


admin.site.register(Blog, BlogAdmin)


admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(SubscribeNewsletter)
admin.site.register(LetsConnect)
