from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


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
            reverse("main:show_project")
        )

        self.assertContains(
            response,
            "FinTrack"
        )
        self.assertContains(
            response,
            "A personal finance dashboard"
        )
        self.assertContains(
            response,
            "HTML, CSS, JavaScript, LocalStorage"
        )

    def test_project_empty_state(self):
        response = self.client.get(
            reverse("main:show_project")
        )

        self.assertContains(
            response,
            "Belum ada project yang ditambahkan."
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