# Generated by Django 4.2.3 on 2023-07-22 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('account_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AccountTypes',
            fields=[
                ('account_type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('company_type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('auth_token', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField()),
                ('monthly_fee', models.FloatField()),
                ('notes', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('whatsapp_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DispatchEntry',
            fields=[
                ('dispatch_entry_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('partner_caseid', models.IntegerField()),
                ('partner_service_id', models.IntegerField()),
                ('repair_status', models.CharField(max_length=100)),
                ('scheduled_date', models.DateField()),
                ('is_scheduled', models.BooleanField()),
                ('pickup_location', models.CharField(max_length=100)),
                ('dropoff_location', models.CharField(max_length=100, null=True)),
                ('eta', models.DateTimeField()),
                ('ata', models.DateTimeField(null=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.accounts')),
            ],
        ),
        migrations.CreateModel(
            name='DispatchStatus',
            fields=[
                ('dispatch_status_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('feature_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('reference_number', models.CharField(max_length=100)),
                ('ponumber', models.CharField(max_length=100)),
                ('txn_number', models.CharField(max_length=100)),
                ('customer', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('subtotal', models.FloatField()),
                ('tax', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('billing_email', models.EmailField(max_length=254)),
                ('dispatch_amount', models.FloatField()),
                ('dispatch_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reasons',
            fields=[
                ('reason_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('service_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTypes',
            fields=[
                ('service_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('service', models.CharField(max_length=100)),
                ('service_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('csr_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('role', models.CharField(max_length=50)),
                ('role_id', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=100)),
                ('vehicle_class', models.CharField(max_length=100)),
                ('vehicle_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SystemUserStatusRecords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('previous_csr_id', models.IntegerField()),
                ('new_csr_id', models.IntegerField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('dispatch_entry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.dispatchentry')),
            ],
        ),
        migrations.CreateModel(
            name='RateItem',
            fields=[
                ('rate_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=100)),
                ('account_company_id', models.IntegerField()),
                ('default_rate_4w', models.IntegerField()),
                ('default_rate_2w', models.IntegerField()),
                ('budget_2w', models.IntegerField()),
                ('premium_2w', models.IntegerField()),
                ('luxury_2w', models.IntegerField()),
                ('budget_4w', models.IntegerField()),
                ('premium_4w', models.IntegerField()),
                ('luxury_4w', models.IntegerField()),
                ('suv_4w', models.IntegerField()),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.accounts')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.vehicles')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('notes', models.TextField()),
                ('txn_number', models.CharField(max_length=100)),
                ('payment_type', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.invoices')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLocation',
            fields=[
                ('driverLocation_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.company')),
            ],
        ),
        migrations.CreateModel(
            name='DispatchEntryAssets',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('colorid', models.IntegerField()),
                ('body_type_id', models.IntegerField()),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('model_year', models.IntegerField()),
                ('license_plate', models.CharField(max_length=100)),
                ('license_state', models.CharField(max_length=100)),
                ('license_year', models.IntegerField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.customers')),
                ('dispatch_entry_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.dispatchentry')),
            ],
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='asset_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.dispatchentryassets'),
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='case_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.cases'),
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.company'),
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='csr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.systemuser'),
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.customers'),
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='dispatch_status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.dispatchstatus'),
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='reason_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.reasons'),
        ),
        migrations.AddField(
            model_name='dispatchentry',
            name='service_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.servicetypes'),
        ),
        migrations.CreateModel(
            name='CustomerFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.customers')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPricing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('default_rate', models.FloatField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.company')),
                ('rate_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.rateitem')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_features_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.company')),
                ('feature_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.features')),
            ],
        ),
        migrations.AddField(
            model_name='cases',
            name='csr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.systemuser'),
        ),
        migrations.AddField(
            model_name='cases',
            name='dispatch_entry_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='A2Zbackend.dispatchentry'),
        ),
    ]
