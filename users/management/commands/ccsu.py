from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=input('Enter an email\n'),
            phone=input('Enter a phone\n'),
            country=input('Enter a county\n'),
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password(input('Enter a password\n'))
        user.save()
