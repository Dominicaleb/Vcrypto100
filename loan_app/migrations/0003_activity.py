# Generated by Django 4.1.6 on 2024-03-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_app', '0002_loanapplication_remove_loan_customer_delete_customer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
            ],
        ),
    ]
