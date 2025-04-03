from django.core.management.base import BaseCommand
from nonprofits.models import Nonprofit

class Command(BaseCommand):
    help = 'Seeds the database with initial nonprofit data'

    def handle(self, *args, **options):
        nonprofits = [
            {
                'name': 'Red Cross',
                'address': '2025 E Street NW, Washington, DC 20006',
                'email': 'contact@redcross.org'
            },
            {
                'name': 'Doctors Without Borders',
                'address': '40 Rector Street, 16th Floor, New York, NY 10006',
                'email': 'contact@doctorswithoutborders.org'
            },
            {
                'name': 'World Wildlife Fund',
                'address': '1250 24th Street NW, Washington, DC 20037',
                'email': 'contact@worldwildlife.org'
            }
        ]

        for nonprofit_data in nonprofits:
            nonprofit, created = Nonprofit.objects.get_or_create(
                email=nonprofit_data['email'],
                defaults=nonprofit_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created nonprofit: {nonprofit.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Nonprofit already exists: {nonprofit.name}')) 