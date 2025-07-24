from django.shortcuts import render
from .models import HomeBanner, Service, Works, Testimonial, Faqs, Blog, Journey


def index(request):
    text= HomeBanner.objects.last()

    print(text)
    services = Service.objects.all()
    works = Works.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faqs.objects.all()
    blogs = Blog.objects.all()
    journeys = Journey.objects.all()    
    context = {"is_index": True,
               "text": text,
               "services": services,
               "works": works,
               "testimonials": testimonials,
               "faqs": faqs,
               "blogs": blogs,
               "journeys": journeys}
    return render(request, "web/index.html", context)

def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)

def contact(request):
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)

def works(request):
    context = {"is_works": True}
    return render(request, "web/works.html", context)

def services(request):
    context = {"is_works": True}
    return render(request, "web/services.html", context)
