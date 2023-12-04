# Generated by Django 4.2.7 on 2023-12-03 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleType",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "article_type",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Contract",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("valid_from", models.DateField(blank=True, null=True)),
                ("valid_to", models.DateField(blank=True, null=True)),
                ("number", models.CharField(max_length=50)),
                ("name", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "contract",
            },
        ),
        migrations.CreateModel(
            name="Country",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "countries",
                "db_table": "country",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Currency",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                ("code", models.CharField(max_length=3)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "currencies",
                "db_table": "currency",
                "ordering": ("code",),
            },
        ),
        migrations.CreateModel(
            name="DocumentType",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "document_type",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Journal",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                ("pissn", models.CharField(blank=True, max_length=9, null=True)),
                ("eissn", models.CharField(blank=True, max_length=9, null=True)),
                ("remark", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        db_column="country",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.country",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "journal",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="SubjectArea",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "subject_area",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Publisher",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("imprint", models.CharField(max_length=100)),
                (
                    "main_publisher",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "publisher",
                "ordering": ("imprint",),
            },
        ),
        migrations.CreateModel(
            name="ProfessionalSociety",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "professional societies",
                "db_table": "professional_society",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="LimitType",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "limit_type",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="LicenseType",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "license_type",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="JournalToSubjectArea",
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
                ("valid_from", models.DateField(blank=True, null=True)),
                ("valid_to", models.DateField(blank=True, null=True)),
                (
                    "journal",
                    models.ForeignKey(
                        db_column="journal",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.journal",
                    ),
                ),
                (
                    "subject_area",
                    models.ForeignKey(
                        db_column="subject_area",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.subjectarea",
                    ),
                ),
            ],
            options={
                "db_table": "journal_to_subject_area",
            },
        ),
        migrations.CreateModel(
            name="JournalToPublisher",
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
                ("valid_from", models.DateField(blank=True, null=True)),
                ("valid_to", models.DateField(blank=True, null=True)),
                (
                    "journal",
                    models.ForeignKey(
                        db_column="journal",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.journal",
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        db_column="publisher",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.publisher",
                    ),
                ),
            ],
            options={
                "db_table": "journal_to_publisher",
            },
        ),
        migrations.CreateModel(
            name="JournalToProfessionalSociety",
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
                ("valid_from", models.DateField(blank=True, null=True)),
                ("valid_to", models.DateField(blank=True, null=True)),
                (
                    "journal",
                    models.ForeignKey(
                        db_column="journal",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.journal",
                    ),
                ),
                (
                    "professional_society",
                    models.ForeignKey(
                        db_column="professional_society",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.professionalsociety",
                    ),
                ),
            ],
            options={
                "db_table": "journal_to_professional_society",
            },
        ),
        migrations.CreateModel(
            name="JournalToLicenseType",
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
                ("valid_from", models.DateField(blank=True, null=True)),
                ("valid_to", models.DateField(blank=True, null=True)),
                (
                    "journal",
                    models.ForeignKey(
                        db_column="journal",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.journal",
                    ),
                ),
                (
                    "license_type",
                    models.ForeignKey(
                        db_column="license_type",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.licensetype",
                    ),
                ),
            ],
            options={
                "db_table": "journal_to_license_type",
            },
        ),
        migrations.AddField(
            model_name="journal",
            name="license_type",
            field=models.ManyToManyField(
                through="main.JournalToLicenseType", to="main.licensetype"
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                db_column="modified_by",
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="professional_society",
            field=models.ManyToManyField(
                through="main.JournalToProfessionalSociety",
                to="main.professionalsociety",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="publisher",
            field=models.ManyToManyField(
                through="main.JournalToPublisher", to="main.publisher"
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="subject_area",
            field=models.ManyToManyField(
                through="main.JournalToSubjectArea", to="main.subjectarea"
            ),
        ),
        migrations.CreateModel(
            name="Institution",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                ("contracts_url", models.CharField(max_length=1000)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "institution",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="FeeScope",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "fee_scope",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Fee",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("membership", models.BooleanField(blank=True, null=True)),
                ("with_contract", models.BooleanField(blank=True, null=True)),
                ("foreign_author", models.BooleanField(blank=True, null=True)),
                ("fee_type", models.CharField(blank=True, max_length=20, null=True)),
                ("fee", models.DecimalField(decimal_places=2, max_digits=12)),
                ("factor", models.PositiveIntegerField(blank=True, null=True)),
                ("lower_limit", models.PositiveIntegerField(blank=True, null=True)),
                ("upper_limit", models.PositiveIntegerField(blank=True, null=True)),
                ("valid_from", models.DateField(blank=True, null=True)),
                ("remark", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "article_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="article_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.articletype",
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        blank=True,
                        db_column="contract",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.contract",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        db_column="currency",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.currency",
                    ),
                ),
                (
                    "document_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="document_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.documenttype",
                    ),
                ),
                (
                    "fee_scope",
                    models.ForeignKey(
                        blank=True,
                        db_column="fee_scope",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.feescope",
                    ),
                ),
                (
                    "journal",
                    models.ForeignKey(
                        db_column="journal",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.journal",
                    ),
                ),
                (
                    "license_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="license_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.licensetype",
                    ),
                ),
                (
                    "limit_type",
                    models.ForeignKey(
                        blank=True,
                        db_column="limit_type",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.limittype",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "fee",
            },
        ),
        migrations.CreateModel(
            name="DiscountLevel",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "discount_level",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Discount",
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
                ("date_created", models.DateTimeField()),
                ("date_modified", models.DateTimeField(blank=True, null=True)),
                ("with_contract", models.BooleanField(blank=True, null=True)),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Discount [%]"
                    ),
                ),
                ("remark", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "contract",
                    models.ForeignKey(
                        blank=True,
                        db_column="contract",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.contract",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "discount_level",
                    models.ForeignKey(
                        db_column="discount_level",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.discountlevel",
                    ),
                ),
                (
                    "journal",
                    models.ForeignKey(
                        db_column="journal",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.journal",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="modified_by",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "discount",
            },
        ),
        migrations.AddField(
            model_name="contract",
            name="institution",
            field=models.ForeignKey(
                db_column="institution",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="main.institution",
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="modified_by",
            field=models.ForeignKey(
                blank=True,
                db_column="modified_by",
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="publisher",
            field=models.ForeignKey(
                db_column="publisher",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="main.publisher",
            ),
        ),
    ]
