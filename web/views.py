from django.shortcuts import render


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)

def base(request):
    context = {"is_index": True}
    return render(request, "web/partials/base.html", context)

