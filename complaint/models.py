from django.db import models

class Complaint(models.Model):
    crn_no = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crn_no
    
class Complaint(models.Model):

    crn_no = models.CharField(max_length=100)

    customer_name = models.CharField(max_length=255)

    status = models.CharField(max_length=100)

    email = models.EmailField()

    email_sent = models.BooleanField(default=False)

    email_error = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crn_no