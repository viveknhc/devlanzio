from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

# Create your models here.
class HomeBanner(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    def __str__(self):
        return self.title


class ServiceCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services"   # 👈 important
    )
    title = models.CharField(max_length=100)
    description = HTMLField()
    icon = VersatileImageField(upload_to="service/icons", blank=True, null=True)
    image = VersatileImageField(
        upload_to="service/images",
        blank=True,
        null=True,
        help_text="Main image used on the service inner page (circle and gallery).",
    )

    # Optional content fields for service detail page (inner page)
    sub_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Subtitle shown near the top of the service inner page.",
    )
    short_description = HTMLField(
        blank=True,
        null=True,
        help_text="Short rich-text description shown under the subtitle.",
    )
    detail_description = HTMLField(
        blank=True,
        null=True,
        help_text="Main detailed description text of the service.",
    )
    included_items = HTMLField(
        blank=True,
        null=True,
        help_text="HTML list or content for the 'Includes this service' section.",
    )
    planning_list = HTMLField(
        blank=True,
        null=True,
        help_text="Optional <li> elements for the planning bullet list.",
    )
    process_steps = HTMLField(
        blank=True,
        null=True,
        help_text="Optional HTML to replace the 4-step 'Our process' cards.",
    )
    process_description = HTMLField(
        blank=True,
        null=True,
        help_text="Optional paragraph shown below the process images.",
    )
    counter_steps = HTMLField(
        blank=True,
        null=True,
        help_text="Optional HTML to replace the 3 bottom counter-step cards.",
    )

    def __str__(self):
        return self.title


class ServiceFAQ(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="faqs",
    )
    question = models.CharField(max_length=255)
    answer = HTMLField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.service.title} - {self.question}"


class Works(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="works"   # 👈 important
    )
    image = VersatileImageField(upload_to = "works")
    title = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)
    description = HTMLField()
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = VersatileImageField(upload_to = "testimonial")
    description = HTMLField()
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = VersatileImageField(upload_to = "blog")
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Journey(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    image = VersatileImageField(upload_to = "journey")
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = HTMLField()

    def __str__(self):
        return self.name
    

class Client(models.Model):
    title = models.CharField(max_length=100)
    image = VersatileImageField(upload_to = "journey")

    def __str__(self):
        return self.title
    