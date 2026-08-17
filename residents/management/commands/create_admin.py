from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Crée le compte administrateur s'il n'existe pas"

    def handle(self, *args, **kwargs):
        username = "admin"
        password = "homeless1234"

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("Le compte admin existe déjà.")
            )
        else:
            User.objects.create_superuser(
                username=username,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS("Compte admin créé avec succès.")
            )