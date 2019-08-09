from django.shortcuts import render, redirect
from django.http import *
from django.template import loader
from .models import district, assemblies, public_complaints
from .forms import *
# Create your views here.
#login and signin module
from django.contrib.auth import authenticate, get_user_model, login, logout

###############################################

from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    all_dist = district.objects.all()
    context = {
        'all_dist': all_dist
    }
    return render(request, 'home.html', context)


def index(request):
    all_dist = district.objects.all()
    context = {
        'all_dist': all_dist
    }
    return render(request, 'index.html', context)


def details(request, districts_id):
    detail = district.objects.get(pk = districts_id)
    return render(request, 'details.html', {'detail': detail})

def complaint(request, complaint_id):
    detail_comp = assemblies.objects.get(pk = complaint_id)
    template = loader.get_template('complaint.html')
    context = {
        "detail_comp": detail_comp
    }
    return HttpResponse(template.render(context, request))


def post_complaint_view(request):
    if request.method == "POST":
        form = public_complaints_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/andhrapradesh/post_complaint/')
    else:
        form = public_complaints_form()
    return render(request, 'post_complaint.html', {'form': form})
