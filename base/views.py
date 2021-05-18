from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Achievement


def index(request):

    achievement_list = Achievement.objects.all()
    student_list = Student.objects.all()
    
    content = {
        "achievement":achievement_list
    }
    return render(request, "base/index.html", content)

def detail(request, id):
    pass