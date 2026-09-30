from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST

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
    title_query = request.GET.get("title", "").strip()

    is_editor = (
        request.user.is_authenticated
        and request.user.groups.filter(name="Editor").exists()
    )

    context = {
        "name": "Naufal Alvaro Habibullah",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": ProjectForm(),
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


@require_POST
def create_project_ajax(request):
    """
    Membuat project baru melalui AJAX.

    Endpoint ini hanya menerima POST dan hanya dapat digunakan
    oleh pemilik portfolio (superuser).
    """

    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": (
                    "Hanya pemilik portofolio yang dapat "
                    "menambahkan proyek."
                )
            },
            status=403,
        )

    form = ProjectForm(request.POST)

    if form.is_valid():
        project = form.save()

        return JsonResponse(
            {
                "message": "Proyek berhasil ditambahkan.",
                "pk": str(project.id),
            },
            status=201,
        )

    return JsonResponse(
        {
            "errors": form.errors.get_json_data(),
        },
        status=400,
    )


@login_required(login_url="/login/")
def update_project(request, id):
    project = get_object_or_404(Project, pk=id)

    is_editor = request.user.groups.filter(
        name="Editor"
    ).exists()

    if not request.user.is_superuser and not is_editor:
        raise PermissionDenied

    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            form.save()
            return redirect("main:show_project")
    else:
        form = ProjectForm(
            instance=project
        )

    context = {
        "form": form,
        "name": "Naufal Alvaro Habibullah",
        "project": project,
    }

    return render(
        request,
        "projects_form.html",
        context
    )


def get_projects_json(request):
    title_query = request.GET.get(
        "title",
        ""
    ).strip()

    projects = Project.objects.prefetch_related(
        "starred_by"
    ).all()

    if title_query:
        projects = projects.filter(
            title__icontains=title_query
        )

    data = []

    for project in projects:
        starred_users = project.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        starred_by_names = ", ".join(
            user.username
            for user in starred_users
        )

        data.append(
            {
                "pk": str(project.id),
                "fields": {
                    "title": project.title,
                    "description": project.description,
                    "tech_stack": project.tech_stack,
                    "project_url": project.project_url,
                    "project_image_url": (
                        project.project_image_url
                    ),
                    "star_count": starred_users.count(),
                    "is_starred": is_starred,
                    "starred_by_names": starred_by_names,
                },
            }
        )

    return JsonResponse(
        data,
        safe=False
    )


@login_required(login_url="/login/")
def delete_project(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(
        Project,
        pk=id
    )

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

    return render(
        request,
        "education_form.html",
        context
    )


def update_education(request, id):
    education = get_object_or_404(
        Education,
        pk=id
    )

    if request.method == "POST":
        form = EducationForm(
            request.POST,
            instance=education
        )

        if form.is_valid():
            form.save()
            return redirect("main:show_education")
    else:
        form = EducationForm(
            instance=education
        )

    context = {
        "form": form,
        "name": "Naufal Alvaro Habibullah",
        "education": education,
    }

    return render(
        request,
        "education_form.html",
        context
    )


def show_education(request):
    json_data = get_education_json(request)
    data = json_data.content.decode("utf-8")

    context = {
        "name": "Naufal Alvaro Habibullah",
        "education_list": serializers.deserialize(
            "json",
            data
        ),
    }

    return render(
        request,
        "education.html",
        context
    )


def get_education_json(request):
    data = Education.objects.all()

    return HttpResponse(
        serializers.serialize(
            "json",
            data
        ),
        content_type="application/json"
    )


def delete_education(request, id):
    education = get_object_or_404(
        Education,
        pk=id
    )

    education.delete()

    return redirect(
        "main:show_education"
    )


def register(request):
    form = UserCreationForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Akun berhasil dibuat. Silakan login."
        )

        return redirect(
            "main:login"
        )

    context = {
        "name": "Naufal Alvaro Habibullah",
        "form": form,
    }

    return render(
        request,
        "register.html",
        context
    )


def login_user(request):
    form = AuthenticationForm(
        request,
        data=request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        user = form.get_user()

        login(
            request,
            user
        )

        response = redirect(
            "main:show_main"
        )

        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        return response

    context = {
        "name": "Naufal Alvaro Habibullah",
        "form": form,
    }

    return render(
        request,
        "login.html",
        context
    )


def logout_user(request):
    logout(request)

    response = redirect(
        "main:show_main"
    )

    response.delete_cookie(
        "last_login"
    )

    return response


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id
    )

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(
                request.user
            )
        else:
            project.starred_by.add(
                request.user
            )

    return redirect(
        "main:show_project"
    )