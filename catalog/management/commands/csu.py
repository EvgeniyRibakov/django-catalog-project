from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email='evgenijrybakov01@gmail.com')
        user.set_password('1234qwe')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()