from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0005_rename_specification_specification_car_specification"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "brand_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("brand_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Model",
            fields=[
                (
                    "model_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("year", models.PositiveIntegerField()),
                ("model_name", models.CharField(max_length=50)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="App.brand",
                    ),
                ),
            ],
        ),
    ]
