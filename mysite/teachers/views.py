from django.shortcuts import render

from .models import Teacher


def index(request):
    teachers_list = list(Teacher.objects.all().values())
    context = {"teachers_list": teachers_list}
    return render(request, "teachers/index.html", context)
