from django.core.management.base import BaseCommand
from teachers.models import Teacher

from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("teachers_count", nargs="?", type=int, default=100)

    def handle(self, *args, teachers_count, **options):
        faker = Faker()
        teachers = [
            Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=faker.pyint(min_value=22, max_value=80),
                email=faker.email(),
            )
            for _ in range(teachers_count)
        ]

        Teacher.objects.bulk_create(teachers)

        self.stdout.write(
            self.style.SUCCESS("Successfully created %s teachers" % teachers_count)
        )
