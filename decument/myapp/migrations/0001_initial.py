# Generated by Django 3.2.2 on 2021-05-09 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_download_files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_name', models.CharField(blank=True, max_length=30, null=True)),
                ('file_size', models.FileField(upload_to='file/')),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business', models.FileField(upload_to='documents/')),
                ('Realestate', models.FileField(upload_to='Realestate/')),
                ('Financial', models.FileField(upload_to='Financial/')),
                ('Family', models.FileField(upload_to='Family/')),
                ('All', models.FileField(upload_to='All/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Previous_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField()),
                ('Amount', models.FloatField()),
                ('discount', models.CharField(blank=True, max_length=30, null=True)),
                ('transaction_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestiMonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('UserDetail', models.CharField(max_length=30)),
                ('User_Test', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_NAME', models.CharField(blank=True, max_length=30, null=True)),
                ('EMAIL_iD', models.EmailField(blank=True, max_length=250, null=True)),
                ('MOBILE_NUMBER', models.BigIntegerField()),
                ('PLAN', models.CharField(choices=[('monthly', 'monthly'), ('anual', 'anual'), ('unlimited', 'unlimited')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AllPlan',
            fields=[
                ('previous_plan_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.previous_plan')),
                ('Action', models.FileField(upload_to='allplan/')),
            ],
            bases=('myapp.previous_plan',),
        ),
        migrations.AddField(
            model_name='previous_plan',
            name='plan_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.users'),
        ),
    ]