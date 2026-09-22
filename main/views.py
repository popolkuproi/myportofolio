from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

import datetime

from main.models import Education, Experience, Project
from main.forms import EducationForm, ProjectForm


def show_main(request):
    last_login = request.COOKIES.get(
        "last_login",
        "Belum ada sesi login / Cookie tidak ditemukan"
    )

    context = {
        "name": "Naufal Alvaro Habibullah",
        "npm": "2506657144",
        "study_program": "Ilmu Komputer",
        "bio": (
            "Computer Science student at the Universitas Indonesia "
            "with a strong interest in Software Engineering. "
            "I enjoy building software, learning new technologies, "
            "and solving problems through code."
        ),
        "last_login": last_login,
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


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

    projects_json = serializers.serialize(
        "json",
        data,
        use_natural_foreign_keys=True
    )

    return HttpResponse(
        projects_json,
        content_type="application/json"
    )


@login_required(login_url="/login/")
def delete_project(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

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


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Akun berhasil dibuat. Silakan login."
        )
        return redirect("main:login")

    context = {
        "name": "Naufal Alvaro Habibullah",
        "form": form,
    }

    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(
        request,
        data=request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        response = redirect("main:show_main")

        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        return response

    context = {
        "name": "Naufal Alvaro Habibullah",
        "form": form,
    }

    return render(request, "login.html", context)


def logout_user(request):
    logout(request)

    response = redirect("main:show_main")
    response.delete_cookie("last_login")

    return response


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id
    )

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")