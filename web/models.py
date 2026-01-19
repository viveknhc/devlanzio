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
    sub_title = models.CharField(max_length=100, blank=True, null=True, help_text="Sub title for the service Inner page")
    sub_description = HTMLField(blank=True, null=True, help_text="Sub description for the service Inner page")

    description1 = HTMLField(blank=True, null=True, help_text="Description 1 for the service Inner page")
    description2 = HTMLField(blank=True, null=True, help_text="Description 2 for the service Inner page")
    icon = VersatileImageField(upload_to="service/icons", blank=True, null=True, help_text="gif image for listing page).")
    main_image_first = VersatileImageField(
        upload_to="service/images",
        blank=True,
        null=True,
        help_text="Main image used on the service inner page (circle and gallery).",
    )
    main_image_second = VersatileImageField(
        upload_to="service/images",
        blank=True,
        null=True,
        help_text="Main image used on the service inner page (circle and gallery).",
    )
    def __str__(self):
        return self.title

class ServicePlaningStep(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="planning_steps",
    )
    planing_title = models.CharField(max_length=100)
    planing_description = HTMLField()

    def __str__(self):
        return self.service.title


class ServiceProcessStep(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="process_steps",
    )
    process_list = HTMLField()

    def __str__(self):
        return self.service.title

class ServicePageImage(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="page_images",
    )
    image = VersatileImageField(upload_to="service/images")
    def __str__(self):
        return self.service.title



class ServiceFAQ(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="faqs",
    )
    question = models.CharField(max_length=255)
    answer = HTMLField()

    def __str__(self):
        return f"{self.service.title} - {self.question}"


class Works(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="works"   # 👈 important
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="works"   # 👈 important
    )
    icon = VersatileImageField(upload_to = "works",help_text="image for listing card")

    inner_page_main_image = VersatileImageField(upload_to = "works",help_text="image for Inner page Main Image")
    title = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    date = models.DateField()
    # link = models.URLField(blank=True, null=True)
    description = HTMLField()

    def __str__(self):
        return self.title

class WorksRelatedImages(models.Model):
    service = models.ForeignKey(
        Works,
        on_delete=models.CASCADE,
        related_name="workImage",
    )
    work_related_images = VersatileImageField(upload_to = "works",help_text="Add on images for work")


    
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
    