# Generated by Django 4.2.2 on 2023-07-02 08:58

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model("posts_app", "post")
    for row in MyModel.objects.all():
        row.slug = uuid.uuid4()
        row.save(update_fields=["slug"])



class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_post_slug'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
