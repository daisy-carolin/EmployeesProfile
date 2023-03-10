from django.db import models
import datetime



# Create your models here.
class Employee(models.Model):
    first_name = models.CharField( max_length=12, null=True)

    last_name = models.CharField(max_length=15, null=True)

    age = models.PositiveSmallIntegerField()

    date_of_birth = models.DateField(max_length=27, null=True)

    roll_number=models.CharField(max_length=10, null=True)

    email_adress=models.EmailField(max_length=50,null=True)
   
    nationality=models.CharField(max_length=150,null=True)
   
    employee_id=models.PositiveSmallIntegerField(null=True)
   
    id_number=models.CharField( max_length=10, null=True)

    GENDER_CHOICES=(
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'O', u'Others'),
    )
    gender=models.CharField( max_length=1, choices=GENDER_CHOICES, null=True )

    phone_number=models.CharField(max_length=15, null=True)

    # image=models.ImageField(upload_to='images',blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

   
    medical_report=models.FileField(null=True,
        upload_to='documents/')
   
    date_of_enrollment=models.DateField(max_length=10,null=True)
   
    course_name=models.CharField(max_length=100, null=True)

   
    LANGUAGE_CHOICES=(
        (u'E', u'English'),
         (u'S', u'Swahili'),
         (U'K', u'Kikuyu'),
         (U'R', u'kinyarwanda'),
         (U'U', u'Kiganda'))
   
    languages=models.CharField(max_length=2, choices=LANGUAGE_CHOICES, null=True)
   
    laptop_serial_number=models.CharField( max_length=20, blank=True,null=True)

    def full_name(self):
        return f"{self.first_name}{self.last_name}"

    def year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year
        return year-self.age