from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создает группу Moderators с нужными правами'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Moderators')
        permissions = [
            Permission.objects.get(codename='can_edit_product'),
            Permission.objects.get(codename='can_edit_description'),
        ]
        group.permissions.set(permissions)
        self.stdout.write(self.style.SUCCESS('Группа Moderators успешно создана или обновлена'))
