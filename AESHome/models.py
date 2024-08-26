
import datetime
from django.db import models


class Contact_us(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    status = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name + '>>' + self.subject

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'