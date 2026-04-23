from django.db import models
import uuid
 
class Issue(models.Model):
    ISSUE_TYPES = [
        ('water_leak', 'Water Leak'),
        ('electricity_fault', 'Electricity Fault'),
        ('pothole', 'Pothole'),
        ('waste_collection', 'Waste Collection'),
    ]
 
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
 
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reference_number = models.CharField(max_length=20, unique=True, blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)
 
    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = f"FXL-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
 
    def __str__(self):
        return f"{self.reference_number} - {self.get_issue_type_display()}"
