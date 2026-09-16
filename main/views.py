from django.shortcuts import render, redirect

from django.core import serializers

from django.http import HttpResponse

from main.models import Education, Experience, Project

from main.forms import EducationForm, ProjectForm

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

def show_project(request):
    json_data = get_projects_json(request)
    data = json_data.content.decode("utf-8")

    context = {
        "name": "Naufal Alvaro Habibullah",
        "project_list": serializers.deserialize("json", data),
    }

    return render(request, "project.html", context)

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_project")
    else:
        form = ProjectForm()

    context = {
        "form": form,
        "name": "Naufal Alvaro Habibullah",
    }

    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title = request.GET.get("title")

    if title:
        data = Project.objects.filter(title__icontains=title)
    else:
        data = Project.objects.all()

    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def delete_project(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    return redirect("main:show_project")

def create_education(request):
    if request.method == "POST":
        form = EducationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("main:show_education")

    else:
        form = EducationForm()

    context = {
        "form": form,
        "name": "Naufal Alvaro Habibullah",
    }

    return render(request, "education_form.html", context)

def update_education(request, id):
    education = Education.objects.get(pk=id)

    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)

        if form.is_valid():
            form.save()
            return redirect("main:show_education")

    else:
        form = EducationForm(instance=education)

    context = {
        "form": form,
        "name": "Naufal Alvaro Habibullah",
        "education": education,
    }

    return render(request, "education_form.html", context)

def show_education(request):
    json_data = get_education_json(request)
    data = json_data.content.decode("utf-8")

    context = {
        "name": "Naufal Alvaro Habibullah",
        "education_list": serializers.deserialize("json", data),
    }

    return render(request, "education.html", context)

def get_education_json(request):
    data = Education.objects.all()

    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def delete_education(request, id):
    education = Education.objects.get(pk=id)
    education.delete()

    return redirect("main:show_education")