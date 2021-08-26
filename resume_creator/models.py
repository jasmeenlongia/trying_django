from django.db import models


# Create your models here.

class Information(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    slug = models.SlugField()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.slug = self.f_name + '-' + self.l_name + '-' + str(self.zip)
        super(Information, self).save(*args, **kwargs)

class Education(models.Model):
    DEGREE_CHOICES = (
        ('Phd','phd'),
        ('Masters','masters'),
        ('Bachelors','bachelors'),
        ('High School','high_school')
    )
    person = models.ForeignKey(Information, on_delete=models.CASCADE, blank=True, null=True)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, blank=True, null=True)
    stream = models.CharField(max_length=100, blank=True, null=True)
    passing_year = models.DateField(blank=True, null=True)

class Work(models.Model):
    person = models.ForeignKey(Information, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)