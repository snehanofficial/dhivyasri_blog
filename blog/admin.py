from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','published_date','theme','audio_file','images','video_file')
admin.site.register(Post)
