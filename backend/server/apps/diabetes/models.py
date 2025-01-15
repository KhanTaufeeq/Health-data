from django.db import models

# Create your models here.
class Diabetes(models.Model):

  fasting_sugar = models.IntegerField('Fasting Sugar', default=0, blank=True, null = True)
  random_sugar = models.IntegerField('Random Sugar', default=0, blank=True, null = True)
  created_at = models.DateTimeField('Noted At', auto_now_add=True)
  updated_at = models.DateTimeField('Update At', auto_now=True) 