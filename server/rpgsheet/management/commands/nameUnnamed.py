from django.core.management.base import BaseCommand, CommandError
from rpgsheet.models import CharacterInformation
import json

class Command(BaseCommand):
    help = 'Names characters that dont have a name in the db'

    def handle(self, *args, **options):
        for obj in CharacterInformation.objects.filter(name=""):
            try:
                open_data = json.loads(obj.data)
                name = open_data["characterInformation"]["name"]
                obj.name = name
                obj.save()
                print("Named", name)
            except Exception as e:
                print("Skipped", obj.key, "due to", e)
        print("Done")
