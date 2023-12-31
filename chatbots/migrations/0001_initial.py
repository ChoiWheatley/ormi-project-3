# Generated by Django 4.2.1 on 2023-07-30 11:53

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatBot",
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
                ("timestamp", models.TimeField(auto_now_add=True)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.member"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChatBotReply",
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
                ("prompt_token_usage", models.PositiveIntegerField()),
                ("completion_token_usage", models.PositiveIntegerField()),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chatbots.chatbot",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Prompt",
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
                ("prompt", models.CharField(max_length=2047)),
                ("answer", models.TextField(blank=True)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chatbots.chatbot",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Choice",
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
                ("role", models.CharField(max_length=255)),
                ("content", models.TextField(blank=True)),
                ("finish_reason", models.CharField(max_length=255)),
                ("index", models.PositiveIntegerField()),
                (
                    "reply",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chatbots.chatbotreply",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChatBotConfig",
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
                ("model", models.CharField(default="gpt-3.5-turbo", max_length=255)),
                (
                    "temperature",
                    models.DecimalField(
                        decimal_places=4, default=Decimal("1"), max_digits=5
                    ),
                ),
                ("stream", models.BooleanField(default=False)),
                ("max_tokens", models.PositiveIntegerField(default=4096)),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chatbots.chatbot",
                    ),
                ),
            ],
        ),
    ]
