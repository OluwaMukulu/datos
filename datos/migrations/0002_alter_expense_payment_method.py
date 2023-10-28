# Generated by Django 4.1 on 2023-10-26 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Cash", "Cash"),
                    ("Card", "Card"),
                    ("Credit", "Credit"),
                    ("Airtel Money", "Airtel Money"),
                    ("MTN Money", "MTN Money"),
                    ("Other", "Other"),
                ],
                max_length=30,
            ),
        ),
    ]
