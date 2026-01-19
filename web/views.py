from django.shortcuts import render
from .models import HomeBanner, Service, ServiceCategory, Works, Testimonial, Blog, Journey,Contact,Client
from django.shortcuts import render,get_object_or_404

def index(request):
    text= HomeBanner.objects.last()
    services = Service.objects.all()
    works_list = list(Works.objects.order_by('-id')[:4])
    last_1_work = works_list[-1] if len(works_list) >= 1 else None      
    last_2_work = works_list[-2] if len(works_list) >= 2 else None    
    last_3_work = works_list[-3] if len(works_list) >= 3 else None
    last_4_work = works_list[0] if len(works_list) >= 1 else None
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.order_by('-id')[:3]
   
    journeys = Journey.objects.all()    

    clients = Client.objects.all().order_by('-id')
    context = {"is_index": True,
               "text": text,
               "services": services,
               "last_1_work": last_1_work,
               "last_2_work": last_2_work,
               "last_3_work": last_3_work,
               "last_4_work": last_4_work,
               "testimonials": testimonials,
               "blogs": blogs,
               "journeys": journeys,
                "clients": clients,
            }
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
    categories = ServiceCategory.objects.prefetch_related('services').all()
    selected_category = request.GET.get("category")
    selected_service = request.GET.get("service")

    # Base queryset
    works_qs = Works.objects.all()

    # Dropdown 1: Filter by category, updates category dropdown and populates services dropdown
    # Dropdown 2: Filter by service under selected category (takes precedence)
    if selected_service:
        # If service is selected, filter works by that service
        works = works_qs.filter(service_id=selected_service)
    elif selected_category:
        # If only category is selected, filter works by that category
        works = works_qs.filter(category_id=selected_category)
    else:
        works = works_qs

    # For dependent service dropdown: If a category is selected, show its related services
    related_services = None
    if selected_category:
        try:
            category_obj = ServiceCategory.objects.prefetch_related('services').get(id=selected_category)
            related_services = category_obj.services.all()
        except ServiceCategory.DoesNotExist:
            related_services = None

    context = {
        "is_works": True,
        "categories": categories,
        "works": works,
        "selected_category": selected_category,
        "selected_service": selected_service,
        "related_services": related_services,
    }
    return render(request, "web/works.html", context)

def workSingle(request,id):
    work= get_object_or_404(Works,id=id)
    context = {"is_works": True,
               "work":work
              }
    return render(request, "web/work-inner.html", context)

def services(request):
    categories = ServiceCategory.objects.all()
    selected_category = request.GET.get("category")

    services = Service.objects.all()

    if selected_category:
        services = services.filter(category_id=selected_category)

    context = {
        "is_works": True,
        "categories": categories,
        "services": services,
        "selected_category": selected_category,
    }
    return render(request, "web/services.html", context)


def serviceSingle(request,id):
    service = get_object_or_404(Service,id=id)
    works = Works.objects.filter(category_id=service.category_id).order_by('-id')[:3]
    context = {"is_works": True,
               "service":service,
               "works":works
               }
    return render(request, "web/service-inner.html", context)


def careers(request):

    context = {"is_works": True}
          
    return render(request, "web/careers.html", context)


def blogSingle(request,id):

    blog = get_object_or_404(Blog,id=id)    
    context = {"is_blog": True,
               "blog":blog}
          
    return render(request, "web/blog-single.html", context)


