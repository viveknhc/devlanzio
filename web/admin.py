from django.contrib import admin
from .models import HomeBanner, Service,ServiceCategory, Works, Testimonial, Blog, Journey,Contact,Client

admin.site.register(HomeBanner)
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")
    search_fields = ("category",)
    ordering = ("category",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "icon_preview")
    list_filter = ("category",)
    search_fields = ("title", "category__category")
    ordering = ("title",)

    readonly_fields = ("icon_preview",)

    def icon_preview(self, obj):
        if obj.icon:
            return f'<img src="{obj.icon.url}" width="40" height="40" />'
        return "—"

    icon_preview.allow_tags = True
    icon_preview.short_description = "Icon"
admin.site.register(Works)
admin.site.register(Testimonial)

admin.site.register(Blog)
admin.site.register(Journey)
admin.site.register(Contact)
admin.site.register(Client)