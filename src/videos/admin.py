from django.contrib import admin

# Register your models here.
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_filter = ['title', 'timestamp', 'updated'] # right sidebar
    list_display = ['title', 'timestamp', 'updated'] # tabs on list
    readonly_fields = ['updated', 'timestamp', 'short_title'] # inside object like a label
    search_fields = ['title', ] # search field
    class Meta:
        model = Video

    def short_title(self, obj):
        return obj.title[:3]

admin.site.register(Video, VideoAdmin)
