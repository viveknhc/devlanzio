from django.contrib import admin
from .models import HomeBanner, Service,ServiceCategory, Works, Testimonial, Blog, Journey,Contact,Client,ServicePlaningStep,ServiceProcessStep,ServicePageImage,ServiceFAQ,WorksRelatedImages

admin.site.register(HomeBanner)
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category")
    search_fields = ("category",)
    ordering = ("category",)


class ServicePlaningInline(admin.TabularInline):
    """Inline to add/edit product variants directly inside Product"""
    model = ServicePlaningStep
    extra = 1
    fields = ("planing_title", "planing_description",)
    show_change_link = True

class ServiceProcessStepInline(admin.TabularInline):
    model = ServiceProcessStep
    extra = 1
    fields = ("process_list",)
    show_change_link = True

class ServicePageImageInline(admin.TabularInline):
    model = ServicePageImage
    extra = 1
    fields = ("image",)
    show_change_link = True

class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1
    fields = ("question", "answer",)
    show_change_link = True

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

    inlines = [ServicePlaningInline,ServiceProcessStepInline,ServicePageImageInline,ServiceFAQInline]


from django.utils.html import format_html

class WorksRelatedImagesInline(admin.TabularInline):
    model = WorksRelatedImages
    extra = 1
    fields = ("work_related_images",)
    show_change_link = True

@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ("id","icon_preview", "title","category", "service", "client",  "date", "inner_page_main_image_preview")
    list_filter = ("category", "service", "date")
    search_fields = ("title", "client", "category__category", "service__title")
    ordering = ("-date", "title")
    readonly_fields = ("icon_preview", "inner_page_main_image_preview")

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="40" height="40" />', obj.icon.url)
        return "—"
    icon_preview.allow_tags = True
    icon_preview.short_description = "Icon"

    def inner_page_main_image_preview(self, obj):
        if obj.inner_page_main_image:
            return format_html('<img src="{}" width="80" height="40" />', obj.inner_page_main_image.url)
        return "—"
    inner_page_main_image_preview.allow_tags = True
    inner_page_main_image_preview.short_description = "Main Image"

    inlines = [WorksRelatedImagesInline]

    

admin.site.register(Testimonial)

admin.site.register(Blog)
admin.site.register(Journey)
admin.site.register(Contact)
admin.site.register(Client)