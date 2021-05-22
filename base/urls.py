from django.urls import path
from .views import index, detail, manage, delete, form

app_name = "base"
urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:id>', detail, name="detail"),
    path('manage/<str:model_name>', manage, name="manage"),
    path('manage/delete/<str:model_name>/<int:id>', delete, name="delete"),
    path('manage/form/<str:model_name>/<int:id>', form, name="form"),
]