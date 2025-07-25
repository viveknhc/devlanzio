from django.shortcuts import render
from .models import HomeBanner, Service, Works, Testimonial, Blog, Journey,Contact
from django.shortcuts import render,get_object_or_404

def index(request):
    text= HomeBanner.objects.last()

    print(text)
    services = Service.objects.all()

    last_4_work = list(Works.objects.order_by('-id')[:4])

    last_1_work = last_4_work[-1]       
    last_2_work = last_4_work[-2:]     
    last_3_work = last_4_work[-3:] 
    last_4_work = last_4_work[-4:] 

    testimonials = Testimonial.objects.all()

    blogs = Blog.objects.all()
    journeys = Journey.objects.all()    
    context = {"is_index": True,
               "text": text,
               "services": services,
               "last_1_work": last_1_work,
               "last_2_work": last_2_work,
               "last_3_work": last_3_work,
               "last_4_work": last_4_work,
               "testimonials": testimonials,
               "blogs": blogs,
               "journeys": journeys}
    return render(request, "web/index.html", context)

def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_save = Contact(name = name,email = email,subject = subject,message = message)
        contact_save.save()
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)

def works(request):
    works = Works.objects.all()
    context = {"is_works": True,
               "works":works}
    return render(request, "web/works.html", context)

def workSingle(request,id):
    work= get_object_or_404(Works,id=id)
    context = {"is_works": True,
               "work":work
              }
    return render(request, "web/work-inner.html", context)

def services(request):
    services = Service.objects.all()
    context = {"is_works": True,
               "services":services}
    return render(request, "web/services.html", context)

def serviceSingle(request,id):
    service = get_object_or_404(Service,id=id)
    context = {"is_works": True,
               "service":service
               }
    return render(request, "web/service-inner.html", context)


