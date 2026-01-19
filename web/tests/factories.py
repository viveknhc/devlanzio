# python manage.py generate_demo_data

import factory
from factory.django import DjangoModelFactory
from faker import Faker
from django.core.files.base import ContentFile
from PIL import Image
import io

from web.models import (
    HomeBanner,
    ServiceCategory,
    Service,
    ServicePlaningStep,
    ServiceProcessStep,
    ServicePageImage,
    ServiceFAQ,
    Works,
    WorksRelatedImages,
    Testimonial,
    Blog,
    Journey,
    Contact,
    Client,
)

fake = Faker()

def fake_image(name="test.jpg"):
    file = io.BytesIO()
    image = Image.new("RGB", (600, 400), color="blue")
    image.save(file, "JPEG")
    file.seek(0)
    return ContentFile(file.read(), name)

class HomeBannerFactory(DjangoModelFactory):
    class Meta:
        model = HomeBanner

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")

class ServiceCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ServiceCategory

    category = factory.Faker("word")

class ServiceFactory(DjangoModelFactory):
    class Meta:
        model = Service

    category = factory.SubFactory(ServiceCategoryFactory)
    title = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    sub_description = factory.Faker("paragraph")
    description1 = factory.Faker("paragraph")
    description2 = factory.Faker("paragraph")
    icon = factory.LazyFunction(lambda: fake_image("icon.jpg"))
    main_image_first = factory.LazyFunction(lambda: fake_image("main1.jpg"))
    main_image_second = factory.LazyFunction(lambda: fake_image("main2.jpg"))

class ServicePlaningStepFactory(DjangoModelFactory):
    class Meta:
        model = ServicePlaningStep

    service = factory.SubFactory(ServiceFactory)
    planing_title = factory.Faker("sentence")
    planing_description = factory.Faker("paragraph")

class ServiceProcessStepFactory(DjangoModelFactory):
    class Meta:
        model = ServiceProcessStep

    service = factory.SubFactory(ServiceFactory)
    process_list = factory.Faker("paragraph")

class ServicePageImageFactory(DjangoModelFactory):
    class Meta:
        model = ServicePageImage

    service = factory.SubFactory(ServiceFactory)
    image = factory.LazyFunction(lambda: fake_image("page.jpg"))

class ServiceFAQFactory(DjangoModelFactory):
    class Meta:
        model = ServiceFAQ

    service = factory.SubFactory(ServiceFactory)
    question = factory.Faker("sentence")
    answer = factory.Faker("paragraph")

class WorksFactory(DjangoModelFactory):
    class Meta:
        model = Works

    category = factory.SubFactory(ServiceCategoryFactory)
    service = factory.SubFactory(ServiceFactory)
    icon = factory.LazyFunction(lambda: fake_image("work_icon.jpg"))
    inner_page_main_image = factory.LazyFunction(lambda: fake_image("work_main.jpg"))
    title = factory.Faker("sentence")
    client = factory.Faker("company")
    date = factory.Faker("date_this_decade")
    description = factory.Faker("paragraph")

class WorksRelatedImagesFactory(DjangoModelFactory):
    class Meta:
        model = WorksRelatedImages

    service = factory.SubFactory(WorksFactory)
    work_related_images = factory.LazyFunction(lambda: fake_image("related.jpg"))

class TestimonialFactory(DjangoModelFactory):
    class Meta:
        model = Testimonial

    name = factory.Faker("name")
    designation = factory.Faker("job")
    image = factory.LazyFunction(lambda: fake_image("testimonial.jpg"))
    description = factory.Faker("paragraph")

class BlogFactory(DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    image = factory.LazyFunction(lambda: fake_image("blog.jpg"))

class JourneyFactory(DjangoModelFactory):
    class Meta:
        model = Journey

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    image = factory.LazyFunction(lambda: fake_image("journey.jpg"))

class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    name = factory.Faker("name")
    email = factory.Faker("email")
    subject = factory.Faker("sentence")
    message = factory.Faker("paragraph")

class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client

    title = factory.Faker("company")
    image = factory.LazyFunction(lambda: fake_image("client.jpg"))
