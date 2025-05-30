from django.db import models
from django.contrib.auth.models import User

class Notice(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science Engineering'),
        ('ECE', 'Electronics & Communication Engineering'),
        ('EEE', 'Electrical & Electronics Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('IT', 'Information Technology'),
        ('AI', 'Artificial Intelligence'),
        ('DS', 'Data Science'),
        ('GENERAL', 'General'),
    ]

    NOTICE_TYPE_CHOICES = [
        ('ACADEMIC', 'Academic'),
        ('EVENT', 'Event'),
        ('EXAM', 'Examination'),
        ('RESULT', 'Result'),
        ('HOLIDAY', 'Holiday'),
        ('ADMISSION', 'Admission'),
        ('PLACEMENT', 'Placement'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    notice_type = models.CharField(max_length=20, choices=NOTICE_TYPE_CHOICES, default='ACADEMIC')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_important = models.BooleanField(default=False)
    valid_until = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
