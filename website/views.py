from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def home(request):
    all_courses = Course.objects.all
    return render(request, 'home.html', {'all': all_courses})

def search(request):
    if request.method=='POST':
        srch = request.POST['srh'].strip().replace(" ", "").upper()
        

        if srch:
            match = Course.objects.filter(Q(course__iexact=srch))
            info = Course.objects.filter(Q(course__iexact=srch)).first()
            cal_code = None
            
            try:
                cal_code = info.course[:4] + '-' + info.course[4:]
            except:
                print('')

            if match:
                return render(request, 'search.html', {'sr': match, 'course': srch, 'credits': info.num_credit, 'name': info.course, 'cal_code': cal_code})
            else:
                messages.error(request, 'No results found, please enter a valid course code (e.g COMP302)')
        else:
            #all_courses = Course.objects.all
            #return render(request, 'search.html', {'sr': all_courses, 'course': 'All Courses'})
            return HttpResponseRedirect('/search/')
    return render(request, 'search.html')
