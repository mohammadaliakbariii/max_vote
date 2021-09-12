from django.core.management.base import BaseCommand,CommandError
from polls.models import Choice
import logging
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--zero',
            action='store_true',
            help="vote for choices will be zero"
        )

    def handle(self, *args, **options):
        if options['zero']:
            logging.info("vote of choices updated")
            choices=Choice.objects.all()
            for choice in choices:

                choice.vote=0
                choice.save()
        else:
            logging.error("pleaze enter correct arguman")

