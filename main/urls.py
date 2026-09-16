from django.urls import path
from main.views import (
    show_main,
    show_experience,
    show_project,
    show_education,
    create_project,
    create_education,
    update_education,
    delete_education,
    get_projects_json,
    get_education_json,
    delete_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("project/", show_project, name="show_project"),

    # Education
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path(
        "education/update/<uuid:id>/",
        update_education,
        name="update_education",
    ),
    path(
        "education/delete/<uuid:id>/",
        delete_education,
        name="delete_education",
    ),
    path(
        "api/education/",
        get_education_json,
        name="get_education_json",
    ),

    # Projects
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path(
        "projects/delete/<uuid:id>/",
        delete_project,
        name="delete_project",
    ),
]