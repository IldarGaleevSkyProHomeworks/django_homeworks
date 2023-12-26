import getpass

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.management import BaseCommand
from django.core.validators import validate_email

from accounts_app.models import User


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        try:
            email = None

            while email is None:
                email = input("Enter email: ")
                try:
                    validate_email(email)
                except ValidationError as e:
                    self.stderr.write('\n'.join(e.messages))
                    email = None

            while True:
                passwords = [None, None]
                for i in range(2):
                    while not passwords[i]:
                        passwords[i] = getpass.getpass(f"Password{'(again)' if i else ''}: ").strip()

                if passwords[0] != passwords[1]:
                    self.stderr.write("Error: Your passwords didn't match.")
                    continue

                try:
                    validate_password(passwords[0])
                    break
                except ValidationError as e:
                    self.stderr.write('\n'.join(e.messages))
                    response = input("Bypass password validation and create user anyway? [y/N]: ")
                    if response.lower() == 'y':
                        break

            user = User.objects.create(
                email=email,
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )

            user.set_password(passwords[0])
            user.save()

        except KeyboardInterrupt:
            self.stderr.write('\r\nOperation cancelled.')
            exit(1)
