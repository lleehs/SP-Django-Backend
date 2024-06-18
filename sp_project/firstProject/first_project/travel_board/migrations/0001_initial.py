# Generated by Django 5.0.6 on 2024-06-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TravelBoard",
            fields=[
                ("boardId", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=128)),
                ("writer", models.CharField(max_length=32)),
                (
                    "point",
                    models.IntegerField(
                        choices=[
                            (0, "ZERO"),
                            (1, "ONE"),
                            (2, "TWO"),
                            (3, "THREE"),
                            (4, "FOUR"),
                            (5, "FIVE"),
                        ],
                        default=0,
                    ),
                ),
                ("review", models.TextField()),
                ("regDate", models.DateTimeField(auto_now_add=True)),
                ("updDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "travel_board",
            },
        ),
    ]
