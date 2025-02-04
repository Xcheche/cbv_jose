# Generated by Django 5.0.6 on 2024-08-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classroom", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="teacher",
            name="first_name",
            field=models.CharField(
                help_text="Enter your first name",
                max_length=100,
                verbose_name="First Name",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="last_name",
            field=models.CharField(
                help_text="Enter your last name",
                max_length=100,
                verbose_name="Last Name",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="subject",
            field=models.CharField(help_text="Enter your subject", max_length=100),
        ),
    ]
