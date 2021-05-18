from django.db import models
from django.utils import timezone


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    photo = models.ImageField(upload_to="photoes/students/%Y/%m/%d")
    # class Meta:
    #     unique_together = (("first_name", "last_name"),)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


class Achievement(models.Model):
    owner = models.ForeignKey("Student" , on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    year = models.DateField()

    f_CHOICES = (("parvareshi","پرورشی"), 
                ("amoozeshi","آموزشی"), 
                ("pajooheshi","پژوهشی"), 
                ("varzeshi","ورزشی"))
    field = models.CharField(max_length=50, choices=f_CHOICES)

    v_CHOICES = (("parvareshi","مدرسه"), 
                ("amoozeshi","ناحیه"), 
                ("pajooheshi","شهر"), 
                ("varzeshi","استان"),
                ("varzeshi","کشور"),
                ("varzeshi","بین الملل"))
    level = models.CharField(max_length=50, choices=v_CHOICES)
    dore = models.CharField(max_length=50, choices=(("aval","اول"), ("dovom", "دوم")))
    pic = models.ImageField(upload_to="photoes/achievement/%Y/%m/%d", blank=True)
    video_link = models.CharField(max_length=255, blank=True)
    detail = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return(self.title)