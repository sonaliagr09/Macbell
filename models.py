from django.db import models

# Create your models here.

class category(models.Model):

    company_name = models.CharField(max_length = 100)
    company_email = models.CharField(max_length = 100)
    website = models.CharField(max_length = 100)
    company_address = models.CharField(max_length = 100)
    city= models.CharField(max_length = 100)
    industry_choices=(
        ('Education', 'Education'),
        ('IT','IT'),
        ('Electronics','Electronics'),
        ('Manufacturing','Manufacturing'),
        ('Health care','Health care'),
        ('finance','finance')
    )
    industry= models.CharField(max_length=50, choices= industry_choices)
    business_choices=(
        ('enterprise','enterprise'),
        ('collaborator','collaborator'),
        ('investor','investor')
    )
    business= models.CharField(max_length=50, choices= business_choices)
    company= models.TextField()
