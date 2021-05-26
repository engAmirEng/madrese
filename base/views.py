from .forms import StudentForm, AchievementForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from .models import Achievement, Student
from . import extentions
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.http import require_GET

def error_400(request, exception):
        data = {}
        return render(request,'errors/error400.html', data)
def error_403(request, exception):
        data = {}
        return render(request,'errors/error403.html', data)
def error_404(request, exception):
        data = {}
        return render(request,'errors/error404.html', data)
def error_503(request, exception):
        data = {}
        return render(request,'errors/error503  .html', data)

def index(request):
    achievement_list = Achievement.objects.all()
    if request.method == "GET":
        content = {
            "achievement":achievement_list
        }
        # return render(request, "base/index.html", content)
        return render(request, "base/modiran_frame/index_detail.html", content)
        # return render(request, "base/modiran_frame/update_form.html", content)
        # return render(request,'errors/error503.html')
    elif request.method == "POST":
        searched_obj = []
        for i in achievement_list:
            if request.POST["title"]  in i.title and request.POST["first_name"]  in i.owner.first_name \
                and request.POST["last_name"]  in i.owner.last_name and request.POST["level"]  in i.level\
                    and request.POST["year"] in str(i.year):

                searched_obj.append(i)
        content = {
            "achievement":searched_obj
        }
        return render(request, "base/modiran_frame/index_detail.html", content)
    else:
        return Http404


def detail(request, id):
    content = {
        "achievement":get_object_or_404(Achievement, id=id),
    }
    return render(request, "base/modiran_frame/index_detail.html", content)

# @login_required
def manage(request, model_name=""):
    achievement_list = Achievement.objects.all()
    student_list = Student.objects.all()
    content = {
        "achievement":achievement_list, "student":student_list
        }
    content.update({"date":timezone.now()})
    if request.method == "GET":
        if model_name != "achievement" and model_name != "student" and model_name != "index":
            return Http404
        else:
            return render(request, "base/modiran_frame/managing.html", content)
    elif request.method == "POST":
        searched_obj = []
        if model_name == "achievement":
            for i in achievement_list:
                if request.POST["owner"]  in f"{i.owner.first_name} + {i.owner.last_name}" and \
                    request.POST["title"] in i.title and request.POST["year"] in str(i.year) and \
                        request.POST["level"] in i.level and request.POST["field"] in i.field and \
                            request.POST["dore"] in i.dore and request.POST["video_link"] in i.video_link and\
                                request.POST["detail"] in i.detail:
                    searched_obj.append(i)
            content = {
                "achievement":searched_obj
            }
            return render(request, "base/modiran_frame/managing.html", content)
        elif model_name == "student":
            searched_year = int(request.POST["birthday"]) if request.POST["birthday"] else 1
            for i in student_list:
                birth = i.birthday.year if request.POST["birthday"] else 0
                if request.POST["first_name"]  in i.first_name and (request.POST["last_name"])  in i.last_name and \
                    searched_year > birth:
                    searched_obj.append(i)
            content = {
                "student":searched_obj
            }
            return render(request, "base/modiran_frame/managing.html", content)

# @login_required
@require_GET
def delete(request, model_name, id):
    if model_name == "student":
        obj = get_object_or_404(Student, id=id)
    elif  model_name == "achievement":
        obj = get_object_or_404(Achievement, id=id)

    obj.delete()
    return HttpResponseRedirect(reverse('base:manage', args=[model_name]))

# @login_required
def form(request, model_name, id):
    request.POST._mutable = True
    massage = ""
    if request.method == "GET":
        if model_name == "student":
            obj = get_object_or_404(Student, id=id)
            initial = {
                "first_name":obj.first_name, "last_name":obj.last_name, "birthday":obj.birthday, "photo":obj.photo
            }
            content = {
                "form":StudentForm(initial=initial)
            }
        elif model_name == "new_student":
            content = {
                "form":StudentForm(),
            }
        elif model_name == "achievement":
            obj = get_object_or_404(Achievement, id=id)
            initial = {
                "owner":obj.owner, "title":obj.title, "year":obj.year, "field":obj.field, "level":obj.level, 
                "dore":obj.dore, "video_link":obj.video_link, "detail":obj.detail, "pic":obj.pic
            }
            content = {
                "form":AchievementForm(initial=initial)
            }
        elif model_name == "new_achievement":
            content = {
                "form":AchievementForm()
            }
        content.update({"date":timezone.now()})
        return render(request,"base/modiran_frame/form.html", content)
    elif request.method == "POST":
        if model_name == "student":
            jy, jm, jd = request.POST["birthday"].split("/")
            miladi_y, miladi_m, miladi_d = extentions.jalali_to_gregorian(int(jy), int(jm) ,int(jd))
            request.POST["birthday"] = f"{miladi_y}-{miladi_m}-{miladi_d}"
            filled_form = StudentForm(request.POST, request.FILES, instance=get_object_or_404(Student, id=id))
            if filled_form.is_valid():
                filled_form.save()
                massage = "با موفقیت تغییر یافت"
            else:
                massage = "خطا، اطلاعات وارد شده معتبر نمی باشد."
        elif model_name == "new_student":
            jy, jm, jd = request.POST["birthday"].split("/")
            miladi_y, miladi_m, miladi_d = extentions.jalali_to_gregorian(int(jy), int(jm) ,int(jd))
            request.POST["birthday"] = f"{miladi_y}-{miladi_m}-{miladi_d}"
            filled_form = StudentForm(request.POST, request.FILES)
            if filled_form.is_valid():
                filled_form.save()
                massage = "با موفقیت تغییر یافت"
            else:
                massage = "خطا، اطلاعات وارد شده معتبر نمی باشد."
        elif model_name == "achievement":
            filled_form = AchievementForm(request.POST, request.FILES, instance=get_object_or_404(Achievement, id=id))
            if filled_form.is_valid():
                filled_form.save()
                massage = "با موفقیت تغییر یافت"
            else:
                massage = "خطا، اطلاعات وارد شده معتبر نمی باشد"
        elif model_name == "new_achievement":
            filled_form = AchievementForm(request.POST, request.FILES)
            if filled_form.is_valid():
                filled_form.save()
                massage = "با موفقیت تغییر یافت"
            else:
                massage = "خطا، اطلاعات وارد شده معتبر نمی باشد"
        content = {
            "massage":massage
        }
        return render(request,"base/update_form.html", content)