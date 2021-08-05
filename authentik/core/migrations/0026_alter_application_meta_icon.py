# Generated by Django 3.2.5 on 2021-07-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_core", "0025_alter_application_meta_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="meta_icon",
            field=models.FileField(
                default=None, max_length=500, null=True, upload_to="application-icons/"
            ),
        ),
        migrations.AlterModelOptions(
            name='authenticatedsession',
            options={'verbose_name': 'Authenticated Session', 'verbose_name_plural': 'Authenticated Sessions'},
        ),
    ]
