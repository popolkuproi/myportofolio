from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.utils.html import strip_tags

from main.models import Education, Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/username/project",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": (
                        "https://drive.google.com/thumbnail"
                        "?id=...&sz=w1000"
                    ),
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(
            self.cleaned_data["title"]
        ).strip()

        if not title:
            raise ValidationError(
                "Nama proyek tidak boleh hanya berisi tag HTML."
            )

        return title

    def clean_tech_stack(self):
        return strip_tags(
            self.cleaned_data["tech_stack"]
        ).strip()

    def clean_description(self):
        return strip_tags(
            self.cleaned_data["description"]
        ).strip()


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "description",
            "start_year",
            "end_year",
            "institution_url",
        ]

        labels = {
            "institution": "Institusi Pendidikan",
            "degree": "Program Studi / Gelar",
            "description": "Deskripsi",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Selesai",
            "institution_url": "URL Institusi",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "Ilmu Komputer",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pendidikanmu",
                    "rows": 3,
                }
            ),
            "start_year": TextInput(
                attrs={
                    "placeholder": "2025",
                }
            ),
            "end_year": TextInput(
                attrs={
                    "placeholder": "2029",
                }
            ),
            "institution_url": URLInput(
                attrs={
                    "placeholder": "https://cs.ui.ac.id",
                }
            ),
        }

    def clean_institution(self):
        institution = strip_tags(
            self.cleaned_data["institution"]
        ).strip()

        if not institution:
            raise ValidationError(
                "Institusi pendidikan tidak boleh hanya berisi tag HTML."
            )

        return institution

    def clean_degree(self):
        degree = strip_tags(
            self.cleaned_data["degree"]
        ).strip()

        if not degree:
            raise ValidationError(
                "Program studi atau gelar tidak boleh hanya berisi tag HTML."
            )

        return degree

    def clean_description(self):
        description = strip_tags(
            self.cleaned_data["description"]
        ).strip()

        if not description:
            raise ValidationError(
                "Deskripsi tidak boleh hanya berisi tag HTML."
            )

        return description
