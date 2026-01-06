from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("marketing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LeadSource",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, unique=True)),
                ("slug", models.SlugField(max_length=120, unique=True)),
                ("notes", models.TextField(blank=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="NewsletterSignup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("organization", models.CharField(blank=True, max_length=180)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.RenameField(
            model_name="lead",
            old_name="name",
            new_name="full_name",
        ),
        migrations.RenameField(
            model_name="lead",
            old_name="org",
            new_name="organization",
        ),
        migrations.RenameField(
            model_name="lead",
            old_name="email",
            new_name="work_email",
        ),
        migrations.AlterField(
            model_name="lead",
            name="country",
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name="lead",
            name="full_name",
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name="lead",
            name="organization",
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name="lead",
            name="work_email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="lead",
            name="use_case",
            field=models.CharField(
                choices=[
                    ("incident_response", "Incident response"),
                    ("perimeter_security", "Perimeter security"),
                    ("crowd_monitoring", "Crowd monitoring"),
                    ("critical_asset", "Critical asset monitoring"),
                    ("search_rescue", "Search & rescue"),
                    ("traffic", "Traffic & mobility"),
                    ("inspection", "Infrastructure inspection"),
                    ("other", "Other"),
                ],
                max_length=40,
            ),
        ),
        migrations.AddField(
            model_name="lead",
            name="consent",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="lead",
            name="sector",
            field=models.CharField(
                choices=[
                    ("law_enforcement", "Law Enforcement"),
                    ("private_security", "Private Security"),
                    ("critical_infra", "Critical Infrastructure"),
                    ("government", "Government / Defense"),
                    ("smart_city", "Smart City / Traffic"),
                    ("emergency_response", "Emergency Response"),
                    ("industrial", "Industrial Operations"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=40,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="lead",
            name="source",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="leads",
                to="marketing.leadsource",
            ),
        ),
    ]
