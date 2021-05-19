from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Achievement

def index(request):
    achievement_list = Achievement.objects.all()
    if request.method == "GET":

        content = {
            "achievement":achievement_list
        }
        return render(request, "base/index.html", content)

    elif request.method == "POST":
        searched_obj_id = []
        for i in achievement_list:
            if request.POST["title"]  in i.title and request.POST["first_name"]  in i.owner.first_name \
                and request.POST["last_name"]  in i.owner.last_name and request.POST["level"]  in i.level\
                    and int(request.POST["year"]) == i.year:

                searched_obj_id.append(i)
        content = {
            "achievement":searched_obj_id
        }
        return render(request, "base/index.html", content)

    else:
        return Http404


def detail(request, id):
    content = {
        "achievement":get_object_or_404(Achievement, id=id)
    }
    return render(request, "base/detail.html", content)