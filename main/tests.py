from django.test import TestCase
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.utils import timezone

from main.models import Education, Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"'
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(
            str(self.experience),
            "Asisten Dosen PBP"
        )
        self.assertEqual(
            self.experience.category,
            "part-time"
        )
        self.assertTrue(
            self.experience.is_ongoing
        )

    def test_experience_page(self):
        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "experience.html"
        )
        self.assertContains(
            response,
            self.experience.title
        )
        self.assertContains(
            response,
            self.experience.description
        )
        self.assertContains(
            response,
            "Part-Time"
        )
        self.assertContains(
            response,
            "Sedang berlangsung"
        )
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertContains(
            response,
            "Belum ada pengalaman yang ditambahkan."
        )

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertFalse(
            self.experience.is_ongoing
        )
        self.assertContains(
            response,
            "Selesai"
        )
        self.assertNotContains(
            response,
            "Sedang berlangsung"
        )


class ProjectTest(TestCase):
    def test_project_page_url(self):
        response = self.client.get(
            reverse("main:show_project")
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "project.html"
        )

    def test_project_data_appears(self):
        Project.objects.create(
            title="FinTrack",
            description=(
                "A personal finance dashboard for tracking income, "
                "expenses, transactions, and cash flow."
            ),
            tech_stack="HTML, CSS, JavaScript, LocalStorage",
        )

        response = self.client.get(
            reverse("main:get_projects_json")
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response["Content-Type"],
            "application/json"
        )

        data = response.json()

        self.assertEqual(
            len(data),
            1
        )
        self.assertEqual(
            data[0]["fields"]["title"],
            "FinTrack"
        )
        self.assertEqual(
            data[0]["fields"]["description"],
            (
                "A personal finance dashboard for tracking income, "
                "expenses, transactions, and cash flow."
            )
        )
        self.assertEqual(
            data[0]["fields"]["tech_stack"],
            "HTML, CSS, JavaScript, LocalStorage"
        )

    def test_project_empty_state(self):
        response = self.client.get(
            reverse("main:get_projects_json")
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response["Content-Type"],
            "application/json"
        )

        data = response.json()

        self.assertEqual(
            data,
            []
        )

    def test_project_json(self):
        Project.objects.create(
            title="FinTrack",
            description=(
                "A personal finance dashboard for tracking income, "
                "expenses, transactions, and cash flow."
            ),
            tech_stack="HTML, CSS, JavaScript, LocalStorage",
        )

        response = self.client.get(
            reverse("main:get_projects_json")
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            response["Content-Type"],
            "application/json"
        )

        data = response.json()

        self.assertEqual(
            len(data),
            1
        )
        self.assertEqual(
            data[0]["fields"]["title"],
            "FinTrack"
        )


class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="Ilmu Komputer",
            description="Mahasiswa Ilmu Komputer",
            start_year=2025,
            end_year=2029,
            institution_url="https://cs.ui.ac.id",
        )

        self.superuser = User.objects.create_superuser(
            username="owner",
            password="test-password",
        )

        self.regular_user = User.objects.create_user(
            username="visitor",
            password="test-password",
        )

        self.editor = User.objects.create_user(
            username="editor",
            password="test-password",
        )

        editor_group, _ = Group.objects.get_or_create(
            name="Editor"
        )
        self.editor.groups.add(editor_group)

        self.education_data = {
            "institution": "Institut Teknologi Bandung",
            "degree": "Teknik Informatika",
            "description": "Pendidikan Teknik Informatika",
            "start_year": 2025,
            "end_year": 2029,
            "institution_url": "https://itb.ac.id",
        }

    def test_education_model(self):
        self.assertEqual(
            str(self.education),
            "Ilmu Komputer - Universitas Indonesia"
        )

    def test_show_education(self):
        response = self.client.get(
            reverse("main:show_education")
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "education.html"
        )
        self.assertContains(response, "education-grid")
        self.assertNotContains(
            response,
            "<h2>Universitas Indonesia</h2>",
            html=True,
        )

    def test_education_json_is_public_and_returns_manual_data(self):
        response = self.client.get(
            reverse("main:get_education_json")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")

        data = response.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["pk"], str(self.education.id))
        self.assertEqual(
            data[0]["fields"]["institution"],
            "Universitas Indonesia",
        )
        self.assertEqual(
            data[0]["fields"]["degree"],
            "Ilmu Komputer",
        )

    def test_education_json_searches_by_institution(self):
        Education.objects.create(
            institution="Universitas Gadjah Mada",
            degree="Sistem Informasi",
            description="Mahasiswa Sistem Informasi",
            start_year=2025,
            institution_url="https://ugm.ac.id",
        )

        response = self.client.get(
            reverse("main:get_education_json"),
            {"institution": "indonesia"},
        )

        data = response.json()

        self.assertEqual(len(data), 1)
        self.assertEqual(
            data[0]["fields"]["institution"],
            "Universitas Indonesia",
        )

    def test_anonymous_user_cannot_create_education_via_ajax(self):
        response = self.client.post(
            reverse("main:create_education_ajax"),
            self.education_data,
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Education.objects.count(), 1)

    def test_regular_user_cannot_create_education_via_ajax(self):
        self.client.force_login(self.regular_user)

        response = self.client.post(
            reverse("main:create_education_ajax"),
            self.education_data,
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Education.objects.count(), 1)

    def test_superuser_can_create_education_via_ajax(self):
        self.client.force_login(self.superuser)

        response = self.client.post(
            reverse("main:create_education_ajax"),
            self.education_data,
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json()["message"],
            "Pendidikan berhasil ditambahkan.",
        )

        self.assertTrue(
            Education.objects.filter(
                institution="Institut Teknologi Bandung"
            ).exists()
        )

    def test_invalid_education_ajax_request_returns_validation_errors(self):
        self.client.force_login(self.superuser)
        invalid_data = self.education_data | {
            "institution": '<img src="x" onerror="alert(\'XSS!\')">',
        }

        response = self.client.post(
            reverse("main:create_education_ajax"),
            invalid_data,
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("institution", response.json()["errors"])
        self.assertEqual(Education.objects.count(), 1)

    def test_education_form_strips_html_tags_from_text_input(self):
        self.client.force_login(self.superuser)
        sanitized_data = self.education_data | {
            "institution": "<b>Institut Teknologi Bandung</b>",
        }

        response = self.client.post(
            reverse("main:create_education_ajax"),
            sanitized_data,
        )

        self.assertEqual(response.status_code, 201)
        education = Education.objects.get(
            institution="Institut Teknologi Bandung"
        )
        self.assertEqual(
            education.institution,
            "Institut Teknologi Bandung",
        )

    def test_editor_can_update_education(self):
        self.client.force_login(self.editor)

        response = self.client.post(
            reverse(
                "main:update_education",
                args=[self.education.id]
            ),
            {
                "institution": "Universitas Indonesia",
                "degree": "Sistem Informasi",
                "description": "Updated description",
                "start_year": 2025,
                "end_year": 2029,
                "institution_url": "https://cs.ui.ac.id",
            },
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.education.refresh_from_db()

        self.assertEqual(
            self.education.degree,
            "Sistem Informasi"
        )

    def test_regular_user_cannot_delete_education(self):
        self.client.force_login(self.regular_user)

        response = self.client.get(
            reverse(
                "main:delete_education",
                args=[self.education.id]
            )
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Education.objects.filter(id=self.education.id).exists()
        )

    def test_anonymous_user_cannot_delete_education_via_ajax(self):
        response = self.client.post(
            reverse(
                "main:delete_education_ajax",
                args=[self.education.id],
            )
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(
            Education.objects.filter(id=self.education.id).exists()
        )

    def test_regular_user_cannot_delete_education_via_ajax(self):
        self.client.force_login(self.regular_user)

        response = self.client.post(
            reverse(
                "main:delete_education_ajax",
                args=[self.education.id],
            )
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.json()["message"],
            "Hanya pemilik portofolio yang dapat menghapus pendidikan.",
        )
        self.assertTrue(
            Education.objects.filter(id=self.education.id).exists()
        )

    def test_superuser_can_delete_education_via_ajax(self):
        education_id = self.education.id
        self.client.force_login(self.superuser)

        response = self.client.post(
            reverse(
                "main:delete_education_ajax",
                args=[education_id],
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["message"],
            "Pendidikan berhasil dihapus.",
        )
        self.assertFalse(
            Education.objects.filter(id=education_id).exists()
        )

    def test_superuser_can_delete_education(self):
        education_id = self.education.id
        self.client.force_login(self.superuser)

        response = self.client.get(
            reverse(
                "main:delete_education",
                args=[education_id]
            )
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertFalse(
            Education.objects.filter(
                id=education_id
            ).exists()
        )
