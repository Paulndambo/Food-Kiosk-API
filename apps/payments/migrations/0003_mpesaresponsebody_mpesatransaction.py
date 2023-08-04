# Generated by Django 4.2.1 on 2023-08-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_amount_payment_orderpayment_amount_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaResponseBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('body', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MpesaTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('receipt_number', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('merchant_request_id', models.CharField(max_length=255)),
                ('checkout_request_id', models.CharField(max_length=255)),
                ('transaction_result_code', models.CharField(max_length=255)),
                ('transaction_timestamp', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]