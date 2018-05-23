from django.db import models

class Staff(models.Model):
    STATUS_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    cashier_name = models.CharField(max_length=250)
    cashier_last_name = models.CharField(max_length=250)
    contact_number = models.IntegerField()
    cashier_email = models.EmailField(max_length=70, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


    def __str__(self):
        return self.cashier_name

