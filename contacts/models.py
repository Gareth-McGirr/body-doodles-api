from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from artists.models import Artist

# Choice fields
REASON_CHOICES = (
    ("general", "General Enquiry"),
    ("account_issue", "Report an issue with your account"),
    ("site_issue", "Report issue with site"),
    ("report", "Report a user")
)

class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reason= models.CharField(
        max_length=25, choices=REASON_CHOICES, default='general'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner} : {self.reason}"
