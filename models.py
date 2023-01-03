from django.db import models
import datetime
from django.utils import timezone


class My_business(models.Model):

    name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AboutText(models.Model):

    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.business_name


class Message(models.Model):

    business_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.business_name


class My_updates(models.Model):

    title = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    my_date = models.CharField(max_length=20)
    posted_by = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Updates(models.Model):

    title = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    date_posted = models.DateTimeField("Date Posted")
    posted_by = models.CharField(max_length=30)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)
