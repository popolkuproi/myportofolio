from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Naufal Alvaro Habibullah",
        "npm": "2506657144",
        "study_program": "Ilmu Komputer",
        "bio": (
            "Computer Science student at the Universitas Indonesia with a strong interest in Software Engineering. I enjoy building software, learning new technologies, and solving problems through code."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Naufal Alvaro Habibullah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)