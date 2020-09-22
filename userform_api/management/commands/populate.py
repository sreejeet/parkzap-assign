from django.core.management.base import BaseCommand, CommandError
from userform_api.models import UserData
from ._private import data


class Command(BaseCommand):
    help = 'Populate the database with some dummy data'

    def add_arguments(self, parser):
        parser.add_argument('cleardb', nargs='?', type=bool,
                            help='Clear the database in case it has any data.')

    def handle(self, *args, **options):

        if UserData.objects.count() != 0:
            if options['cleardb']:
                self.stdout.write(self.style.SUCCESS(
                    'Deleting all records from UserData model...'))
                a = input("Proceed? [y/N]: ") or 'N'
                if a == 'y' or a == 'Y':
                    UserData.objects.all().delete()
                else:
                    raise CommandError('User aborted.')
            else:
                raise CommandError(
                    'Database is not empty. Cannot add dummy data to existing data. Pass "cleardb" arg to clear the database completely')

        self.stdout.write(self.style.SUCCESS(
            'Inserting dummy records into empty database...'))

        for record in data:
            user_data = UserData.objects.create(
                name=record['name'],
                email=record['email'],
                dob=record['dob'],
                phone=record['phone']
            )
            user_data.save()
            self.stdout.write(self.style.SUCCESS(
                f'Added user_data {user_data}'))

        self.stdout.write(self.style.SUCCESS(
            'Successfully inserted dummy records'))
