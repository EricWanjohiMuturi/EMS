# Generated by Django 5.1.2 on 2024-12-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveIntegerField()),
                ('DOB', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], default='others', max_length=255)),
                ('skills', models.CharField(max_length=100)),
                ('County', models.CharField(choices=[('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Kwale', 'Kwale'), ('Laikipia', 'Laikipia'), ('Lamu', 'Lamu'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Meru', 'Meru'), ('Migori', 'Migori'), ('Mombasa', 'Mombasa'), ("Murang'a", "Murang'a"), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Nyamira', 'Nyamira'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Siaya', 'Siaya'), ('Taita-Taveta', 'Taita-Taveta'), ('Tana River', 'Tana River'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Turkana', 'Turkana'), ('Uasin Gishu', 'Uasin Gishu'), ('Vihiga', 'Vihiga'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot')], max_length=100)),
                ('Residence', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='employee_profile_pic/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='employee_resume/')),
                ('video', models.FileField(blank=True, null=True, upload_to='employee_video/')),
            ],
        ),
    ]
