from django.contrib import admin

# Register your models here.
from .models import Post, Tag ,Comment



class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug":("title",)}

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)