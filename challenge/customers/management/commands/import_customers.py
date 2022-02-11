from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Import customers from csv file"

    def add_arguments(self, parser):
        parser.add_argument("filepath", type=str)

    def handle(self, *args, **options):
        # TODO fill this
        print("Done")
