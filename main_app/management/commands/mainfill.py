from django.core.management import BaseCommand

from main_app.models import Contact


class Command(BaseCommand):
    def handle(self, *args, **options):
        Contact.objects.all().delete()
        contacts = [
            Contact(name='Головной офис', phones='+71231235678', order=1, address='ул. Светлая, 12'),
            Contact(name='Пункт выдачи "Центр"', phones='+71231231122, +71231233344', order=2,
                    address='ул. Далекая, 3/14ц'),
        ]
        Contact.objects.bulk_create(contacts)
