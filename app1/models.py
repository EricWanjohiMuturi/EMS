from django.db import models # type: ignore

# Create your models here.
class Employee(models.Model):

    GENDER_CHOICES={
        ("male","male"),
        ("female","female"),
        ("others","others")
    }

    COUNTY_CHOICES = [
        ("Baringo", "Baringo"),
        ("Bomet", "Bomet"),
        ("Bungoma", "Bungoma"),
        ("Busia", "Busia"),
        ("Elgeyo-Marakwet", "Elgeyo-Marakwet"),
        ("Embu", "Embu"),
        ("Garissa", "Garissa"),
        ("Homa Bay", "Homa Bay"),
        ("Isiolo", "Isiolo"),
        ("Kajiado", "Kajiado"),
        ("Kakamega", "Kakamega"),
        ("Kericho", "Kericho"),
        ("Kiambu", "Kiambu"),
        ("Kilifi", "Kilifi"),
        ("Kirinyaga", "Kirinyaga"),
        ("Kisii", "Kisii"),
        ("Kisumu", "Kisumu"),
        ("Kitui", "Kitui"),
        ("Kwale", "Kwale"),
        ("Laikipia", "Laikipia"),
        ("Lamu", "Lamu"),
        ("Machakos", "Machakos"),
        ("Makueni", "Makueni"),
        ("Mandera", "Mandera"),
        ("Marsabit", "Marsabit"),
        ("Meru", "Meru"),
        ("Migori", "Migori"),
        ("Mombasa", "Mombasa"),
        ("Murang'a", "Murang'a"),
        ("Nairobi", "Nairobi"),
        ("Nakuru", "Nakuru"),
        ("Nandi", "Nandi"),
        ("Narok", "Narok"),
        ("Nyamira", "Nyamira"),
        ("Nyandarua", "Nyandarua"),
        ("Nyeri", "Nyeri"),
        ("Samburu", "Samburu"),
        ("Siaya", "Siaya"),
        ("Taita-Taveta", "Taita-Taveta"),
        ("Tana River", "Tana River"),
        ("Tharaka-Nithi", "Tharaka-Nithi"),
        ("Trans Nzoia", "Trans Nzoia"),
        ("Turkana", "Turkana"),
        ("Uasin Gishu", "Uasin Gishu"),
        ("Vihiga", "Vihiga"),
        ("Wajir", "Wajir"),
        ("West Pokot", "West Pokot"),
    ]



    name = models.CharField(max_length=225)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    DOB = models.DateField(auto_now_add=False, auto_now=False, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default="others")
    skills = models.CharField(max_length=100)
    County = models.CharField(max_length=100, choices=COUNTY_CHOICES) 
    Residence = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="employee_profile_pic/", null=True, blank=True)
    resume=models.FileField(upload_to="employee_resume/", null=True, blank=True)
    video=models.FileField(upload_to="employee_video/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"