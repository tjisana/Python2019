from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxLengthValidator


class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    share_price_date = models.DateField(default=now)
    share_price = models.DecimalField(max_digits=8, decimal_places=3)
    comments = models.TextField(default='', validators=[MaxLengthValidator(256)])

    class Meta:
        ordering = ['company_id', 'name']

    def __str__(self):
        return f"{self.company_id} - {self.name}"
