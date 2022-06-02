# Generated by Django 4.0.4 on 2022-06-02 19:49

from os import getenv
from django.db import migrations
from django.db.migrations.state import StateApps

from dotenv import load_dotenv

from user.models import User

load_dotenv()


def default_user_admin(apps: StateApps, _):
    user: User = apps.get_model("user", "User")
    user.objects.create_superuser(
        username=getenv("ADMIN_USERNAME"),
        password=getenv("ADMIN_PASSWORD"),
        email=getenv("ADMIN_EMAIL"),
        first_name=getenv("ADMIN_NAME"),
    )


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_rename_id_user_user_uuid"),
    ]

    operations = [migrations.RunPython(default_user_admin)]
