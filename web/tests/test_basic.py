import pytest
from web.tests.factories import (
    HomeBannerFactory,
    ServiceCategoryFactory,
    ServiceFactory,
    ServicePlaningStepFactory,
    ServiceProcessStepFactory,
    ServicePageImageFactory,
    ServiceFAQFactory,
    WorksFactory,
    WorksRelatedImagesFactory,
    TestimonialFactory,
    BlogFactory,
    JourneyFactory,
    ContactFactory,
    ClientFactory,
)






@pytest.mark.django_db
def test_homebanner_factory():
    banner = HomeBannerFactory()
    assert banner.title
    assert banner.description

@pytest.mark.django_db
def test_servicecategory_factory():
    category = ServiceCategoryFactory()
    assert category.category

@pytest.mark.django_db
def test_service_factory():
    service = ServiceFactory()
    assert service.title
    assert service.category
    assert service.icon
    assert service.main_image_first
    assert service.main_image_second

@pytest.mark.django_db
def test_service_planing_step_factory():
    step = ServicePlaningStepFactory()
    assert step.planing_title
    assert step.planing_description
    assert step.service

@pytest.mark.django_db
def test_service_process_step_factory():
    step = ServiceProcessStepFactory()
    assert step.process_list
    assert step.service

@pytest.mark.django_db
def test_service_page_image_factory():
    img = ServicePageImageFactory()
    assert img.image
    assert img.service

@pytest.mark.django_db
def test_service_faq_factory():
    faq = ServiceFAQFactory()
    assert faq.question
    assert faq.answer
    assert faq.service

@pytest.mark.django_db
def test_works_factory():
    work = WorksFactory()
    assert work.category
    assert work.service
    assert work.icon
    assert work.inner_page_main_image
    assert work.title
    assert work.client
    assert work.date
    assert work.description

@pytest.mark.django_db
def test_works_related_images_factory():
    related = WorksRelatedImagesFactory()
    assert related.service
    assert related.work_related_images

@pytest.mark.django_db
def test_testimonial_factory():
    t = TestimonialFactory()
    assert t.name
    assert t.designation
    assert t.image
    assert t.description

@pytest.mark.django_db
def test_blog_factory():
    blog = BlogFactory()
    assert blog.title
    assert blog.description
    assert blog.image

@pytest.mark.django_db
def test_journey_factory():
    journey = JourneyFactory()
    assert journey.title
    assert journey.description
    assert journey.image

@pytest.mark.django_db
def test_contact_factory():
    c = ContactFactory()
    assert c.name
    assert c.email
    assert c.subject
    assert c.message

@pytest.mark.django_db
def test_client_factory():
    client = ClientFactory()
    assert client.title
    assert client.image